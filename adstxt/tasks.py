from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from celery import Celery

app = Celery("tasks", broker = "amqp://adstxt:rockoholic@localhost:5672/adstxtcrawler")

@app.task
def crawl_this(fileInfo):
    process = CrawlerProcess(get_project_settings())
    process.crawl('adstxt', fileInfo=fileInfo)
    process.start(stop_after_crawl=False)
    # return None
