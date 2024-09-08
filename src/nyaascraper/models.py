from typing import Self
from dataclasses import dataclass
from datetime import datetime
import time

from .enums import FunCategory, FapCategory, TorrentType, UserLevel

@dataclass
class SearchResultTorrent:
    """
    Represents a search result torrent.
    
    Attributes:
        torrent_type (TorrentType): The type of the torrent.
        view_id (int): The View-ID of the torrent.
        category (FunCategory | FapCategory): The category of the torrent.
        category_icon_url (str): The URL of the icon of category.
        torrent_url (str): The URL of the torrent file.
        magnet_link (str): The Magnet Link of the torrent.
        size (str): The size of the torrent.
        timestamp (datetime): The timestamp of when the torrent was uploaded.
        seeders (int): The number of seeders of the torrent.
        leechers (int): The number of leechers of the torrent.
        completed (int): The number of times the torrent has been completed.
        total_comments (int): The number of total comments.
    """
    torrent_type: TorrentType
    view_id: int
    name: str
    category: FunCategory | FapCategory
    category_icon_url: str
    torrent_url: str
    magnet_link: str
    size: str
    timestamp: datetime
    seeders: int
    leechers: int
    completed: int
    total_comments: int

@dataclass
class SearchResult:
    """
    Search result.
    
    Attributes:
        torrents (list[SearchResultTorrent]): A list of `SearchResultTorrent` objects.
        displaying_from (int): The number of results displaying from.
        displaying_to (int): The number of results displaying to.
        total_results (int): The number of total results.
        current_page (int): The number of current result page.
        previous_page (int, optional): The number of previous result page. Defaults to None.
        next_page (int, optional): The number of next result page. Defaults to None.
        available_pages (int, optional): The number of currently available result pages. If exceeded, there might be more result pages available. Defaults to None.
    """
    torrents: list[SearchResultTorrent]
    displaying_from: int
    displaying_to: int
    total_results: int
    current_page: int
    previous_page: int | None = None
    next_page: int | None = None
    available_pages: int | None = None

@dataclass
class User:
    """
    An User.
    
    Attributes:
        username (str): The username of the user.
        profile_url (str): The URL of the user.
        photo_url (str, optional): The URL of the photo of the user. Defaults to None.
        user_level: (UserLevel, optional): The level of the user.
        is_banned: (bool, optional): Indicates if the user is banned.
    """
    username: str
    profile_url: str
    photo_url: str | None = None
    user_level: UserLevel | None = None
    is_banned: bool | None = None

@dataclass
class File:
    """
    A File.
    
    Attributes:
        name (str): The name of the file.
        size (str): The size of the file.
    """
    name: str
    size: str

@dataclass
class Folder:
    """
    A Folder.
    
    Attributes:
        name (str): The name of the folder.
        files (File | Folder): A list of `File` or `Folder` objects.
    """
    name: str
    files: list[File | Self]

@dataclass
class Comment:
    """
    A Comment.
    
    Attributes:
        id (int): The ID of the comment.
        user (User): The user who commented.
        is_uploader (bool): Indicates if the user is uploader of the torrent.
        timestamp (datetime): The timestamp of when the comment was made.
        text (str): The text of the comment.
    """
    id: int
    user: User
    is_uploader: bool
    timestamp: datetime
    text: str

@dataclass
class TorrentInfo:
    """
    Torrent information.
    
    Attributes:
        name (str): The name of the torrent.
        category (FunCategory | FapCategory): The category of the torrent.
        torrent_url (str): The URL of the torrent file.
        magnet_link (str): The Magnet Link of the torrent.
        size (str): The size of the torrent.
        timestamp (datetime): The timestamp of when the torrent was uploaded.
        seeders (str): The number of seeders of the torrent.
        leechers (str): The number of leechers of the torrent.
        completed (str): The number of times the torrent has been completed.
        info_hash (str): The info hash of the torrent.
        submitter (User | None): The user who uploaded this torrent. If anonymous, the value is None.
        information (str): The information of the torrent.
        description (str): The description of the torrent.
        files (list[File | Folder]): A list of torrent files.
        total_comments (int): The number of total comments on the torrent.
        comments (list[Comment]): A list of comments on the torrent.
    """
    name: str
    category: FunCategory | FapCategory
    torrent_url: str
    magnet_link: str
    size: str
    timestamp: datetime
    seeders: int
    leechers: int
    completed: int
    info_hash: str
    submitter: User | None
    information: str
    description: str
    files: list[File | Folder]
    total_comments: int
    comments: list[Comment]

@dataclass
class NyaaRSSTorrent:
    """
    Represents a torrent entry from Nyaa RSS feed.
    
    Attributes:
        torrent_type (TorrentType): The type of the torrent.
        view_id (int): The View-ID of the torrent.
        name (str): The name of the torrent.
        category (FunCategory | FapCategory): The category of the torrent.
        size (str): The size of the torrent.
        published (str): The published date/time string.
        published_parsed (time.struct_time): The published date/time as a `time.struct_time` object.
        torrent_url (str | None): The URL of the torrent file.
        magnet_link (str | None): The magnet link.
        seeders (int): The number of seeders of the torrent.
        leechers (int): The number of leechers of the torrent.
        completed (int): The number of times the torrent has been completed.
        info_hash (str): The info hash of the torrent.
        description (str): The CDATA of the RSS feed of the torrent.
        total_comments (int): The number of total comments on the torrent.
    """
    
    torrent_type: TorrentType
    view_id: int
    name: str
    category: FunCategory | FapCategory
    size: str
    published: str
    published_parsed: time.struct_time
    torrent_url: str | None
    magnet_link: str | None
    seeders: int
    leechers: int
    completed: int
    info_hash: str
    description: str
    total_comments: int

@dataclass
class NyaaRSSFeed:
    """
    Nyaa RSS Feed.
    
    Attributes:
        title (str): The title of the RSS feed.
        description (str): The description of the RSS feed.
        torrents (list[NyaaRSSTorrent]): A list of torrents in the RSS feed.
    """
    title: str
    description: str
    torrents: list[NyaaRSSTorrent]