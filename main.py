import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
from PIL import ImageGrab

def random_var():
    return random.randint(1, 99)


engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
engin.setProperty('voice', voices[1].id)


def speak(audio):
    engin.say(audio)
    engin.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I'm layla. how may i help you today,")


def takeCommand():
    '''
    It takes microphone input from the user and return string output.
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='eng-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open_new_tab('youtube.com')

        elif 'open google' in query:
            webbrowser.open_new_tab('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open_new_tab('stackoverflow.com')

        elif 'open zoro.to' in query:
            webbrowser.open_new_tab('zoro.to')
            
        elif 'play music' in query:
            music_dir = 'D:\\Music\\Deep Focus'
            music = os.listdir(music_dir)
            print(music)
            os.startfile(os.path.join(music_dir, music[random_var()]))

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is: {str_time}")
            speak(f"The time is: {str_time}")

        elif 'take a screenshot' in query:
            image = ImageGrab.grab()
            image.show()

        elif 'open code' in query:
            code_path ="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'open edge' in query:
            code_path ="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(code_path)
            
        elif 'open edge' in query:
            code_path ="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(code_path)

        elif 'quit' in query:
            print("thank you sir, see you again soon")
            speak("thank you sir, see you again soon")
            exit()
