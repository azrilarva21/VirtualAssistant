import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Guys")
    elif hour >= 12 and hour < 4:
        speak("Good afternoon Guys")
    else:
        speak("Good Evening Guys")

    speak("I am your Assistant Wita")
