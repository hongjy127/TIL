nums = [11,22,33]

# for문의 내부 코드, 실제로 사용하지는 않음
it = iter(nums)
while True:
    try:
        num = next(it)
    except StopIteration:
        break
    print(num)