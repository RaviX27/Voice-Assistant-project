import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

hour = datetime.datetime.now().hour

def wishme():

    if hour >= 6 and hour <= 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("Welcome back")
    speak("how can i help you today sir!")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen (source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(query)
    except Exception as e:
        print(e)
        speak("I didn't get it sir, Can you tell it again!")
        takecommand()
        return 'none'

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak('Searching...')
            query = query.replace('wikipedia',"")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'offline' in query:
            if hour >= 22:
                speak("Good Night Sir!")
                quit()
            else:
                speak("Good Bye Sir, Have a nice dayS!")
                quit()
