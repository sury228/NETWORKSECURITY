import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger

class networkdataextraction:

    def __init__(self):
        try:
            pass

        except Exception as e:
            raise NetworkSecurityException(e, sys) 


    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def insert_records_to_mongodb(self,records,collection,database):
        try:
           self.records=records
           self.collection=collection
           self.database=database

           if not self.records:
               raise ValueError("No records to insert")

           client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
           self.mongo_client = client

           # get database and collection objects
           db_obj = self.mongo_client[self.database]
           coll_obj = db_obj[self.collection]

           coll_obj.insert_many(self.records)
           return len(self.records)

        except Exception as e:
           raise NetworkSecurityException(e, sys)



if __name__ == "__main__":
   FILE_PATH = "network_data/phisingData.csv"
   DATABASE = "suryansh"
   COLLECTION = "network_data"

   obj = networkdataextraction()
   records = obj.csv_to_json_converter(file_path=FILE_PATH)
   print(records)
   no_of_records = obj.insert_records_to_mongodb(records=records, collection=COLLECTION, database=DATABASE)
   print(no_of_records)


