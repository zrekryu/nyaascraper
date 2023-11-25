# NyaaScraper
Scrap and search for torrents avaiable at [nyaa.si](https://nyaa.si) and [sukebei.nyaa.si](https://sukebei.nyaa.si)

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

### Search torrents
```py
import asyncio

from nyaascraper import NyaaClient

client = NyaaClient()

async def main() -> None:
    torrents = await client.search("Naruto")
    print(torrents)

asyncio.run(main())
```

### Search torrents using filter.
```py
from nyaascraper.utils import Filter

await client.search("Naruto", filter_=Filter.NO_REMAKES)
```

### Search torrents using category and sub-category.
```py
from nyaascraper.utils import Category, Subcategory

await client.search("Naruto", category=Category.ANIME, subcategory=Subcategory.ANIME.RAW)
```

For more, `help(NyaaClient.search)`

### Changing site
```py
from nyaascraper.utils import NyaaClient, SITE

client = NyaaClient(SITE.FAP) # scrap sukebei.nyaa.si
```
