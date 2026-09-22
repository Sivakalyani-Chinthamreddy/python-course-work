#pip install SpeechRecognitio
#pip insatll pyttsx3

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
#------------------------
#SPEAK FUNCTION
#------------------------

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

#------------------------------
#LISTEN FUNCTION
#------------------------------
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..................")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        print("Audio Done")
    try:
        command = recognizer.recognize_google(audio, language='en-in')
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, i didn't understand.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavilable.")
        return ""
#--------------------------------------
#PROCESS COMMAND
#--------------------------------------
speak("Hello i am your voice assistence. how can i help you")

while True:

    command = listen()
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M:%p")

        speak(f"the current time is {current_time}")
    elif "date" in command:
        today=datetime.datetime.now().strftime("%d %B %Y")
        speak(f"today date is {today}")

    elif "open google" in command:
        speak("Opening google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")

    elif "Who created you" in command:
        speak("i was created using python")

    elif "bye" in command or "exit" in command:
        speak("bye,have a great day")
        break
    else:
        speak("sorry i do not know that command")