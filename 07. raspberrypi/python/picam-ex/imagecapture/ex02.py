from picamera import PiCamera
from time import sleep
from vutil import *

with PiCamera() as camera:
    camera.vflip = True
    camera.resolution = get_resolution()

    filename = input('File Name?')
    camera.start_preview()
    sleep(1)
    camera.stop_preview()
    camera.capture(filename + '.jpg')