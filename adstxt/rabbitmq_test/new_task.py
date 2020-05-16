import sys
import pika

message = " ".join(sys.argv[1:]) or "Hello World"
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
