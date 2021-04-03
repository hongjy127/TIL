from gpiozero import Button, LED
from signal import pause

button = Button(20)
led = LED(21)
count = 0

def say_hello():
    global count
    # count += 1
    # print("Hello!", count)
    print("Hello!")
    led.on()

def say_goodbye():
    print("Goodbye!")
    led.off()   

button.when_pressed = say_hello
button.when_released = say_goodbye
pause()