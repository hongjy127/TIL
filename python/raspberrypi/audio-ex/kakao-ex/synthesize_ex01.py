# 사용할 음색 선정
# 무한 루프를 돌면서
# 사용자로부터 문자열 입력
# 입력 받은 문자열을 음성 합성으로 출력
# quit 입력시 프로그램 종료

import requests
import io
from pydub import AudioSegment
from pydub.playback import play

URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize" 
HEADERS = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK 4cf5f301c1c62029f447bb1326dea702"
}

while True:
    input_str = input("대화 입력: ")

    if input_str == 'quit': break
    xml = f'<speak><voice name="WOMAN_READ_CALM">{input_str}</voice></speak>'
    res = requests.post(URL, headers = HEADERS, data = xml.encode('utf-8'))

    if res.status_code == 200:
        sound = io.BytesIO(res.content)
        song = AudioSegment.from_mp3(sound)
        play(song)
    else:   # 실패
        print(res.status_code)
        print(res.json())