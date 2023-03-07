import datetime
try:
    import speak as spfc
except:
    import core.speak as spfc 
hour = int(datetime.datetime.now().hour)


def wishMe():
    '''
    <<<<<<<<<<<<<<<<<--------- Read Me Please ------------->>>>>>>>>>>>>>>>>
    wishMe() function is to make your program greet you according to time.
    <<<<<<<<<<<<<<<<------------- Thank You -------------->>>>>>>>>>>>>>>>>>
    '''
    if hour >= 0 and hour < 12 :
        spfc.speak("Good Morning, Ayush!")

    elif hour >= 12 and hour < 18 :
        spfc.speak("Good Afternoon, Ayush!")

    else :
        spfc.speak("Good Evening, Ayush!")

    spfc.speak("I am JARVIS. Please tell me how may I help you?")


if __name__ == "__main__":
   wishMe()
