# 일정 시간 지나면 동작을 안함.
import paho.mqtt.client as mqtt
import json

# MQTT 클라이언트 객체 인스턴스화
client = mqtt.Client()

def publish(topic, device, value):
    dic = {
        "device": device,
        "value": value
    }
    client.publish(topic, json.dumps(dic))
    client.loop(2)

try:
    # 브로커 연결
    client.connect("localhost")
    while True:
        ans = input('밝기: ')
        if ans == 'q':
            break
        value = int(ans)
        publish('test/led', 'led', value)
except Exception as err:
    print('에러 : %s'%err)
