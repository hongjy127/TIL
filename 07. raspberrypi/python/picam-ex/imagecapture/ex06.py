from picamera import PiCamera
from time import sleep
from vutil import *

with PiCamera() as camera:
    camera.resolution = get_resolution()

    filename = input('File Name?')

    camera.framerate = 15
    camera.start_preview()
    camera.start_recording(output = filename+'.h264')
    camera.wait_recording(5)
    camera.stop_recording()
    camera.stop_preview()