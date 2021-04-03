# 임의의 길이 녹음

import io
import queue
import sounddevice as sd
import soundfile as sf
import sys

samplerate = 44100
channels = 1
sd.default.samplerate = samplerate
sd.default.channels = channels

q = queue.Queue()   # 동기화 큐
recMem = io.BytesIO()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())    # 녹음 데이터를 큐에 추가

try:
    with sf.SoundFile(recMem, mode='x', format='wav',
                    samplerate=samplerate, channels=channels) as file:
        with sd.InputStream(callback=callback): # 녹음시작
            print('#' * 80)
            print('press Ctrl+C to stop the recording')
            print('#' * 80)
            # 메인 스레드
            while True:
                # 큐에 녹음 데이터가 있다면 추출하여 파일에 기록
                file.write(q.get())

except KeyboardInterrupt:
    print(recMem.tell())
    print('\nRecording finished: ')
except Exception as e:
    print(e)