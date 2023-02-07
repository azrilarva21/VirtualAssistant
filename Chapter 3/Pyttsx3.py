import pyttsx3

engine = pyttsx3.init()  # pembuatan objek

""" RATE"""
rate = engine.getProperty('rate')   # mendapatkan detail laju bicara saat ini
print(rate)  # mencetak laju suara saat ini
engine.setProperty('rate', 125)     # menyiapkan kecepatan suara baru


"""VOLUME"""
volume = engine.getProperty(
    'volume')  # mengenal tingkat volume saat ini (min=0 dan maks=1)
print(volume)  # printing level volume saat ini
engine.setProperty('volume', 1.0)    # menyetel level volume antara 0 dan

"""VOICE"""
voices = engine.getProperty('voices')  # mendapatkan detail suara saat ini
# engine.setProperty('voice', voices[0].id)  #mengubah indeks, mengubah suara. o untuk mesin laki-laki
# mengubah indeks, mengubah suara. o untuk mesin perempuan
engine.setProperty('voice', voices[1].id)

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()
