from pymongo import MongoClient
from datetime import datetime

from mqtt_sub import subscribe

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")   # byte 데이터를 utf-8 문자열로 변환
    print(msg.topic + " " + str(msg.payload))

    sensor_value = {
        "topic": msg.topic,
        "value": float(str(msg.payload)),
        "reg_date": datetime.now()
    }

    sensors_col.insert_one(sensor_value)

# C:\Users\hongj\TIL\arduino\NODEMCU\ex07\app.ino(온,습도 publish 하는 코드)
# 실행하면 여기서 subscribe
subscribe("localhost", "user1/home/#", on_message)