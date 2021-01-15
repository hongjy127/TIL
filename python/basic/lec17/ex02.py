class Seq:
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __eq__(self, value):
        return self.data == value.data

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 2
        if self.index >= len(self.data):
            self.index = -2
            raise StopIteration

        return self.data[self.index:self.index+2]

solarterm1 = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
solarterm2 = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")

for k in solarterm1:
    print(k, end=',')

print()
for k in solarterm2:
    print(k, end=',')

print()
print(solarterm1 == solarterm1)
print(dir(solarterm1))

# 개발자가 추가한 멤버변수만 나옴
print(solarterm1.__dict__)

# print(dir(solarterm1))
print(solarterm1.__dir__)