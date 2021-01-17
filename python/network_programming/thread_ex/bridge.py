from threading import Lock

class Bridge:
    def __init__(self):
        self.counter = 0
        self.name = "아무개"
        self.address = "모름"
        self.lock = Lock()

    def across(self, name, address):
        self.lock.acquire() # Lock의 상태가 바뀔때까지 sleep
        # === Critical Section(임계영역) ===
        # 어디가 CS인지 잘 확인
        self.counter += 1
        self.name = name
        self.address = address
        self.check()
        # === Critical Section(임계영역) ===
        self.lock.release()

    def toString(self):
        return f"이름:{self.name}, 출신:{self.address}, 도전횟수:{self.counter}"

    def check(self):
        if self.name[0] != self.address[0]:
            print(f"문제 발생!!!! {self.toString()}")

