# Models needed for this app.

## Schedule a crawl (django_adstxt_crawls)

- id from auth_table
- crawl_id (uuid)
- timestamp
- status (1|0)
- file_path

## Downloaded files (django_adstxt_downloads)

- crawl_id (uuid, ForeignKey)
- timestamp
- Download_location_link
