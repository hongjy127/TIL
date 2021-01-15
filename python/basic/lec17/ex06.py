### 1
# 앞, 뒤에 다 가능
# def inner():
#     print("결과를 출력합니다")

# def outer(func):
#     print("-"*20)
#     func()
#     print("-"*20)

# def hello():
#     print("안녕하세요")

# outer(inner)
# outer(hello)


### 2
# inner를 실행하는 것처럼 보임
# def inner():
#     print("결과를 출력합니다")

# def outer(func):
#     def wrapper():
#         print("-"*20)
#         func()
#         print("-"*20)
#     return wrapper

# inner = outer(inner)
# inner()
# 복잡하니 이걸 대체

### 3

def outer(func):
    def wrapper():
        print("-"*20)
        func()
        print("-"*20)
    return wrapper

@outer
def inner():
    print("결과를 출력합니다")

inner()