#------------ Imports ---------------#
from Backend.model import Mahiru_Model
import speech_recognition as sr
import pyttsx3
#------------------------------------#

#------- Pyttsx3 ---------
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    speak("Artificial Intelligence core activated and fully operational. All primary systems are online, neural processing units synchronized, voice recognition modules loaded, and command interface ready. Awaiting user instructions.") 
    speak("Speech recognition, Pyttsx3, Pyaudio system initialized successfully")
    speak("Text to speech system initialized successfully")
    speak("Watching system dataset to response for your queries")
#-------------------------

while True:

    

    r = sr.Recognizer()
    with sr.Microphone() as source:
                  
        print("Recognition your voice....")
        audio = r.listen(source)
        user_text = r.recognize_google(audio).strip()
        print("You said:",user_text)
        response = Mahiru_Model.get_response(user_text)
        print("Mahiru:", response)
