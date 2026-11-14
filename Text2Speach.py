from gtts import gTTS

text = "Hello Shazam welcom to python, i will be your assistant."

tts = gTTS(text=text, lang="en")

tts.save("speach.mp3")

print("Speach saved as speach.mp3")