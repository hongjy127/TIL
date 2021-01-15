class Human:
    def __init__(self):
        self.name = '홍길동'

    def info(self):
        print(self.name)
    
def test3(func):
    func()

hong = Human()  # 생성자함수 호출
test3(hong.info)

# hong 인스턴스의 메서드  

hong = Human    # 실제 Human class가 정의되어있는 곳의 참조
hong().info
# hong.info()