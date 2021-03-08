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

try:
    # 브로커 연결
    client.connect("localhost")
    client.loop_start() # 새로운 스레드(데몬 스레드-메인 종료시 같이 종료)를 실행 - 메세지를 처리
    while True:
        ans = input('밝기: ')
        if ans == 'q':
            break
        value = int(ans)
        publish('test/led', 'led', value)
except Exception as err:
    print('에러 : %s'%err)
