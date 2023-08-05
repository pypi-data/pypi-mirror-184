from F import LIST, DICT
from pymongo.database import Database
# from FM.DBDatabase import DBDatabase
from FM.QueryHelper import QHelpers
from F.LOG import Log

s = " "
Log = Log(f"DBCollection")

"""
    -> THE MASTER BASE CLASS
        - The Database Instance Itself.
    -> Does not need a collection to be initiated.
    -> Other Classes inherent this object.
"""

class DBCollection(QHelpers):
    core_collection = None

    def __init__(self, collection):
        self.core_collection = collection

    def get_document_count(self):
        return self.core_collection.estimated_document_count()

    def base_aggregate(self, pipeline, allowDiskUse=True):
        if not self.core_collection:
            return False
        results = self.core_collection.aggregate(pipeline, allowDiskUse=allowDiskUse)
        results = self.to_list(results)
        if results and len(results) > 0:
            return results
        return False

    def base_query(self, kwargs, page=0, limit=100):
        if not self.core_collection:
            return False
        if limit and page >= 0:
            results = self.core_collection.find(kwargs).skip(page).limit(limit)
        else:
            results = self.core_collection.find(kwargs)
        results = self.to_list(results)
        if results and len(results) > 0:
            return results
        return False

    def base_query_unlimited(self, kwargs):
        if not self.core_collection:
            return False
        results = self.core_collection.find(kwargs)
        results = self.to_list(results)
        if results and len(results) > 0:
            return results
        return False
    def get_field_names(self):
        fields = []
        oneResult = self.base_query({}, 0, 1)
        oneDoc = LIST.get(0, oneResult)
        for doc in oneDoc:
            fields.append(doc)
        return fields

    def record_exists(self, recordIn) -> bool:
        temp = self.base_query(recordIn)
        if temp:
            Log.w("Object Exists in Database Already. Skipping...")
            return True
        Log.v("Object Does Not Exist in Database.")
        return False

    def record_exists_by_field_match(self, field, value) -> bool:
        temp = self.base_query({field:value})
        if temp:
            Log.w("Object Exists in Database Already. Skipping...")
            return True
        Log.v("Object Does Not Exist in Database.")
        return False

    def add_records(self, list_of_objects):
        """ Each Object should be JSON Format """
        list_of_objects = LIST.flatten(list_of_objects)
        Log.w(f"Beginning Add Records Queue. COUNT=[ {len(list_of_objects)} ]")
        for objectItem in list_of_objects:
            record_exists = self.record_exists(objectItem)
            if not record_exists:
                self.insert_record(objectItem)
        Log.w(f"Finished Add Records Queue.")

    def add_records_field_match(self, list_of_objects, fieldName, ignoreExists=False):
        """ Each Object should be JSON Format """
        list_of_objects = LIST.flatten(list_of_objects)
        Log.w(f"Beginning Add Records Queue. COUNT=[ {len(list_of_objects)} ]")
        for objectItem in list_of_objects:
            fieldValue = DICT.get(fieldName, objectItem, default=False)
            if ignoreExists:
                self.insert_record(objectItem)
                continue
            record_exists = self.record_exists_by_field_match(fieldName, fieldValue)
            if not record_exists:
                self.insert_record(objectItem)
        Log.w(f"Finished Add Records Queue.")

    def insert_record(self, kwargs):
        try:
            # time.sleep(1)
            self.core_collection.insert_one(kwargs)
            Log.s(f"NEW Record created in DB=[ {self.core_collection} ]")
            return True
        except Exception as e:
            Log.e(f"Failed to save record in DB=[ {self.core_collection} ]", error=e)
            return False

    def update_record(self, findQuery: dict, updateQuery: dict, upsert=True):
        try:
            # time.sleep(1)
            self.core_collection.update_one( findQuery, { "$set": updateQuery }, upsert=upsert )
            Log.s(f"UPDATED Record in DB=[ {self.core_collection} ]")
            return True
        except Exception as e:
            Log.e(f"Failed to save record in DB=[ {self.core_collection} ]", error=e)
            return False

    def replace_record(self, findQuery: dict, updateQuery: dict, upsert=True):
        try:
            # time.sleep(1)
            self.core_collection.replace_one( findQuery, { "$set": updateQuery }, upsert=upsert )
            Log.s(f"REPLACED Record in DB=[ {self.core_collection} ]")
            return True
        except Exception as e:
            Log.e(f"Failed to save record in DB=[ {self.core_collection} ]", error=e)
            return False

    def update_many_records(self, findQuery: dict, updateQueries: list, upsert=True):
        try:
            # time.sleep(1)
            self.core_collection.update_many( findQuery, updateQueries, upsert=upsert )
            Log.s(f"UPDATED Record in DB=[ {self.core_collection} ]")
            return True
        except Exception as e:
            Log.e(f"Failed to save record in DB=[ {self.core_collection} ]", error=e)
            return False

    def remove_record(self, kwargs):
        try:
            # time.sleep(1)
            self.core_collection.delete_one(kwargs)
            Log.s(f"Removed Record in DB=[ {self.core_collection} ]")
            return True
        except Exception as e:
            Log.e(f"Failed to remove record in DB=[ {self.core_collection} ]", error=e)
            return False
