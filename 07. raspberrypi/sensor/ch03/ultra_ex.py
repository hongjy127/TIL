import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 19
ECHO = 26
print("Distance measuement in progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting for sensor t settle")
time.sleep(2)

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.000001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            start = time.time()
        while GPIO.input(ECHO)==1:
            stop = time.time()

        check_time = stop - start
        distance = check_time * 34300 / 2
        print("Distance: %.3f cm" %distance)
        time.sleep(0.4)

except KeyboardInterrupt:
    print("Measurement stopped by User")

finally:
    GPIO.cleanup()