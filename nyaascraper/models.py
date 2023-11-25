from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Union

from .utils import Category, Subcategory

@dataclass
class File:
    name: str
    size: str

@dataclass
class Folder:
    name: str
    files: Union[List[File]]

@dataclass
class User:
    username: str
    profile_url: str
    image_url: str

@dataclass
class Comment:
    user: User
    is_uploader: bool
    timestamp: datetime
    text: str

@dataclass
class SearchResult:
    view_id: int
    title: str
    torrent_url: str
    magnet_link: str
    size: str
    timestamp: datetime
    seeders: int
    leechers: int
    completed: int
    comment_count: int
    category: Category
    subcategory: Subcategory
    category_int: int
    subcategory_int: int

@dataclass
class TorrentInfo:
    view_id: int
    title: str
    torrent_url: str
    magnet_link: str
    size: str
    timestamp: datetime
    seeders: int
    leechers: int
    completed: int
    info_hash: str
    category: Category
    subcategory: Subcategory
    category_int: int
    subcategory_int: int
    description: str
    files: Union[List[File], List[Folder]]
    submitter_username: str
    submitter_link: Optional[str] = None
    comments: Optional[List[Comment]] = field(default_factory=list)