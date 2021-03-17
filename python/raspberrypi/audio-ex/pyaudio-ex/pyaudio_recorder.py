import pyaudio
import wave

CHUNK = 1024                # 버퍼 크기
FORMAT = pyaudio.paInt16    # byte
CHANNELS = 1                # or 2
RATE = 16000 # 44100                # CD 음질

# TTS: Text To Speech (음성 합성) -> MP3
# STT: Speekch To Text (음성 인식) -> 16K 음성 데이터 ***

RECORD_SECONDS = 5        # 녹음시간 5초
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

# 장치 - 배타적 사용(다른 곳에서 사용하면 사용 불가)
# --> 장치 권한을 받아야 함
stream = p.open(input_device_index=1,   # 자신에게 맞는 장치 번호 지정
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
            
print("Start to record the audio.")
frames = []

# 5초 동안 돌아감
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK, exception_on_overflow=False)
    frames.append(data)

print("Recording is finished.")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

