from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

process.crawl('adstxt', fileName="/home/kaustubh/Workspace/adstxt-crawler-ui/docs/sample/sample4")
process.start()
