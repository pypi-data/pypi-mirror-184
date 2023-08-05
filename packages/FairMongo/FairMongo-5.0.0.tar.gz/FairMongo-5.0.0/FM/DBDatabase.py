from pymongo.database import Database
from FM.DBClient import DBClient
from FM.DBCollection import DBCollection
from F.LOG import Log


Log = Log(f"DBDatabase")

"""
    -> THE MASTER BASE CLASS
        - The Database Instance Itself.
    -> Does not need a collection to be initiated.
"""

class DBDatabase(DBClient):
    db: Database = None
    db_bulk = bulk = None

    def database(self, databaseName, dbclient:DBClient=None):
        if dbclient:
            self.client = dbclient.client
        if self.is_connected():
            self.db = self.client.get_database(databaseName)
            return self
        return None

    def collection(self, collectionName):
        cc = self.db.get_collection(collectionName)
        return DBCollection(cc)


if __name__ == '__main__':
    # clientOne = DBClient().connect("192.168.1.180", 27017)
    dbone = DBDatabase().connect("192.168.1.180", 27017).database("research")
    results = dbone.collection("companies").get_field_names()
    print(results)
