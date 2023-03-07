import os
from core.wishMe import wishMe
from core.speak import speak
from core.takeCommand import takeCommand
from core.webbrow import webbrowser
from core.calculatewolf import computational_intelligence
from core.copy2clip import copy2clip
from core.passwordgen import newpassword

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
        elif 'previous' in query and 'command' in query:
            with open('remember.txt', 'r') as f:
                speak(f.read())
            f.close()
            continue
        elif "calculate" in query or "what is" in query or "who is" in query or "find" in query:
            question = query
            answer = computational_intelligence(question)
            print("Answer:", answer)
            speak(answer)
        elif 'close' in query:
            exit()
        elif 'generate' in query and 'password' in query:
            password = newpassword(12)
            copy2clip(password)
            speak("Password copied to clipboard")
        if query != ".":
            with open("remember.txt", "w") as f:
                f.write(query)
            f.close()
