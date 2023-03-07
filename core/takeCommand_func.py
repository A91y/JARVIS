import speech_recognition as sr
try:
    import speak_func as spfc
except:
    import core.speak_func as spfc 


def takeCommand():
    '''
    <<<<<<<<<<<<<<<<<--------- Read Me Please ------------->>>>>>>>>>>>>>>>>
        takeCommand() function is to give user's microphone input
                           IMPORT ME AS tkcmmd
                  This requires internet connection
    <<<<<<<<<<<<<<<<------------- Thank You -------------->>>>>>>>>>>>>>>>>>
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Default is 0.8
        r.energy_threshold = 300  # Default is 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        # spfc.speak("Say That Again Please...")
        # print("Say That Again Please...")
        return "."
    return query


#  query = takeCommand().lower()
# Use me after while loop or for loop o


if __name__ == "__main__":
    spfc.speak("Speak Your Test Command")
    while True:
        query = takeCommand().lower()

        if 'hello' in query:
            spfc.speak("Hello")
            print("Hello")

        elif 'done' in query:
            spfc.speak("Ok Quitting")
            exit()

        else:
            spfc.speak(query)
            print("U said:"+" " + query)
