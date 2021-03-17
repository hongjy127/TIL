from gpiozero import Button, LED
from signal import pause

button = Button(20)
led = LED(21)

# button의 상태를 led와 동일하게 하겠다
led.source = button.values

pause()