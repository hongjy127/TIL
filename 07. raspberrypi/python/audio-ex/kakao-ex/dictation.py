import requests
import json
kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

rest_api_key = "4cf5f301c1c62029f447bb1326dea702"

headers = {
    "Content-Type" : "application/octet-stram",
    "X-DSS-Service" : "DICTATION",
    "Authorization" : "KakaoAK 4cf5f301c1c62029f447bb1326dea702"
}

with open('heykakao.wav', 'rb') as fp:
    audio = fp.read()

res = requests.post(kakao_speech_url, headers=headers, data=audio)

if res.status_code == 200:
    # print(res.text)
    result_json_string = res.text[
        res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1
    ]
    result = json.loads(result_json_string)
    print(result)
    print(result['value'])
else:   # 실패
    print(res.status_code)
    print(res.json())


# multipart