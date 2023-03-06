import pyttsx3, os
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.record(source, duration=5)
    text = r.recognize_google(audio)
print(text)
path = os.path.dirname(os.path.realpath(__file__))

engine = pyttsx3.init() # object creation

# voices = engine.getProperty('voices')   
# for voice in voices:
#     print(voice.id)
rate = engine.getProperty('rate')
# print(rate)
engine.setProperty('rate', 125) 
text = text.lower()
if "code" in text:
    engine.say("Opening Visual Studio Code")
    os.system("code")
if "screenshot" in text:
    engine.say("Taking screenshot")
    os.system(f'python "{path}\screenshot-py\main.py"')
if ("chrome" or "google") in text:
    engine.say("Opening Chrome")
    os.system('"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"')
engine.runAndWait()
engine.stop()
