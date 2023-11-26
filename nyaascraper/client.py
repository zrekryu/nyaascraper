from datetime import datetime
from typing import List, Optional, Union

from bs4 import BeautifulSoup, ResultSet, Tag
import httpx

from .exceptions import TorrentNotFoundError
from .models import(
    SearchResult, TorrentInfo,
    File, Folder,
    User, Comment
    )
from .utils import (
    SITE,
    Filter, Category, Subcategory,
    SortBy, SortOrder
    )

class NyaaClient:
    def __init__(self: "NyaaClient", base_url: str = SITE.FUN) -> None:
        """
        Initialize NyaaClient.
        
        PARAMETERS:
            base_url (str): The base URL. (default: SITE.FUN)
        """
        self.base_url = base_url
        self.client = httpx.AsyncClient()
    
    async def search(
        self: "NyaaClient",
        query: Optional[str] = "",
        username: Optional[str] = "",
        filter_: Optional[Filter] = Filter.NO_FILTER,
        category: Optional[Category] = Category.ALL_CATEGORIES,
        subcategory: Optional[Subcategory] = Subcategory.ALL_SUBCATEGORIES,
        sort_by: Optional[SortBy] = None,
        order: Optional[SortOrder] = None,
        page: Optional[int] = 1
        ) -> Optional[List[SearchResult]]:
        """
        Search for torrents.
        
        Parameters:
            query (optional, str): Query to search torrents.
            username (optional, str): Search torrents uploaded by this user.
            filter_ (optional, str): Filter torrents (default: Filter.NO_FILTER)
            category (optional, int): Get torrents based on category. (default: Category.ALL_CATEGORIES)
            subcategory (optional, int): Get torrents based on subcategory. (default: Subcategory.ALL_SUBCATEGORIES)
            sort_by (optional, str): Sort torrents by comments, size, date, seeders, leechers and completed. (default: None)
            order (optional, str): Order of sorting torrents. (default: None)
            page (optional, int): The page number of the torrent list. (default: 1)
        
        Returns:
            List[SearchResult]: A list of search result.
        """
        params = {
            "q": query,
            "f": filter_,
            "c": str(category) + "_" + str(subcategory),
            "p": page,
            **({"s": sort_by} if sort_by else {}),
            **({"o": order} if order else {})
        }
        
        url = f"{self.base_url}/user/{username}" if username else self.base_url
        response = await self.client.get(url, params=params)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, "html.parser")
        rows = soup.select("table.torrent-list tbody tr")
        
        results = []
        for row in rows:
            comment_count = int(x.text) if (x := row.select_one("td[colspan='2'] a.comments")) else 0
            achor_tag = row.select_one("td[colspan='2'] a[href^='/view/']")
            title, view_id = achor_tag.text, int(achor_tag["href"][6:].strip("#comments"))
            
            tds = row.select("td.text-center")
            torrent_url = self.base_url + tds[0].select_one("a[href^='/download/']")["href"]
            magnet_link = tds[0].select_one("a[href^='magnet:?xt=']")["href"]
            size = tds[1].text
            timestamp = datetime.utcfromtimestamp(int(tds[2]["data-timestamp"]))
            seeders = int(tds[3].text)
            leechers = int(tds[4].text)
            completed = int(tds[5].text)
            
            category_achor_tag = row.select_one("td a[href^='/?c=']")
            category, subcategory = category_achor_tag["title"].split(" - ")
            category_int, subcategory_int = [int(x) for x in category_achor_tag["href"][4:].split("_")]
            
            results.append(
                SearchResult(
                    view_id=view_id,
                    title=title,
                    torrent_url=torrent_url,
                    magnet_link=magnet_link,
                    size=size,
                    timestamp=timestamp,
                    seeders=seeders,
                    leechers=leechers,
                    completed=completed,
                    comment_count=comment_count,
                    category=category,
                    subcategory=subcategory,
                    category_int=category_int,
                    subcategory_int=subcategory_int
                    )
                )
        return results
    
    def __get_all_files_and_folders(self: "NyaaClient", list_items: Union[ResultSet, List[Tag]]) -> Union[List[File], List[Folder]]:
        """
        Get all files and folders, including nested ones.
        
        Parameters:
            list_items (Union[ResultSet, List[Tag]]): A collection of BeautifulSoup tags representing files and folders.
        
        Returns:
            Union[List[File], List[Folder]]: A list containing File and Folder objects representing files and folders, including nested ones.
        """
        file_and_folders = []
        for item in list_items:
            if (folder := item.find("a", class_="folder")):
                files = self.__get_all_files_and_folders(folder.find_next("ul").find_all("li"))
                file_and_folders.append(
                    Folder(
                        name=folder.text,
                        files=files
                        )
                    )
            elif (file := item.find("i", class_="fa-file").parent):
                file_and_folders.append(
                    File(
                        name=file.find(text=True, recursive=False).strip(),
                        size=file.find("span").text.strip("()")
                        )
                    )
        return file_and_folders
    
    async def get_torrent_info(self: "NyaaClient", view_id: int) -> TorrentInfo:
        """
        Get information about the torrent.
        
        Parameters:
            view_id (int): The view id of the torrent.
        
        Raises:
            TorrentNotFoundError: Torrrent not found.
            HTTPError: HTTp request error.
        
        Returns:
            TorrentInfo: Information about the torrent.
        """
        response = await self.client.get(self.base_url + f"/view/{view_id}")
        if response.status_code == 404:
            raise TorrentNotFoundError(f"Torrent '{view_id}' not found")
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        title = soup.select_one("div.panel-heading h3.panel-title").get_text(strip=True)
        timestamp = datetime.utcfromtimestamp(int(soup.select_one("div.panel-body div[data-timestamp]")["data-timestamp"]))
        
        rows = soup.select("div.panel-body div.row")
        
        category_achor_tags = rows[0].select("a[href^='/?c=']")
        category, subcategory = category_achor_tags[0].text, category_achor_tags[1].text
        category_int, subcategory_int = [int(x) for x in category_achor_tags[1]["href"][4:].split("_")]
        
        if (submitter := rows[1].select_one("a[href^='/user/']")):
            submitter_username = submitter.text
            submitter_link = self.base_url + submitter["href"]
        else:
            submitter_username = "Anonymous"
            submitter_link = None
        
        seeders = int(rows[1].select_one("span[style='color: green;']").text)
        information = rows[2].select_one("div:nth-of-type(2)").get_text(strip=True)
        leechers = int(rows[2].select_one("span[style='color: red;']").text)
        size = rows[3].select_one("div:nth-of-type(2)").text
        completed = int(rows[3].select_one("div:nth-of-type(4)").text)
        info_hash = rows[4].select_one("div kbd").text
        torrent_url = self.base_url +  soup.select_one("div.panel-footer a[href^='/download/']")["href"]
        magnet_link = soup.select_one("div.panel-footer a[href^='magnet:?xt=']")["href"]
        description = soup.find("div", {"id": "torrent-description"}).text
        files = self.__get_all_files_and_folders(soup.select("div.torrent-file-list ul li:not(li li)"))
        
        comments = []
        for comment in soup.select("div[id='comments'] div[id='collapse-comments'] div.comment-panel"):
            user = comment.select_one("a[href^='/user/']")
            username, profile_url = user.text, self.base_url + user["href"]
            image_url = comment.find("img", class_="avatar")["src"]
            comments.append(
                Comment(
                    user=User(username=username, profile_url=profile_url, image_url=image_url),
                    is_uploader=True if "(uploader)" in comment.find("p").text else False,
                    timestamp=datetime.utcfromtimestamp(int(comment.select_one("small[data-timestamp]")["data-timestamp"])),
                    text=comment.find("div", class_="comment-content").text
                    )
                )
        
        return TorrentInfo(
            view_id=view_id,
            title=title,
            torrent_url=torrent_url,
            magnet_link=magnet_link,
            size=size,
            timestamp=timestamp,
            seeders=seeders,
            leechers=leechers,
            completed=completed,
            info_hash=info_hash,
            category=category,
            subcategory=subcategory,
            category_int=category_int,
            subcategory_int=subcategory_int,
            description=description,
            files=files,
            submitter_username=submitter_username,
            submitter_link=submitter_link,
            comments=comments
            )