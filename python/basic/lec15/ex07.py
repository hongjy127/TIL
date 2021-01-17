import random
import time

class TempSensor:
    def __init__(self):
        self.value = 5

    # -1.0 ~ 1.0 random 변수 생성
    def read_temp(self):
        self.value += random.uniform(-1.0,1.0)
        return self.value


class Boiler:
    def on(self):
        print('보일러가 켜집니다')


class Controller:
    def __init__(self, base, func):  # 주입: injection
        self.base = base
        # self.bolier = Boiler()
        self.func = func
        self.__temp = 10
    
    @property
    def temp(self):
        return self.__temp

    @temp.setter
    def temp(self, value):
        if value < self.base:
            # self.bolier.on()
            self.func()
        self.__temp = value

tsensor = TempSensor()
bolier = Boiler()

def light_on():
    print('전등을 켭니다.')

# controller = Controller(5, bolier.on)
controller = Controller(5, light_on)

# 1초 간격으로 온도 측정
while True:
    controller.temp = tsensor.read_temp()
    print(controller.temp)
    time.sleep(1)
