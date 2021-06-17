from redis import Redis
from adstxt.spiders.adstxtparser.parsers.helper import HelperFunctions

class RedisTasks:
    def __init__(self):
        self.connection = Redis("localhost")
        self.hlpObj = HelperFunctions()

    def update_job_status(self, jobId, status):
        try:
            statusUpdate = {"status" : status}
            self.connection.hmset(name = jobId + ":jobdetails",
                                mapping = statusUpdate)
            return True
        except Exception as e:
            # print("Something went wrong here : {}".format(str(e)))
            self.hlpObj.py_logger("Something went wrong here : {}".format(str(e)), name="publisher")
            return False

    def register_job(self, jobId, crawlerDownloadPath, userDownloadPath ,status = "pending"):
        try:
            jobDetails = {"crawlerDownloadPath" : crawlerDownloadPath,
                            "userDownloadPath": userDownloadPath,
                            "status" : status}
            self.connection.hmset(name = jobId + ":jobdetails",
                                mapping = jobDetails)
            return True
        except Exception as e:
            # print("Something went wrong here : {}".format(str(e)))
            self.hlpObj.py_logger("Something went wrong here : {}".format(str(e)), name="publisher")
            return False
