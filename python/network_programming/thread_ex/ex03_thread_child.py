import threading, requests, time

class HtmlGetter(threading.Thread):
    def __init__(self,url):
        # 다중상속이면 이런 이름사용
        threading.Thread.__init__(self)
        # super().__init__()
        self.url = url

    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), resp.text)

t = HtmlGetter('https://google.com')
t.start()

print("### End ###")