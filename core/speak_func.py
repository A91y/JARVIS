import pyttsx3

engine = pyttsx3.init("sapi5")
# voices = engine.getProperty('voices')
# print(voices)
# Only voice at 0 index works, others are useless.......... # Old PC config
# engine.setProperty('voice', voices[0].id)
# for voice in voices:
#     print(voice.id)
# rate = engine.getProperty('rate')
# print(rate)
# engine.setProperty('rate', 125)

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
    speak('Hi Sir, can you hear me')