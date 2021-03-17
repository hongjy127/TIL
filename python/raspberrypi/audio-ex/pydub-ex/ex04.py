from pydub import AudioSegment

sound = AudioSegment.from_file('test.mp3', format="mp3")
sound.export('converted.wav', format="wav")