from enum import Enum

class FunCategory(Enum):
    """
    Categories for torrents used in SITE.FUN.
    
    Members:
        ALL_CATEGORIES (str): Represents all categories.
        
        ANIME (str): Anime category.
        ANIME_AMV (str): Anime Music Video (AMV) category.
        ANIME_ENGLISH_TRANSLATED (str): Anime - English Translated category.
        ANIME_NON_ENGLISH_TRANSLATED (str): Anime - Non-English Translated category.
        ANIME_RAW (str): Anime - Raw category.
        
        AUDIO (str): Audio category.
        AUDIO_LOSSLESS (str): Audio - Lossless category.
        AUDIO_LOSSY (str): Audio - Lossy category.
        
        LITERATURE (str): Literature category.
        LITERATURE_ENGLISH_TRANSLATED (str): Literature - English Translated category.
        LITERATURE_NON_ENGLISH_TRANSLATED (str): Literature - Non-English Translated category.
        LITERATURE_RAW (str): Literature - Raw category.
        
        LIVE_ACTION (str): Live Action category.
        LIVE_ACTION_ENGLISH_TRANSLATED (str): Live Action - English Translated category.
        LIVE_ACTION_IDOL_PROMOTIONAL_VIDEO (str): Live Action - Idol Promotional Video category.
        LIVE_ACTION_NON_ENGLISH_TRANSLATED (str): Live Action - Non-English Translated category.
        LIVE_ACTION_RAW (str): Live Action - Raw category.
        
        PICTURES (str): Pictures category.
        PICTURES_GRAPHICS (str): Pictures - Graphics category.
        PICTURES_PHOTOS (str): Pictures - Photos category.
        
        SOFTWARE (str): Software category.
        SOFTWARE_APPLICATIONS (str): Software - Applications category.
        SOFTWARE_GAMES (str): Software - Games category.
    """
    ALL_CATEGORIES: str = "0_0"
    ANIME: str = "1_0"
    ANIME_AMV: str = "1_1"
    ANIME_ENGLISH_TRANSLATED: str = "1_2"
    ANIME_NON_ENGLISH_TRANSLATED: str = "1_3"
    ANIME_RAW: str = "1_4"
    
    AUDIO: str = "2_0"
    AUDIO_LOSSLESS: str = "2_1"
    AUDIO_LOSSY: str = "2_2"
    
    LITERATURE: str = "3_0"
    LITERATURE_ENGLISH_TRANSLATED: str = "3_1"
    LITERATURE_NON_ENGLISH_TRANSLATED: str = "3_2"
    LITERATURE_RAW: str = "3_3"
    
    LIVE_ACTION: str = "4_0"
    LIVE_ACTION_ENGLISH_TRANSLATED: str = "4_1"
    LIVE_ACTION_IDOL_PROMOTIONAL_VIDEO: str = "4_2"
    LIVE_ACTION_NON_ENGLISH_TRANSLATED: str = "4_3"
    LIVE_ACTION_RAW: str = "4_4"
    
    PICTURES: str = "5_0"
    PICTURES_GRAPHICS: str = "5_1"
    PICTURES_PHOTOS: str = "5_2"
    
    SOFTWARE: str = "6_0"
    SOFTWARE_APPLICATIONS: str = "6_1"
    SOFTWARE_GAMES: str = "6_2"

class FapCategory(Enum):
    """
    Categories for torrents used in SITE.FAP.
    
    Members:
        ALL_CATEGORIES (str): Represents all categories.
        
        ART (str): Art category.
        ART_ANIME (str): Art - Anime category.
        ART_DOUJINSHI (str): Art - Doujinshi category.
        ART_GAMES (str): Art - Games category.
        ART_MANGA (str): Art - Manga category.
        ART_PICTURES (str): Art - Pictures category.
        
        REAL_LIFE (str): Real Life category.
        REAL_LIFE_PHOTOBOOKS_AND_PICTURES (str): Real Life - Photobooks and Pictures category.
        REAL_LIFE_VIDEOS (str): Real Life - Videos category.
    """
    ALL_CATEGORIES: str = "0_0"
    
    ART: str = "1_0"
    ART_ANIME: str = "1_1"
    ART_DOUJINSHI: str = "1_2"
    ART_GAMES: str = "1_3"
    ART_MANGA: str = "1_4"
    ART_PICTURES: str = "1_5"
    
    REAL_LIFE: str = "2_0"
    REAL_LIFE_PHOTOBOOKS_AND_PICTURES: str = "2_1"
    REAL_LIFE_VIDEOS: str = "2_2"