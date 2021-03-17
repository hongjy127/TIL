from audioapi import *

with open('heykakao.wav', 'rb') as fp:
    audio = fp.read()

ret, data = stt(audio)

if ret:
    print(data)
else:   # 실패
    print(f'인식 실패 {data}')