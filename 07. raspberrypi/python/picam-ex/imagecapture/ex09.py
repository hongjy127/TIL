from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(2)

for filename in camera.capture_continuous('img{counter:03d}.jpg'):
    print('Cpatured %s' % filename)
    sleep(10)