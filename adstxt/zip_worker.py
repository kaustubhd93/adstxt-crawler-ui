import os
import sys
import shutil
import pika
import app_config
from redis_helper import RedisTasks
from adstxt.spiders.adstxtparser.parsers.helper import HelperFunctions

hlpObj = HelperFunctions()
redisConn = RedisTasks()
prefix = "[ zipworkerpid " + str(os.getpid()) + " ]"
credentials = pika.PlainCredentials(app_config.rabbitmq_username, app_config.rabbitmq_password)
parameters = pika.ConnectionParameters("localhost",
                                        app_config.rabbitmq_port,
                                        app_config.rabbitmq_vhost,
                                        credentials,
                                        heartbeat = 900,
                                        blocked_connection_timeout = 600)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue = "zip_ads_txt_dir", durable = True)

def callback(ch, method, properties, body):
    jobId = body.decode()
    # print(" [x] Received zip task with jobId = {}".format(jobId))
    hlpObj.py_logger(prefix + " Received zip task with jobId = {}".format(jobId), name="worker")
    compDirName = app_config.user_download_path + jobId
    rootDirPath = app_config.crawler_download_path + jobId
    shutil.make_archive(compDirName, "zip", rootDirPath)
    # print(prefix + " Done zipping")
    hlpObj.py_logger(prefix + " Done zipping", name="worker")
    redisConn.update_job_status(jobId, "completed")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count = 1)
channel.basic_consume(queue = "zip_ads_txt_dir", on_message_callback = callback)
# print(" [*] Waiting for messages.")
hlpObj.py_logger(prefix + " Waiting for messages.", name="worker")
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("Pressed Ctrl+c exiting now.")
    sys.exit(1)
