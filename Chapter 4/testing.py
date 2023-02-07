import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui
import time


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


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said : ", query)
    except Exception as e:
        print(e)
        speak("Sorry guys, can you repeat that again?")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        speak("How can i help you?")
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching in wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open chrome' in query:
            os.startfile(
                'C:\Program Files\Google\Chrome\Application\chrome.exe')

        elif 'maximize this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')

        elif 'google search' in query:
            query = query.replace("google search", "")
            pyautogui.hotkey('alt', 'd')
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')

        elif 'youtube search' in query:
            query = query.replace("youtube search", "")
            pyautogui.hotkey('alt', 'd')
            time.sleep(1)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')

        elif 'open new window' in query:
            pyautogui.hotkey('ctrl', 'n')

        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')

        elif 'minimize this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')

        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')

        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl', 'j')

        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')

        elif 'next tab' in query:
            pyautogui.hotkey('ctrl', 'tab')

        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')

        elif 'close window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'w')

        elif 'clear browsing history' in query:
            pyautogui.hotkey('ctrl', 'shift', 'delete')

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'youtube' in query:
            webbrowser.open("youtube.com")
            speak("youtube is opened")
        elif 'google' in query:
            webbrowser.open("google.com")
            speak("google is opened")
        elif 'email' in query:
            webbrowser.open("gmail.com")
            speak("gmail is opened")
        elif 'chat' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("whatsapp is opened")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'open code' in query:
            codePath = "D:\Proyek 3\App9"
            os.startfile(codePath)
        elif 'stop' in query:
            speak("see you soon smartboy")
            exit()
        elif 'hello' in query:
            wishMe()
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "screenshot" in query:
            speak('tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif "open notepad" in query:
            npath = "C:\WINDOWS\system32\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")

        else:
            speak("Im not understand")
