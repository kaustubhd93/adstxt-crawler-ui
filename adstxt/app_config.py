import os

currentDir = os.getcwd()
rabbitmq_username = "adstxt"
rabbitmq_password = "rockoholic"
rabbitmq_vhost = "adstxtcrawler"
rabbitmq_port = 5672
send_task_log_file = currentDir + "/rabbitmq_tasks/send_task.log"
receive_task_log_file = currentDir + "/rabbitmq_tasks/receive_task.log"
user_download_path = currentDir + "/userdownloads/"
crawler_download_path = currentDir + "/csv/"
