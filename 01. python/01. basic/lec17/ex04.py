# 데코레이터
# 일급시민
# 함수를 리턴(지역함수)

def calcsum(n):
    def add(a,b):
        return a+b

    total = 0
    for i in range(n+1):
        total = add(total,i)

    return total

print(f"~10 = {calcsum(10)}")