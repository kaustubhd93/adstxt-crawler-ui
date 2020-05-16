import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host = "localhost"))
channel = connection.channel()

channel.exchange_declare(exchange = "logs", exchange_type = "fanout")
result = channel.queue_declare(queue = "", exclusive = True)
queue_name = result.method.queue

channel.queue_bind(exchange = "logs", queue = queue_name)

def callback(ch, method, properties, body):
    print(" [x] {}".format(body))

channel.basic_consume(queue = queue_name, on_message_callback = callback, auto_ack = True)

try:
    print(" [*] Waiting for logs. To exit press CTRL+C")
    channel.start_consuming()
except KeyboardInterrupt:
    print("Pressed Ctrl+c exiting now.")
    sys.exit(1)
