from typing import Self

import httpx
import feedparser

from .enums import SITE, QualityFilter, FunCategory, FapCategory, TorrentType
from .utils.categories import get_category_by_id

from .models import NyaaRSSFeed, NyaaRSSTorrent

class NyaaRSSClient:
    DEFAULT_SITE: SITE = SITE.FUN
    TIMEOUT: int = 30
    
    def __init__(self: Self, site: SITE = DEFAULT_SITE, timeout: int = TIMEOUT) -> None:
        """
        Initialize rss client.
        
        Parameters:
            site (SITE, optional): The site to fetch from. Defaults to DEFAULT_SITE.
            timeout (int, optional): The timeout for HTTP requests. Defaults to TIMEOUT.
        """
        self._site = site
        self.base_url = site.value
        self.timeout = timeout
        
        self._http_client: httpx.AsyncClient = httpx.AsyncClient(timeout=self.timeout)
    
    @property
    def site(self: Self) -> SITE:
        """
        Getter property for the current site of the client.
        
        Returns:
            SITE: The current site used by the client.
        """
        return self._site
    
    @site.setter
    def site(self: Self, new_site: SITE) -> None:
        """
        Set the site to fetch from.
        
        Parameters:
            new_site (SITE): The new site to set.
        """
        self._site = new_site
        self.base_url = new_site.value
    
    async def get_feed(
        self: Self,
        term: str | None = None,
        username: str | None = None,
        quality_filter: QualityFilter | int = QualityFilter.NO_FILTER,
        category: FunCategory | FapCategory | int | None = None,
        use_magnet: bool | None = None
        ) -> NyaaRSSFeed:
        """
        Parameters:
            term (str | None, optional): Search term. Defaults to None.
            username (str | None, optional): Search torrents of a user. Defaults to None.
            quality_filter (QualityFilter | int | None, optional): Filter torrents by quality. If not specified, defaults to QualityFilter.NO_FILTER.
            category (FunCategory | FapCategory | int | None, optional): Filter torrents by category. If None, a default category is used. Defaults to None.
            use_magnet (bool | None, optional): Whether or not to use magnet links. Defaults to None.
        
        Raises:
            httpx.HTTPError: If an HTTP-related error occurs during the request.
        
        Returns:
            NyaaRSSFeed: RSS feed.
        """
        if category is None:
            category = get_category_by_id(self.site, "0_0")
        
        params = {
            "page": "rss",
            "q": term,
            "u": username,
            "f": quality_filter.value if isinstance(quality_filter, QualityFilter) else quality_filter,
            "c": category.value if isinstance(category, (FunCategory, FapCategory)) else category,
            "magnets": use_magnet
        }
        
        response: httpx.Response = await self._http_client.get(self.base_url, params={k: v for k, v in params.items() if v is not None})
        response.raise_for_status()
        
        parsed_feed = feedparser.parse(response.text)
        
        torrents: list[NyaaRSSTorrent] = []
        for entry in parsed_feed.entries:
            torrent_type = TorrentType.NORMAL
            if entry.nyaa_trusted.lower() == "yes":
                torrent_type = TorrentType.TRUSTED
            elif entry.nyaa_remake.lower() == "yes":
                torrent_type = TorrentType.REMAKE
            
            view_id = int(entry.guid.split("/view/")[-1])
            category = get_category_by_id(site=self.site, category_id=entry.nyaa_categoryid)
            
            torrents.append(
                NyaaRSSTorrent(
                    torrent_type=torrent_type,
                    view_id=view_id,
                    name=entry.title,
                    category=category,
                    size=entry.nyaa_size,
                    published=entry.published,
                    published_parsed=entry.published_parsed,
                    torrent_url=entry.link if not use_magnet else None,
                    magnet_link=entry.link if use_magnet else None,
                    seeders=int(entry.nyaa_seeders),
                    leechers=int(entry.nyaa_leechers),
                    completed=int(entry.nyaa_downloads),
                    info_hash=entry.nyaa_infohash,
                    description=entry.description,
                    total_comments=int(entry.nyaa_comments)
                    )
                )
        
        return NyaaRSSFeed(
            title=parsed_feed.feed.title,
            description=parsed_feed.feed.description,
            torrents=torrents
            )