from pydub import AudioSegment
from pydub.playback import play
import io
import requests

# 파일을 읽어서 BytesIO로 만듦
with open('test.wav', 'rb') as f:
    wavMem = io.BytesIO(f.read())

# mp3를 저장할 BytesIO 만듦
mp3Mem = io.BytesIO()
sound = AudioSegment.from_file(wavMem, format="wav")    # 파일명 대신 BytesIO 객체도 가능
sound.export(mp3Mem, format="mp3", codec="libmp3lame")

print(mp3Mem.tell())
mp3Mem.seek(0)

song = AudioSegment.from_mp3(mp3Mem)
play(song)

# mp3Mem.seek(0)
# upload = {'image': mp3Mem}

# res = requests.post('http://127.0.0.1:8080/test', files = upload)
