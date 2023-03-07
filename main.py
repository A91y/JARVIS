import os
from core import wishMe
from core import speak
from core import takeCommand
from core import webbrowser

app_paths = {
    'google_chrome_path': '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'
}
path = os.path.dirname(os.path.realpath(__file__))


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "code" in query:
            speak("Opening Visual Studio Code")
            os.system("code")

        elif "screenshot" in query:
            speak("Taking screenshot")
            os.system(f'python "{path}\screenshot_py\main.py"')
        elif ("chrome" or "google") in query:
            speak("Opening Chrome")
            os.startfile(app_paths["google_chrome_path"])
        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com", new=1)
        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com", new=1)
        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open("stackoverflow.com", new=1)

        elif 'close' in query:
            exit()
