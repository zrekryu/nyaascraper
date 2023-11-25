class SITE:
    FUN = "https://nyaa.si"
    FAP = "https://sukebei.nyaa.si"

class Filter:
    NO_FILTER = 0
    NO_REMAKES = 1
    TRUSTED_ONLY = 2

class Category:
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
    ANIME_MUSIC_VIDEO = 1
    ENGLISH_TRANSLATION = 2
    NON_ENGLISH_TRANSLATION = 3
    RAW = 4

class SubcateogryAudio:
    LOSSLESS = 1
    LOSSY = 2

class SubcateogryLiterature:
    ENGLISH_TRANSLATION = 1
    NON_ENGLISH_TRANSLATION = 2
    RAW = 3

class SubcateogryLiveAction:
    ENGLISH_TRANSLATION = 1
    IDOL_PROMOTIONAL_VIDEO = 2
    NON_ENGLISH_TRANSLATION = 3
    RAW = 4

class SubcateogryPictures:
    GRAPHICS = 1
    PHOTOS = 2

class SubcateogrySoftware:
    APPS = 1
    GAMES = 2

# FAP : SUKEBEI
class SubcateogryArt:
    ANIME = 1
    DOUJINSHI = 2
    GAMES = 3
    MANGA = 4
    PICTURES = 5

class SubcateogryRealLife:
    PICTURES = 1
    VIDEOS = 2

class Subcategory:
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
    COMMENTS = "comments"
    SIZE = "size"
    DATE = "id"
    SEEDERS = "seeders"
    LEECHERS = "leechers"
    COMPLETED = "downloads"

class SortOrder:
    ASCENDING = "asc"
    DESCENDING = "desc"