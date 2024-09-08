# nyaascraper

`nyaascraper` is an asynchronous Python library for scraping [nyaa.si](https://nyaa.si) and [sukebei.nyaa.si](https://sukebei.nyaa.si).

# Installation

Installing through pip:

```bash
pip install nyaascraper
```

# Usage

## Initializing Client with Site

By default, the site is nyaa.si (work-safe site).

```py
from nyaascraper import NyaaClient, SITE

# Work-safe site. (Default)
client = NyaaClient(SITE.FUN)

# Non-work-safe site.
client = NyaaClient(SITE.FAP)
```

## Changing Site

Changing the site of the client dynamically.

```py
from nyaascraper import SITE

client.site = SITE.FUN
```

## Searching Torrents

### Search with Term

```py
from nyaascraper.models import SearchResult

result: SearchResult = await client.search(term="...")
print(result)

for torrent in result.torrents:
    print(torrent)
```

### Search by Username

```py
result = await client.search(username="...")
print(result)
```

### Search with Quality Filter

```py
from nyaascraper import QualityFilter

# No Filter. (Default)
result = await client.search(quality_filter=QualityFilter.NO_FILTER)
print(result)

# Trusted only.
result = await client.search(quality_filter=QualityFilter.TRUSTED_ONLY)
print(result)

# No Remakes.
result = await client.search(quality_filter=QualityFilter.NO_REMAKES)
print(result)
```

### Search with Category

```py
from nyaascraper.enums import FunCategory, FapCategory

# Work-safe category.
result = await client.search(category=FunCategory.ANIME)
print(result)

# Work-safe subcategory search.
result = await client.search(category=FunCategory.ANIME_ENGLISH_TRANSLATED)
print(result)

# Non-work-safe category.
result = await client.search(category=FapCategory.ART)
print(result)

# Non-work-safe subcategory search.
result = await client.search(category=FapCategory.ART_MANGA)
print(result)
```

### Search with Sorting

```py
from nyaascraper.enums import SortBy, SortOrder

# Sort by comments.
result = await client.search(sort_by=SortBy.COMMENTS)
print(result)

# Sort by size.
result = await client.search(sort_by=SortBy.SIZE)
print(result)

# Sort by date.
result = await client.search(sort_by=SortBy.DATE)
print(result)

# Sort by seeders.
result = await client.search(sort_by=SortBy.SEEDERS)
print(result)

# Sort by leechers.
result = await client.search(sort_by=SortBy.LEECHERS)
print(result)

# Sort by downloads.
result = await client.search(sort_by=SortBy.DOWNLOADS)
print(result)

# Sort order: Ascending.
result = await client.search(sort_order=SortOrder.ASCENDING)
print(result)

# Sort order: Descending.
result = await client.search(sort_order=SortOrder.DESCENDING)
print(result)
```

### Search by Page

```py
result = await client.search(page=2)
print(result)
```

## Getting Torrent Information

```py
from nyaascraper.models import TorrentInfo

result = await client.search()

# Select View-ID of the first torrent from the search result.
view_id: int = result.torrents[0].view_id

torrent_info: TorrentInfo = await client.get_torrent_info(view_id)
print(torrent_info)
```

## RSS Feed

### Initializing Client with Site

By default, the site is nyaa.si (work-safe site).

```py
from nyaascraper import NyaaRSSClient, SITE

# Work-safe site. (Default)
client = NyaaRSSClient(SITE.FUN)

# Non-work-safe site.
client = NyaaRSSClient(SITE.FAP)
```

### Changing Site

Changing the site of the client dynamically.

```py
from nyaascraper import SITE

client.site = SITE.FUN
```

### Get RSS feed

```py
from nyaascraper.models import NyaaRSSFeed

feed: NyaaRSSFeed = await client.get_feed()

print("Title:", feed.title)
print("Description:", feed.description)

for torrent in feed.torrents:
    print(torrent)
```

### Get RSS Feed with Magnet Links Only
```
feed = await client.get_feed(use_magnets=True)
```

# License

© 2023-2024 Zrekryu. Licensed under MIT License. See the LICENSE file for details.