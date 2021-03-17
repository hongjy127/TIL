from pymongo import MongoClient
from datetime import datetime
import random

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

rows = sensors_col.find().sort("value")
# rows = sensors_col.find().sort("value", -1)

for x in  rows:
    print(x)