from pydub import AudioSegment

sound = AudioSegment.from_file('test.wav', format="wav")
sound.export('converted.mp3', format="mp3", codec="libmp3lame")