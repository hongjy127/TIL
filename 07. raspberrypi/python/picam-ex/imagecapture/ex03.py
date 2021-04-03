from picamera import PiCamera
from time import sleep
from vutil import *

with PiCamera() as camera:
    camera.vflip = True
    camera.resolution = get_resolution()

    camera.start_preview()
    for i in range(5):
        sleep(5)
        camera.capture(f'./image_{i}.jpg')
    
    camera.stop_preview()