import sys
import pika
import app_config
from adstxt.spiders.adstxtparser.parsers.helper import HelperFunctions

hlpObj = HelperFunctions()
message = sys.argv[1]
credentials = pika.PlainCredentials(app_config.rabbitmq_username, app_config.rabbitmq_password)
parameters = pika.ConnectionParameters("localhost",
                                        app_config.rabbitmq_port,
                                        app_config.rabbitmq_vhost,
                                        credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue = "zip_ads_txt_dir", durable = True)

# print(" [x] Sending task message {}".format(message))
hlpObj.py_logger(" [x] Sending task message {}".format(message), name="publisher")
channel.basic_publish(exchange = "",
                    routing_key = "zip_ads_txt_dir",
                    body = message,
                    # This will make messages persistent
                    properties = pika.BasicProperties(delivery_mode = 2))
# print(" [x] Sent {}".format(message))
hlpObj.py_logger(" [x] Sent {}".format(message), name="publisher")
connection.close()
