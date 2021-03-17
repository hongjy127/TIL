import RPi.GPIO as GPIO
import time

buzzer_pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

Freq = [262, 294, 330, 349, 392, 440, 493, 523]
speed = 0.5

p = GPIO.PWM(buzzer_pin, 100)
p.start(10)

try:
    while 1:
        for fr in Freq:
            p.ChangeFrequency(fr)
            time.sleep(speed)

except KeyboardInterrupt:
    pass

finally:
    p.stop()
    GPIO.cleanup()