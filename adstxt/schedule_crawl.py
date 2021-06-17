import sys
import pika

import app_config
from redis_helper import RedisTasks
from adstxt.spiders.adstxtparser.parsers.helper import HelperFunctions

hlpObj = HelperFunctions()
redisConn = RedisTasks()
message = sys.argv[1]
credentials = pika.PlainCredentials(app_config.rabbitmq_username, app_config.rabbitmq_password)
parameters = pika.ConnectionParameters("localhost",
                                        app_config.rabbitmq_port,
                                        app_config.rabbitmq_vhost,
                                        credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue = "crawl_ads_txt", durable = True)

jobId = message.split(":")[0]
crawlerDownloadPath = app_config.crawler_download_path + jobId
userDownloadPath = app_config.user_download_path + jobId + ".zip"
# Registering Job in Redis.
if redisConn.register_job(jobId, crawlerDownloadPath, userDownloadPath):
    hlpObj.py_logger(" [x] Sending task message {}.".format(message), name="publisher")
    channel.basic_publish(exchange = "",
                        routing_key = "crawl_ads_txt",
                        body = message,
                        # This will make messages persistent
                        properties = pika.BasicProperties(delivery_mode = 2))
    hlpObj.py_logger(" [x] Sent {}".format(message), name="publisher")
else:
    hlpObj.py_logger("Something went wrong while registering new job with job id {}.".format(jobId), name="publisher")
connection.close()
