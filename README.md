# NyaaScraper
An asynchronous library for scraping and searching torrents on [nyaa.si](https://nyaa.si) and [sukebei.nyaa.si](https://sukebei.nyaa.si).

## Installation

### Using pip:
```bash
pip install nyaascraper
```

### Local Setup:
```bash
git clone https://github.com/zrekryu/nyaascraper
pip install -r requirements.txt
python setup.py install
```

## Usage

### Search Torrents:
```py
import asyncio

from nyaascraper import NyaaClient

client = NyaaClient()

async def main() -> None:
    torrents = await client.search("Naruto")
    print(torrents)

asyncio.run(main())
```

### Search with Filter:
```py
from nyaascraper.utils import Filter

await client.search("Naruto", filter_=Filter.NO_REMAKES)
```

### Search with Category and Sub-category:
```py
from nyaascraper.utils import Category, Subcategory

await client.search("Naruto", category=Category.ANIME, subcategory=Subcategory.ANIME.RAW)
```

### Sorting Torrents:
```py
from nyaascraper.utils import SortBy, SortOrder

await client.search("Naruto", sort_by=SortBy.SEEDERS, sort_order=SortOrder.DESCENDING)
```

### Search Torrents on Specific Page:
```py
await client.search("Naruto", page=3)
```

## Search torrents by Username:
To search for torrents uploaded by a specific user.
```py
await client.search("Naruto", username="Erai-raws")
```

### Use sukebei.nyaa.si:
```py
from nyaascraper.utils import NyaaClient, SITE

client = NyaaClient(SITE.FAP)
```

### Getting torrent information:
```py
torrents = await client.search("Doraemon")
await client.get_torrent_info(torrents[0].view_id)
```

## Utils

### SITE
- Constants for different sites.

#### Constants
- `FUN`: "https://nyaa.si"
- `FAP`: "https://sukebei.nyaa.si"

### Filter
- Constants for different filters.

#### Constants
- `NO_FILTER`: 0
- `NO_REMAKES`: 1
- `TRUSTED_ONLY`: 2

### Category
- Constants for different torrent categories.

#### Constants
- `ALL_CATEGORIES`: 0
- `ANIME`: 1
- `AUDIO`: 2
- `LITERATURE`: 3
- `LIVE_ACTION`: 4
- `PICTURES`: 5
- `SOFTWARE`: 6
- `ART`: 1
- `REAL_LIFE`: 2

### Subcategory
- Constants for different torrent subcategories.

#### Anime Subcategories (`Subcategory.ANIME`)
- **Anime Music Video (`Subcategory.ANIME.ANIME_MUSIC_VIDEO`):** 1
- **English Translation (`Subcategory.ANIME.ENGLISH_TRANSLATION`):** 2
- **Non-English Translation (`Subcategory.ANIME.NON_ENGLISH_TRANSLATION`):** 3
- **Raw (`Subcategory.ANIME.RAW`):** 4

#### Audio Subcategories (`Subcategory.AUDIO`)
- **Lossless (`Subcategory.AUDIO.LOSSLESS`):** 1
- **Lossy (`Subcategory.AUDIO.LOSSY`):** 2

#### Literature Subcategories (`Subcategory.LITERATURE`)
- **English Translation (`Subcategory.LITERATURE.ENGLISH_TRANSLATION`):** 1
- **Non-English Translation (`Subcategory.LITERATURE.NON_ENGLISH_TRANSLATION`):** 2
- **Raw (`Subcategory.LITERATURE.RAW`):** 3

#### Live Action Subcategories (`Subcategory.LIVE_ACTION`)
- **English Translation (`Subcategory.LIVE_ACTION.ENGLISH_TRANSLATION`):** 1
- **Idol Promotional Video (`Subcategory.LIVE_ACTION.IDOL_PROMOTIONAL_VIDEO`):** 2
- **Non-English Translation (`Subcategory.LIVE_ACTION.NON_ENGLISH_TRANSLATION`):** 3
- **Raw (`Subcategory.LIVE_ACTION.RAW`):** 4

#### Pictures Subcategories (`Subcategory.PICTURES`)
- **Graphics (`Subcategory.PICTURES.GRAPHICS`):** 1
- **Photos (`Subcategory.PICTURES.PHOTOS`):** 2

#### Software Subcategories (`Subcategory.SOFTWARE`)
- **Apps (`Subcategory.SOFTWARE.APPS`):** 1
- **Games (`Subcategory.SOFTWARE.GAMES`):** 2

#### Art Subcategories (`Subcategory.ART`)
- **Anime (`Subcategory.ART.ANIME`):** 1
- **Doujinshi (`Subcategory.ART.DOUJINSHI`):** 2
- **Games (`Subcategory.ART.GAMES`):** 3
- **Manga (`Subcategory.ART.MANGA`):** 4
- **Pictures (`Subcategory.ART.PICTURES`):** 5

#### Real Life Subcategories (`Subcategory.REAL_LIFE`)
- **Pictures (`Subcategory.REAL_LIFE.PICTURES`):** 1
- **Videos (`Subcategory.REAL_LIFE.VIDEOS`):** 2

### SortBy
- Constants for different sorting options for torrents.

#### Constants
- `COMMENTS`: "comments"
- `SIZE`: "size"
- `DATE`: "id"
- `SEEDERS`: "seeders"
- `LEECHERS`: "leechers"
- `COMPLETED`: "downloads"

### SortOrder
- Constants for different sorting orders for torrents.

#### Constants
- `ASCENDING`: "asc"
- `DESCENDING`: "desc"

## LICENSE
Licensed under the [Unlicense](https://unlicense.org/).