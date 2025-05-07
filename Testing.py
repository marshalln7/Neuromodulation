from pydub import AudioSegment

AudioSegment.converter = r"C:\Users\Administrator\Documents\Coding Relevant\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"
AudioSegment.ffprobe   = r"C:\Users\Administrator\Documents\Coding Relevant\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin\ffprobe.exe"

mp3_file = AudioSegment.from_mp3("calming-rain-257596.mp3")
wav_file = mp3_file.export("output.wav", format="wav")