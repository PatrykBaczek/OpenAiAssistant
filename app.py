import playsound
import speech_recognition as sr
from gtts import gTTS as gts
import os

def speak(text):
    tts = gts(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    # os.system('cmd /c "del voice.mp3"')
    os.remove("voice.mp3")

def get_audio():
    r = sr.Recognizer()
    print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language='en')
        except Exception as e:
            print("Waiting for questions..." + str(e))

    return said

speak("Hello")
print("Hello")
        