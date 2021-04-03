# 사용자의 입력을 받아 LED의 on/off 제어
# value를 사용해서

from gpiozero import LED

red = LED(21)

while True:
    x = input("LED on(1)/off(0) : ")
    if x == "q":
        break
    
    red.value = int(x)  # @property, 값을 대입하면 동작이 일어남
