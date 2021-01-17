# import threading
# 주로 이렇게 많이 씀
from threading import Thread

count = 2   # 운영할 스레드의 개수

def sum(low, high):
    global count
    total = 0
    for i in range(low, high):
        total += i
    print("Subthread", total)
    count -=1

t1 = Thread(target=sum, args=(1,100000))
t2 = Thread(target=sum, args=(100,10000000))
t1.start()
t2.start()

# 작업 스레드가 모두 종료된 후 메인스레드 실행
while count != 0:
    pass

print("main Thread")
# print된 결과로 메인, 작업 스레드 중 먼저 실행/종료된걸 알 수 있음

# 전역, Heap은 Process당 한개
# stack은 스레드(작업, 메인) 각각 한개씩