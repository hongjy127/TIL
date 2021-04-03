from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_file('test.wav', format="wav")
# song = AudioSegment.from_wav('test.wav')

play(song)      # 동기 함수: 재생중에 다른 일 못함(재생이 끝나야 exit 출력)
print("exit")