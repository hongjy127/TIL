class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f'{self.age}살 {self.name}입니다')

class Player:
    def __init__(self, gender):
        self.gender = gender
        super().__init__()

class Student(Human):
    def __init__(self, name, age, stunum):
        super().__init__(name, age)
        # Human.__init__(self,name,age)
        self.stunum = stunum

    # def intro(self):
    #     #super().intro()
    #     print(f'학번: {self.stunum}')

    def study(self):
        print('하늘천 따지 검을 현 누를 황')

# 다중상속(부모가 여러개) - 권장하지는 않으나 쓰임
class Student(Human,Player):
    def __init__(self, name, age, gender, stunum):
        # super().__init__(name, age)
        Human.__init__(self,name,age)
        Player.__init__(self,gender)
        self.stunum = stunum

    # def intro(self):
    #     #super().intro()
    #     print(f'학번: {self.stunum}')

    def study(self):
        print('하늘천 따지 검을 현 누를 황')

# hong = Human('홍정연', 28)
# hong.intro()

hong = Student('홍정연', 28, 2015020064)
hong.intro()
hong.study()


