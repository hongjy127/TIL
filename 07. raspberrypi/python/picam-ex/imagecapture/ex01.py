from picamera import PiCamera
from time import sleep

camera = PiCamera()

# 180도 회전하기
camera.rotation = 180
# camera.vflip=True

camera.start_preview()
# camera.start_preview(alpha=200)
sleep(10)
camera.stop_preview()