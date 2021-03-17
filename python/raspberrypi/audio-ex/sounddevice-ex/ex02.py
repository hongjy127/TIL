import sounddevice as sd
import soundfile as sf

fs = 44100
seconds = 3

myrecording = sd.rec(int(seconds*fs), samplerate=fs, channels=1)
sd.wait()

sf.write('output.wav', myrecording, fs)