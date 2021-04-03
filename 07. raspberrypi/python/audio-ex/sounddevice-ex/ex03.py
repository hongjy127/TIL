from gpiozero import Button, LED
from signal import pause
import sounddevice as sd
import soundfile as sf
from audioapi import *

fs = 16000
# fs = 44000
seconds = 3

led = LED(21)
btn = Button(20)

def start_record():
    led.on()
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write('output.wav', myrecording, fs)

    with open('output.wav', 'rb') as f:
        audio = f.read()
        ret, data = stt(audio)
        if ret:
            print(f'인식 결과: {data}')
            if data == "불 꺼":
                pass
            elif data == "불 켜":
                pass
        else:
            print(f'인식 실패: {data}')
    led.off()

btn.when_pressed = start_record

pause()