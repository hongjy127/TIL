import RPi.GPIO as GPIO
import time

servo_pin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

servo = GPIO.PWM(servo_pin, 50) # 주파수는 정해져있음
servo.start(0)

# (10/180) * angle + 2.5
try:
    while True:
        servo.ChangeDutyCycle(7.5)
        time.sleep(1)
        # servo.ChangeDutyCycle(12.5)
        servo.ChangeDutyCycle(12)
        time.sleep(1)
        servo.ChangeDutyCycle(2.5)
        time.sleep(1)

finally:
    servo.stop()
    GPIO.cleanup()