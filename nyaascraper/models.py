from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Union

@dataclass
class File:
    """
    A File of torrent.
    
    Attributes:
        - name (str): Name of the file.
        - size (str): Size of the file.
    """
    name: str
    size: str

@dataclass
class Folder:
    """
    A Folder containing files and folders of torrent.
    
    Attributes:
        - name (str): Name of the folder
        - files (List[File | Folder]): A list of file or folder.
    """
    name: str
    files: List[Union[File, "Folder"]]

@dataclass
class User:
    """
    A Nyaa User.

    Attributes:
        - username (str): Username of the user.
        - profile_url (str): URL of user's profile.
        - photo_url (str): URL of user's profile photo.
    """
    username: str
    profile_url: str
    photo_url: str

@dataclass
class Comment:
    """
    A comment of user on torrent.
    
    Attributes:
        - user (User): User who commented.
        - is_uploader (bool): True, if user is uploader of the torrent, False otherwise.
        - timestamp (datetime.datetime): A datetime object of when the comment was posted.
        - text (str): Text of the comment.
    """
    user: User
    is_uploader: bool
    timestamp: datetime
    text: str

@dataclass
class SearchResult:
    """
    Search result information of a torrent.
    
    Attributes:
        - view_id (int): View id of the torrent.
        - name (str): Name of the torrent.
        - torrent_url (str): URL of the torrent.
        - magnet_link (str): Magnet link of the torrent.
        - size (str): Size of the torrent.
        - timestamp (datetime.datetime): A datetime object of when the torrent was uploaded.
        - seeders (str): Total number of seeders.
        - leechers (str): Total number of leechers.
        - completed (str): Total number of completed.
        - comment_count (int): Count of total comments.
        - category (str): Category of the torrent.
        - subcategory (str): Subcategory of the torrent.
        - category_number (int): Number of the category.
        - subcategory_number (int): Number of the Subcategory.
    """
    view_id: int
    name: str
    torrent_url: str
    magnet_link: str
    size: str
    timestamp: datetime
    seeders: int
    leechers: int
    completed: int
    comment_count: int
    category: str
    subcategory: str
    category_number: int
    subcategory_number: int

@dataclass
class TorrentInfo:
    """
    information of a torrent.
    
    Attributes:
        - view_id (int): View ID of the torrent.
        - name (str): Name of the torrent.
        - magnet_link (str): Magnet link of the torrent.
        - size (str): Size of the torrent.
        - size (str): Size of the torrent.
        - timestamp (datetime.datetime): A datetime object of when the torrent was uploaded.
        - seeders (str): Total number of seeders.
        - leechers (str): Total number of leechers.
        - completed (str): Total number of completed.
        - info_hash (str): Info hash of the torrent.
        - category (str): Category of the torrent.
        - subcategory (str): Subcategory of the torrent.
        - category_number (int): Number of the category.
        - subcategory_number (int): Number of the Subcategory.
        - description (str): Description of the torrent.
        - files (List[File] | List[Folder]): The list of File or Folder.
        - submitter_username (str): Username of the submitter.
        - submitter_link (str, optional) Link of submitter's profile. (None, if submitter is an anonymous).
        - comments (List[Comment], optional): The list of Comment.
    """
    view_id: int
    name: str
    torrent_url: str
    magnet_link: str
    size: str
    timestamp: datetime
    seeders: int
    leechers: int
    completed: int
    info_hash: str
    category: str
    subcategory: str
    category_number: int
    subcategory_number: int
    description: str
    files: Union[List[File], List[Folder]]
    submitter_username: str
    submitter_link: Optional[str] = None
    comments: Optional[List[Comment]] = field(default_factory=list)