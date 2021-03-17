import RPi.GPIO as GPIO
import time

led_pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

p = GPIO.PWM(led_pin, 50)
p.start(0)  # 듀티비: 0

try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    p.stop()
    GPIO.cleanup()