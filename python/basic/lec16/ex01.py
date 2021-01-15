import m1
# module이 import 될 때 print(__name__)이 실행됨

if __name__ == "__main__":
    print(m1.calcsum(10))


print('ex01.py', __name__)  # __main__