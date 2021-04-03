import requests
import io
from pydub import AudioSegment
from pydub.playback import play

URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize" 
HEADERS = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK 4cf5f301c1c62029f447bb1326dea702"
}

DATA = """
<speak>
그는 그렇게 말했습니다.
<voice name="MAN_DIALOG_BRIGHT">잘 지냈어? 나도 잘 지냈어.</voice>
<voice name="WOMAN_DIALOG_BRIGHT" speechStyle="SS_ALT_FAST_1">금요일이 좋아
요.</voice>

<voice name="WOMAN_READ_CALM"> 지금은 여성 차분한 낭독체입니다.</voice>
<voice name="MAN_READ_CALM"> 지금은 남성 차분한 낭독체입니다.</voice>
<voice name="WOMAN_DIALOG_BRIGHT"> 안녕하세요. 여성 밝은 대화체예요.</voice>
<voice name="MAN_DIALOG_BRIGHT">안녕하세요. 남성 밝은 대화체예요.</voice>

</speak>
"""

# 서버에 text 전송
res = requests.post(URL, headers = HEADERS, data = DATA.encode('utf-8'))
if res.status_code == 200:  # 성공
    # 음성 합성 결과를 파일로 저장하기
    with open("result.mp3", 'wb') as f:
        f.write(res.content)

    sound = io.BytesIO(res.content)
    song = AudioSegment.from_mp3(sound)
    play(song)
else:   # 실패
    print(res.status_code)
    print(res.json())   # 구체적으로 뭐가 잘못되었는지

# 음성 합성 결과를 파일로 저장하기
# with open("result.mp3", 'wb') as f:
#     f.write(res.content)

# 바로 재생하기
# https://ffmpeg.zeranoe.com/builds/
# 환경 변수에 경로 지정

# sound = io.BytesIO(res.content)
# song = AudioSegment.from_mp3(sound)

# 파일에서 재생하기
# song = AudioSegment.from_mp3("./result.mp3")
# play(song)