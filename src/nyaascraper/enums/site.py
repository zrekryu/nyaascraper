from enum import Enum

class SITE(Enum):
    """
    Sites for the scraper client.
    
    Members:
        FUN (str): URL for the work-safe site, nyaa.si.
        FAP (str): URL for the non-work-safe site, sukebei.nyaa.si.
    """
    FUN = "https://nyaa.si"
    FAP = "https://sukebei.nyaa.si"