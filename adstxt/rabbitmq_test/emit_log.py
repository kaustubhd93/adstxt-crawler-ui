import sys
import pika

message = " ".join(sys.argv[1:])
message = "info: " + message
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange = "logs",
                        exchange_type = "fanout")

# Routing key is empty because exchange type is fanout.
# Every consumer will receive this message.
channel.basic_publish(exchange = "logs",
                    routing_key = "",
                    body = message)
print(" [x] Sent {}".format(message))
connection.close()
