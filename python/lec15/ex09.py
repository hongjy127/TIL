class Car:
    count = 0

    def __init__(self, name):
        self.name = name
        Car.count += 1

    @classmethod
    def outcount(cls):
        print(cls.count)


pride = Car('Pride')
korando = Car('Korando')
Car.outcount()
