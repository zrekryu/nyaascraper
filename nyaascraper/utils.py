class SITE:
    """
    Class representing Nyaa.si site URLs.

    Attributes:
        - FUN (str): URL for Nyaa.si.
        - FAP (str): URL for Sukebei.nyaa.si.
    """
    FUN = "https://nyaa.si"
    FAP = "https://sukebei.nyaa.si"

class Filter:
    """
    Enumeration of filters for torrent search.

    Attributes:
        - NO_FILTER (int): No filtering.
        - NO_REMAKES (int): Exclude remakes.
        - TRUSTED_ONLY (int): Show only trusted torrents.
    """
    NO_FILTER = 0
    NO_REMAKES = 1
    TRUSTED_ONLY = 2

class Category:
    """
    Enumeration of torrent categories.

    Attributes:
        - ALL_CATEGORIES (int): All categories.
        - ANIME (int): Anime category.
        - AUDIO (int): Audio category.
        - LITERATURE (int): Literature category.
        - LIVE_ACTION (int): Live Action category.
        - PICTURES (int): Pictures category.
        - SOFTWARE (int): Software category.
        
        - ART (int): Art category.
        - REAL_LIFE (int): Real Life category.
    """
    ALL_CATEGORIES = 0
    ANIME = 1
    AUDIO = 2
    LITERATURE = 3
    LIVE_ACTION = 4
    PICTURES = 5
    SOFTWARE = 6
    
    # FAP : SUKEBEI
    ART = 1
    REAL_LIFE = 2

class SubcateogryAnime:
    """
    Subcategories for the Anime category.

    Attributes:
        - ANIME_MUSIC_VIDEO (int): Anime Music Video.
        - ENGLISH_TRANSLATION (int): English Translation.
        - NON_ENGLISH_TRANSLATION (int): Non-English Translation.
        - RAW (int): Raw.
    """
    ANIME_MUSIC_VIDEO = 1
    ENGLISH_TRANSLATION = 2
    NON_ENGLISH_TRANSLATION = 3
    RAW = 4

class SubcateogryAudio:
    """
    Subcategories for the Audio category.

    Attributes:
        - LOSSLESS (int): Lossless.
        - LOSSY (int): Lossy.
    """
    LOSSLESS = 1
    LOSSY = 2

class SubcateogryLiterature:
    """
    Subcategories for the Literature category.

    Attributes:
        - ENGLISH_TRANSLATION (int): English Translation.
        - NON_ENGLISH_TRANSLATION (int): Non-English Translation.
        - RAW (int): Raw.
    """
    ENGLISH_TRANSLATION = 1
    NON_ENGLISH_TRANSLATION = 2
    RAW = 3

class SubcateogryLiveAction:
    """
    Subcategories for the Live Action category.

    Attributes:
        - ENGLISH_TRANSLATION (int): English Translation.
        - IDOL_PROMOTIONAL_VIDEO (int): Idol Promotional Video.
        - NON_ENGLISH_TRANSLATION (int): Non-English Translation.
        - RAW (int): Raw.
    """
    ENGLISH_TRANSLATION = 1
    IDOL_PROMOTIONAL_VIDEO = 2
    NON_ENGLISH_TRANSLATION = 3
    RAW = 4

class SubcateogryPictures:
    """
    Subcategories for the Pictures category.

    Attributes:
        - GRAPHICS (int): Graphics.
        - PHOTOS (int): Photos.
    """
    GRAPHICS = 1
    PHOTOS = 2

class SubcateogrySoftware:
    """
    Subcategories for the Software category.

    Attributes:
        - APPS (int): Apps.
        - GAMES (int): Games.
    """
    APPS = 1
    GAMES = 2

# FAP : SUKEBEI
class SubcateogryArt:
    """
    Subcategories for the Art category (FAP : SUKEBEI).

    Attributes:
        - ANIME (int): Anime.
        - DOUJINSHI (int): Doujinshi.
        - GAMES (int): Games.
        - MANGA (int): Manga.
        - PICTURES (int): Pictures.
    """
    ANIME = 1
    DOUJINSHI = 2
    GAMES = 3
    MANGA = 4
    PICTURES = 5

class SubcateogryRealLife:
    """
    Subcategories for the Real Life category (FAP : SUKEBEI).

    Attributes:
        - PICTURES (int): Pictures.
        - VIDEOS (int): Videos.
    """
    PICTURES = 1
    VIDEOS = 2

class Subcategory:
    """
    Subcategories for different torrent categories.

    Attributes:
        - ALL_SUBCATEGORIES (int): Represents all subcategories.

        - ANIME (SubcateogryAnime): Subcategories for the Anime category.
        - AUDIO (SubcateogryAudio): Subcategories for the Audio category.
        - LITERATURE (SubcateogryLiterature): Subcategories for the Literature category.
        - LIVE_ACTION (SubcateogryLiveAction): Subcategories for the Live Action category.
        - PICTURES (SubcateogryPictures): Subcategories for the Pictures category.
        - SOFTWARE (SubcateogrySoftware): Subcategories for the Software category.

        - ART (SubcateogryArt): Subcategories for the Art category.
        - REAL_LIFE (SubcateogryRealLife): Subcategories for the Real Life category.
    """
    ALL_SUBCATEGORIES = 0
    
    ANIME = SubcateogryAnime
    AUDIO = SubcateogryAudio
    LITERATURE = SubcateogryLiterature
    LIVE_ACTION = SubcateogryLiveAction
    PICTURES = SubcateogryPictures
    SOFTWARE = SubcateogrySoftware
    
    # FAP : SUKEBEI
    ART = SubcateogryArt
    REAL_LIFE = SubcateogryRealLife

class SortBy:
    """
    Enumeration of sorting options for torrents.

    Attributes:
        - COMMENTS (str): Sort by comments.
        - SIZE (str): Sort by size.
        - DATE (str): Sort by date.
        - SEEDERS (str): Sort by seeders.
        - LEECHERS (str): Sort by leechers.
        - COMPLETED (str): Sort by completed downloads.
    """
    COMMENTS = "comments"
    SIZE = "size"
    DATE = "id"
    SEEDERS = "seeders"
    LEECHERS = "leechers"
    COMPLETED = "downloads"

class SortOrder:
    """
    Enumeration of sorting orders for torrents.

    Attributes:
        - ASCENDING (str): Ascending order.
        - DESCENDING (str): Descending order.
    """
    ASCENDING = "asc"
    DESCENDING = "desc"