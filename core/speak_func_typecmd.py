import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices)
# Only voice at 0 index works, others are useless..........
engine.setProperty('voice', voices[0].id)

def speak(audio):
    '''
    <<<<<<<<<<<<<<<<<--------- Read Me Please ------------->>>>>>>>>>>>>>>>>
    speak() function is to make your string be spoke by TTS.
                      IMPORT THIS FUNCTION AS spfc
    <<<<<<<<<<<<<<<<------------- Thank You -------------->>>>>>>>>>>>>>>>>>
    '''
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak(input("Enter ->"))
