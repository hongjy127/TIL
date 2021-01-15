import paho.mqtt.client as mqtt

# 1. MQTT 클라이언트 객체 인스턴스화
client = mqtt.Client()

try:
    # 2. 브로커 연결
    client.connect("localhost")
    
    ### 토픽메세지
    # 3. 토픽 메세지 발행
    client.publish("iot/greeting", "Hello World!")
    client.loop(2)
except Exception as e:
    print(f"에러 {e}")