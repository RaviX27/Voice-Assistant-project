import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.ehlo()
    server.starttls()
    server.login('Ravii27X@gmail.com','########')
    server.sendmail('Ravii27X@gmail.com',to,content)
    server.close()

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
        elif 'send email' in query:
            try:
                speak('What is the content?')
                content = takecommand()
                to = 'abc@gmail.com'
                sendEmail(to,content)
                speak("Email is Sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")

        elif 'search' in query:
            speak('What do you need to search?')
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'offline' in query:
            if hour >= 22:
                speak("Good Night Sir!")
                quit()
            else:
                speak("Good Bye Sir, Have a nice dayS!")
                quit()
