import sys
import shutil
import pika

import app_config

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
    print(" [x] Received zip task with jobId = {}".format(body.decode()))
    compDirName = app_config.user_download_path + body.decode()
    rootDirPath = app_config.crawler_download_path + body.decode()
    shutil.make_archive(compDirName, "zip", rootDirPath)
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count = 1)
channel.basic_consume(queue = "zip_ads_txt_dir", on_message_callback = callback)
print(" [*] Waiting for messages.")
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("Pressed Ctrl+c exiting now.")
    sys.exit(1)
