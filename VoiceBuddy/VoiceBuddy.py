import webbrowser

import  pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import comtypes.client
from django.templatetags.i18n import language
from django.utils.lorem_ipsum import sentence

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Goog Morning")
    elif hour>= 12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your Buddy , Tell me how can I help u bro ")

def takecommand ():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognization")
        query = r.recognize_google(audio, language='en-in')

        print(f"user said {query}\n")

    except Exception as e:
        print("Say that again Please.....")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    if 1 :
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching in wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open music' in query:
            webbrowser.open("youtubemusic.com")

        elif 'open news' in query:
            webbrowser.open("https://www.thehindu.com/")

        elif 'favourite song' in query:
            webbrowser.open("https://music.youtube.com/watch?v=x9EoXWJ_cWM")

        elif 'open word' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
        elif 'open chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open excel' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sir , the time is {strTime}")
