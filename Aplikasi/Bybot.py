# Import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import webbrowser
import datetime
import warnings
import calendar
import random
import wikipedia
import pyttsx3
from random import choice
from Text import Opening_text

print("initializing Bybot")

USERNAME = "Wita"
BOTNAME = "Bybot"

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


# Greet the user
def greet_user():
    """Greets the user according to the time"""
    hour = int(datetime.datetime.now().hour)
    if (hour >= 24) and (hour < 12):
        speak(f"Selamat Pagi {USERNAME}")
    elif (hour >= 12) and (hour < 18):
        speak(f"Selamat Siang {USERNAME}")
    elif (hour >= 18) and (hour < 24):
        speak(f"Selamat  {USERNAME}")
    speak(f"Hai Nama Saya {BOTNAME}. Adakah yang bisa dibantu?")


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Mendengarkan....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='id-ID')
        if not 'exit' in query or 'stop' in query:
            speak(choice(Opening_text))
        else:
            hour = int(datetime.datetime.now().hour)
            if hour >= 21 and hour < 6:
                speak("Selamat Malam {USERNAME}, Hati-Hati!")
            else:
                speak('Selalu Bahagia!')
            exit()
    except Exception:
        speak('Saya tidak mengerti, apakah bisa diulang?')
        query = None
    return query


# main start
greet_user()
query = take_user_input()

# logic for tasks
if "wikipedia" in query.lower():
    speak("searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    # webbrowser.open('youtube.com')
    url = "youtube.com"
    chrome_path = 'c:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
    # webbrowser.open('youtube.com')
    url = "google.com"
    chrome_path = 'c:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{USERNAME} the time is {strTime}")
