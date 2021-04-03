# 페어링 된 상태에서 실행
import bluetooth

serverMACAddress = '00:20:04:32:5F:15'  # 아두이노가 서버
port = 1

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))

while 1:
    data = s.recv(1024)
    print("Received: %s" % data)
    if data == "q":
        print("Quit")
        break

s.close()