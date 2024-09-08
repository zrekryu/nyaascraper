from enum import Enum

class SortBy(Enum):
    """
    Sorting options for torrents.
    
    Members:
        COMMENTS (str): Sort by comments.
        SIZE (str): Sort by size.
        DATE (str): Sort by date.
        SEEDERS (str): Sort by seeders.
        LEECHERS (str): Sort by leechers.
        DOWNLOADS (str): Sort by downloads.
    """
    COMMENTS = "comments"
    SIZE = "size"
    DATE = "id"
    SEEDERS = "seeders"
    LEECHERS = "leechers"
    DOWNLOADS = "downloads"

class SortOrder(Enum):
    """
    Sorting order for torrents.
    
    Members:
        ASCENDING (str): Ascending order.
        DESCENDING (str): Descending order.
    """
    ASCENDING = "asc"
    DESCENDING = "desc"