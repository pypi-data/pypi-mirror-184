from pymongo import MongoClient
from F.LOG import Log

s = " "
Log = Log(f"DBClient")

"""
    -> THE MASTER BASE CLASS
        - The Database Instance Itself.
    -> Does not need a collection to be initiated.
    -> Other Classes inherent this object.
"""

BASE_MONGO_URI = lambda mongo_ip, mongo_port: f"mongodb://{mongo_ip}:{mongo_port}"
BASE_MONGO_AUTH_URI = lambda mongo_ip, mongo_port, user, pw: f"mongodb://{user}:{pw}@{mongo_ip}:{mongo_port}"

class DBClient:
    client_connection_status = False
    client: MongoClient = None

    def __init__(self, dbclient=None):
        if dbclient:
            Log.i("Setting Client Object.")
            self.client = dbclient.client

    # -> !!MAIN CONSTRUCTOR!! <-
    def connect(self, ip, port, username=None, password=None):
        Log.i(f"DBClient: HOST=[ {ip}:{port} ]")
        url = BASE_MONGO_URI(ip, port)
        if username:
            url = BASE_MONGO_AUTH_URI(ip, port, username, password)
        try:
            Log.i(f"Initiating MongoDB: URI={url}")
            self.client = MongoClient(host=url, connectTimeoutMS=10000)
            self.is_connected()
            return self
        except Exception as e:
            Log.e(f"Unable to initiate MongoDB: URI={url}", error=e)
            return None
    def is_connected(self) -> bool:
        try:
            info = self.client.server_info()
            if info:
                Log.i("MongoDB is Up.")
                self.client_connection_status = True
                return True
        except Exception as e:
            Log.e("MongoDB is Down.", error=e)
            self.client_connection_status = False
            return False
        return False


if __name__ == '__main__':
    client = DBClient()
    client.connect("192.168.1.180", 27017)
    print(client)