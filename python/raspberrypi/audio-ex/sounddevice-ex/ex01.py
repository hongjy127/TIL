import sounddevice as sd

duration = 5.5

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)

    print(frames, time)
    # 스피커로 소리나옴
    # indata로 여러가지 사운드 처리를 할 수 있음.
    outdata[:] = indata

with sd.Stream(channels=1, callback=callback):
    sd.sleep(int(duration * 1000))