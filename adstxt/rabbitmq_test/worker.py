import sys
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host = "localhost"))
channel = connection.channel()
channel.queue_declare(queue = "task_queue", durable = True)

def callback(ch, method, properties, body):
    print(" [x] Received : {}".format(body))
    time.sleep(body.count(b"."))
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
