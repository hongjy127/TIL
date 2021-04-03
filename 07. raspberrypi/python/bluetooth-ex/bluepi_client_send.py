# 페어링 된 상태에서 실행
import bluetooth

serverMACAddress = '00:20:04:32:5F:15'  # 아두이노가 서버
port = 1

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))

while 1:
    text = input('입력')
    if text == "quit":
        break
    s.send(text)

s.close()