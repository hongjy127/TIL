# LED와 PIR 센서를 연결
# 움직임이 감지되면 동영상 녹화 시작, 서버로 이미지 전송
# 움직임이 없어지면 동영상 녹화 중지, 이미지 전송 중지
# 파일명은 날짜_녹화시작시간.h264
# 화면 출력은 없음

from gpiozero import LED, MotionSensor
from signal import pause
from time import sleep
import picamera
import datetime
import socket
import struct
import threading
import io
import net

HOST = '172.30.1.35'
PORT = 5000

motion = MotionSensor(20)
led = LED(21)

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.vflip = True

def video_streaming():
    with socket.socket() as s:
        s.connect((HOST, PORT))
        writer = s.makefile('wb')
        reader = s.makefile('rb')
        stream = io.BytesIO()

        for _ in camera.capture_continuous(stream, 'jpeg', use_video_port = True):
                image = stream.getvalue()   # 스트림에서 byte 배열 얻기
                net.send(writer, image)
                result = net.receive(reader)[0]

                # 다음 캡쳐를 위해 스트림을 리셋 - 파일의 기존 내용을 버림
                stream.seek(0)      # 파일 쓰기 위치를 맨 앞으로 이동
                stream.truncate()   # 기존 내용을 버리는 작업

                if not motion.value:
                    writer.write(struct.pack('<L', 0))  # 스트리밍 끝
                    writer.flush()
                    break

def start_record():
    led.on()
    now = datetime.datetime.now()
    fname = now.strftime("%T%m%d_%H%M") + ".h264"
    camera.start_recording(fname)
    threading.Thread(target=video_streaming).start()

def stop_record():
    led.off()
    camera.stop_recording()

motion.when_motion = start_record
motion.when_no_motion = stop_record

pause()

# 응용
# PIR 대신 초음파 센서운영
# 물체가 일정 거리 안으로 진입시 운영
# 물체가 차량인 경우
# 이미지에서 차량의 번호판 영역 추룰(OpenCV로 가능 - 인터넷에 소스 많음)

# AI를 이용하여 번호판 번호 해석
# 차량 번호에 따라 출입 통제 등