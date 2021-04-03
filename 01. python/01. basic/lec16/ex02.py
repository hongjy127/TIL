import ex01
import m1
# ex01이 모듈이 됨 -> __name__이 모듈명

print('ex02.py', __name__)
print(m1.calcsum(20))

if __name__=='__main__':
    # 모듈인지 아닌지 판단하는 코드
    print(dir(m1))
    print(m1.__file__)
    pass