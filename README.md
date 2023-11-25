# NyaaScraper
Scrape and search for torrents on [nyaa.si](https://nyaa.si) and [sukebei.nyaa.si](https://sukebei.nyaa.si)

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
- `FUN`: "https://nyaa.si"
- `FAP`: "https://sukebei.nyaa.si"

### Filter
- Constants for different filters.

#### Constants
- `NO_FILTER`: 0
- `NO_REMAKES`: 1
- `TRUSTED_ONLY`: 2

### Category
- `ALL_CATEGORIES`: 0
- `ANIME`: 1
- `AUDIO`: 2
- `LITERATURE`: 3
- `LIVE_ACTION`: 4
- `PICTURES`: 5
- `SOFTWARE`: 6