import json

dic = {
    "file_name" : "C:/temp/CNN_0.ckpt.meta",
    "file_size" : 400500
}

# 사전(파이썬 자료구조 객체) --> 문자열로 표현
msg = json.dumps(dic)   # 문자열 / json.dump(): 파일
print(type(msg),msg)    # 문자열 msg를 전송

# 문자열 msg를 수신
# 문자열 --> 사전 객체로 복원
dic2 = json.loads(msg)   # json.load()
print(type(dic2),dic2)

li = [dic, dic]

msg = json.dumps(li)
print(type(msg),msg)

li2 = json.loads(msg)   # json.load()
print(type(li2),li2)