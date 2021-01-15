from threading import Thread
import requests # pip install request
import time

def getHtml(url):
    resp = requests.get(url)
    with open('./profileImage.png','wb') as f:
        f.write(resp.content)

url = 'https://blogpfthumb-phinf.pstatic.net/MjAyMDEyMDVfMjcw/MDAxNjA3MTU3NDk3Nzg2.LsSaZQf1NKD7jslPVZPDNBVb0GnRsUSoN7M7-xClKcgg.B2kjHax3ptQMOPK05B7qq4Sf2YoH8f6A37UxQbixPAwg.PNG.hongjy127/profileImage.png'
t1 = Thread(target=getHtml, args=(url,))
t1.start()

# url이 list에 담겨있다면 (작업간의 연동할 것이 없음)
# url_list = [...]

# for url in url_list:
#     t1 = Thread(target=getHtml, args=(url,))
#     t1.start()



