import paho.mqtt.client as mqtt

### 변수화 해야하는거
# 브로커 접속 시도 결과 처리 콜백 함수
# 연결 했을 때 호출될, 함수명은 아무거나 해도 되지만 관례상 on_이벤트명, 매개변수는 생략 불가능
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    ### 토픽메세지
    if rc == 0:
        client.subscribe("iot/#")  # 연결 선공시 토픽 구독 신청
    else:
        print(f'연결 실패: {rc}')

### 어떻게 처리할지
# 관련 토픽 메세지 수신 콜백 함수
def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}")

# 1. MQTT 클라이언트 객체 인스턴스화
client = mqtt.Client()

# 2. 관련 이벤트에 대한 콜백 함수 등록
client.on_connect = on_connect
client.on_message = on_message

# on_connect는 호출하지 않았지만 알아서 실행됨
try:
    ### 브로커 주소
    # 3. 브로커 연결
    client.connect("localhost")

    # 4. 메세지 루프 - 이벤트 발생시 해당 콜백 함수 호출됨
    client.loop_forever()
    # client.loop_start()     # 데몬스레드
except Exception as e:
    print(f"에러 {e}")

# import time
# time.sleep(10)
# print('End')