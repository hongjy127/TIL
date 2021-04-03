from django.shortcuts import render
from django.http import JsonResponse
from gpiozero import LED, Servo, AngularServo
import pigpio

led1 = LED(21)
SERVO = 18
# servo = AngularServo(SERVO, min_angle=-90, max_angle=90, min_pulse_width=0.0004, max_pulse_width=0.0024)
# servo.value = 0
pi = pigpio.pi() 
pi.set_servo_pulsewidth(SERVO, 1500)    # 초기 90도

def ledcontrol(request):
    # target = request.GET["target"]    # 키가 없으면 예외 발생
    target = request.GET.get("target")  # 키가 없으면 None 리턴
    value = request.GET.get("value", "off") # 키가 없으면 2번째 인자 리턴
    
    if target == "1":
        if value == "on":
            led1.on()
        elif value == "off":
            led1.off()

    result = {
        "result": "OK",
        "target": target,
        "value": value
    }

    return JsonResponse(result)

def servocontrol(request):
    target = request.GET.get("target")
    value = int(request.GET.get("value", "0"))
    
    if target == "1":   # servo 모터 조정
        # servo.value = value
        pulse_width = 500 + 11.11*(value+90)
        # print(value, pulse_width)
        pi.set_servo_pulsewidth(SERVO, pulse_width)
            
    result = {
        "result": "OK",
        "target": target,
        "value": str(value)
    }

    return JsonResponse(result)