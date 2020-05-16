import sys
import subprocess
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host = "localhost",
                                                            heartbeat=900,
                                                            blocked_connection_timeout = 600))
channel = connection.channel()
channel.queue_declare(queue = "task_queue", durable = True)

def shell_me(cmd):
    bash = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = bash.communicate()
    returnCode = bash.returncode
    if returnCode == 0:
        return str(stdout)
    else:
        return str(stderr)

def callback(ch, method, properties, body):
    print(" [x] Received task with jobId:filePath = {}".format(body.decode()))
    shell_me("/bin/bash crawl.sh {}".format(body.decode()))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count = 1)
channel.basic_consume(queue = "task_queue", on_message_callback = callback)
print(" [*] Waiting for messages.")
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("Pressed Ctrl+c exiting now.")
    sys.exit(1)
