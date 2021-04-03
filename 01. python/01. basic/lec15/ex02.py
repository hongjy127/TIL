class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # self.gender = None

    def intro(self):
        # print(f"{self.age}살 {self.name}입니다.")
        print(f"{self.age}살 {self.name} ({self.gender})입니다.")
        # AttributeError: 'Human' object has no attribute 'gender'
        # -> 없는 멤버를 접근함.

    def change(self,gender):
        self.gender = gender  # 권장하지 않음, 생성자에서 주는 것이 좋음.


kim = Human("김상형", 29)
print(kim.name)
kim.gender = '남'  # 멤버변수는 언제든지 추가 가능(class 밖에서)
kim.intro()

lee = Human("이승우", 45)
lee.change('남')  # class 안에서도 추가 가능
lee.intro()

del kim.name
kim.intro()