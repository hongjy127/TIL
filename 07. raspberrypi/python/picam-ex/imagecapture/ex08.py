from picamera import PiCamera
from time import sleep
from vutil import *

camera = PiCamera(resolution = (320, 240), framerate=30)

camera.iso = 100
sleep(2)

camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = get_resolution

camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])