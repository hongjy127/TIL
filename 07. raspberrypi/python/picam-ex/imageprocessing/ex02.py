# LED와 PIR 센서를 연결
# 움직임이 감지되면 동영상 녹화 시작
# 움직임이 없어지면 동영상 녹화 중지
# 파일명은 날짜_녹화시작시간.h264
# 화면 출력은 없음
# 녹화 중일 때는 LED ON

import time
from signal import pause
from gpiozero import LED, MotionSensor
import picamera
import datetime

motion = MotionSensor(20)
led = LED(21)

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.vflip = True

def start_record():
    led.on()
    now = datetime.datetime.now()
    fname = now.strftime("%T%m%d_%H%M") + ".h264"
    print("motion")
    camera.start_recording(fname)

def stop_record():
    led.off()
    print("no motion")
    camera.stop_recording()

motion.when_motion = start_record
motion.when_no_motion = stop_record

pause()