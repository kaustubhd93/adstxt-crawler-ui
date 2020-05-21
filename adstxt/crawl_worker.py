import time
import sys
import subprocess
import pika
import app_config
from redis_helper import RedisTasks

redisConn = RedisTasks()
credentials = pika.PlainCredentials(app_config.rabbitmq_username, app_config.rabbitmq_password)
parameters = pika.ConnectionParameters("localhost",
                                        app_config.rabbitmq_port,
                                        app_config.rabbitmq_vhost,
                                        credentials,
                                        heartbeat = 900,
                                        blocked_connection_timeout = 600)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue = "crawl_ads_txt", durable = True)

def shell_me(cmd):
    bash = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = bash.communicate()
    returnCode = bash.returncode
    if returnCode == 0:
        return str(stdout)
    else:
        return str(stderr)

def callback(ch, method, properties, body):
    content = body.decode()
    jobId = content.split(":")[0]
    print(" [x] Received task with jobId:filePath = {}".format(body.decode()))
    redisConn.update_job_status(jobId, "running")
    shell_me("/bin/bash crawl.sh {}".format(body.decode()))
    print(" [x] Done")
    # Acknowledgment for message received and processed.
    ch.basic_ack(delivery_tag = method.delivery_tag)

# For proper distribution of tasks
channel.basic_qos(prefetch_count = 1)
channel.basic_consume(queue = "crawl_ads_txt", on_message_callback = callback)
print(" [*] Waiting for messages.")
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("Pressed Ctrl+c exiting now.")
    sys.exit(1)
