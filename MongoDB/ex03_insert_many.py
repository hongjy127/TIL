from pymongo import MongoClient
from datetime import datetime
import random

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

sensor_value = [
    {
        "topic" : "iot/home1/device1/temp",
        "value" : 24 + random.random(),
        "reg_date" : datetime.utcnow()
    },
    {
        "topic" : "iot/home1/device1/humi",
        "value" : 55 + random.random(),
        "reg_date" : datetime.utcnow()
    },
    {
        "topic" : "iot/home2/device1/temp",
        "value" : 24 + random.random(),
        "reg_date" : datetime.utcnow()
    },
    {
        "topic" : "iot/home2/device1/humi",
        "value" : 55 + random.random(),
        "reg_date" : datetime.utcnow()
    }
]

x = sensors_col.insert_many(sensor_value)
print(x.inserted_ids)