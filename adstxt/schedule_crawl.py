import sys
import pika

message = sys.argv[1]
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue = "task_queue", durable = True)

channel.basic_publish(exchange = "",
                    routing_key = "task_queue",
                    body = message,
                    # This will make messages persistent
                    properties = pika.BasicProperties(delivery_mode = 2))
print(" [x] Sent {}".format(message))
connection.close()
