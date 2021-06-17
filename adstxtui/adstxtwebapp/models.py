import uuid
from django.db import models

# Create your models here.
class Crawls(models.Model):
    # user_id is actually from Django_auth table.
    user_id = models.IntegerField(default=0)
    crawl_id = models.UUIDField(default=uuid.uuid4, editable=False)
    scheduled_time = models.DateTimeField("scheduled_time")
    status = models.SmallIntegerField(default=0)
    file_path = models.CharField(max_length=200)

class Downloads(models.Model):
    crawl = models.ForeignKey("Crawls", on_delete=models.CASCADE)
    download_time = models.DateTimeField("scheduled_time")
    downloaded_file_link = models.CharField(max_length=200)
