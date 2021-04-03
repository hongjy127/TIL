# 아두이노랑 연결할 때는 client
# send, receive - 스레드
import bluetooth
import threading
import json

serverMACAddress = '00:20:04:32:5F:15'  # 아두이노가 서버
port = 1

def receive_thread(s):
    reader = s.makefile('rb')   # socket -> file
    reader.readline()           # 첫번째 데이터 버리기(통신 초기에 문제)
    while True:
        data = reader.readline().rstrip()
        # json 역직렬화
        command = json.loads(data)
        print("Received: %s" % command)
        if command["target"] == "servo": # 서보모터 제어
            pass    
        else:                           # 카메라 제어
            pass

        # if data == "q":
        #     break

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))

t = threading.Thread(target=receive_thread, args=(s,))
t.daemon = True     # 메인 스레드가 종료 시 같이 종료
t.start()           # 스레드 기동

while 1:
    text = input('입력')
    if text == "quit":
        break
    s.send(text)

s.close()