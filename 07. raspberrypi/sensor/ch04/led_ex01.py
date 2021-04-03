from gpiozero import LED
from time import sleep

red = LED(21)
# 스레드 운영도 객체에서 해줌

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)

