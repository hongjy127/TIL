from gpiozero import Servo
from time import sleep

myGPIO = 21
servo = Servo(myGPIO,
            min_pulse_width = 0.0004, max_pulse_width = 0.0024)
# 센서마다 조금씩 다를 수 있음

while True:
    servo.value = 0
    print("mid")
    sleep(0.5)
    servo.value = -1
    print("min")
    sleep(1)
    servo.value = 0
    print("mid")
    sleep(0.5)
    servo.value = 1
    print("max")
    sleep(1)