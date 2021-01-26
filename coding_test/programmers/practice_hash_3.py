# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    dic = {}
    for cloth, key in clothes:
        if key in dic.keys():
            dic[key].append(cloth)
        else:
            dic[key] = [cloth]
    for clothes in dic.values():
        answer *= len(clothes)+1
    return answer-1

# 이건 좀 더 느림
# def solution(clothes):
#     answer = 1
#     dic = {}
#     for cloth, key in clothes:
#         if key in dic.keys():
#             dic[key] += 1
#         else:
#             dic[key] = 1
#         print(dic)
#     for num_clothes in dic.values():
#         print(num_clothes)
#         answer *= num_clothes+1
#     return answer-1

clothes1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(clothes1))
print(solution(clothes2))