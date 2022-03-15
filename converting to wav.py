import pydub
input_file = r"C:/Users/dines/Downloads/sample1.mp3"
sound = pydub.AudioSegment.from_mp3(input_file)
sound.export(r"C:\Users\dines\Music\test\apple.wav", format="wav")
