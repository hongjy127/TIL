# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

# 모든 조합을 사용할 경우 O(100,000!)
# 숫자를 최고자리부터 비교 -> 큰게 제일 앞에 오도록 정렬

def solution(numbers):
    numbers_str = list(map(str, numbers))
    # 원소는 0 이상 1000이하 -> *4로 비교
    numbers_str.sort(key = lambda x:x*4, reverse=True)
    # key=lambda x: (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)])
    # 이렇게 하는 방법도 있다 -> n%len(x)가 자리수를 최고자리부터 반환하다가 없는 경우에 처음으로 돌아와서 다시 비교
    answer = ''.join(numbers_str)
    return answer if int(answer) != 0 else "0"

# test case
# numbers = [0,0,0,0], return = '0' 인 경우
# if int(answer) != 0 else "0" 이 문구가 꼭 필요
# 이걸 생각한 사람은 정말 대단