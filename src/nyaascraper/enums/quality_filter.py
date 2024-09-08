from enum import IntEnum

class QualityFilter(IntEnum):
    """
    Quality filters for torrents.
    
    Members:
        NO_FILTER (int): No filtering applied.
        NO_REMAKES (int): Filters out torrents labeled as remakes.
        TRUSTED_ONLY (int): Filters torrents by trusted users only.
    """
    NO_FILTER: int = 0
    NO_REMAKES: int = 1
    TRUSTED_ONLY: int = 2