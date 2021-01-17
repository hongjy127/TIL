from threading import Thread
import requests # pip install request
import time

def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), resp.text)

t1 = Thread(target=getHtml, args=('https://naver.com',))
t1.start()
# 변수명이 같아도 됨(참조만 사라질 뿐 운영체제에 의해 메모리에 남아있음)
t1 = Thread(target=getHtml, args=('https://www.daum.com',))
t1.start()
# 스레드를 쓰면 동시에 진행

# 스레드를 안쓰는 경우 (시간이 오래 걸림)
# getHtml('https://www.daum.com')
# getHtml('https://naver.com')