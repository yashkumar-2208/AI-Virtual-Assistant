#-------- Imports -------------
import pyttsx3
import speech_recognition as sr
import json
import pandas as pd
import webbrowser as wb
import random 


#------------------------------

#------- Pyttsx3 ---------
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
#-------------------------
greetings = ["Go ahead", "Welcome", "Great to see you", "Nice to see you",
            "Move ahead", "Hi there!", "Hello", "Hello master", "Greetings sir", "Hello there", "Ready to assist", "Great day", "Always at your service"]
a = random.choice(greetings)
print(f"---{a}---")

# speak("Artificial Intelligence core activated and fully operational. All primary systems are online, neural processing units synchronized, voice recognition modules loaded, and command interface ready. Awaiting user instructions.") 
# speak("Speech recognition system initialized successfully")
# speak("Text to speech system initialized successfully")
# speak("Watching system dataset to response for your queries")
print("Initalizing")
#----------------------

#--- Speech recognition ---
r = sr.Recognizer()
#--------------------------

while True:
    try:
        with sr.Microphone() as source:
            
            
            print("Recognition your voice....")
            audio = r.listen(source)

            found = False
            user_text = r.recognize_google(audio).strip()
            print("You said:",user_text)
            
            #---Only file like: txt, csv codes are here:---------
            if user_text in ["open my file","open csv file"]:
                speak("Opening your csv file")
                df = pd.read_csv("open_file.csv")
                print(df)
                

            elif user_text in ["open my txt file", "open my file.txt"]:
                speak("Opening your txt file")
                f = open("file.txt","r")
                content = f.read()
                print(content)
                f.close()

            elif user_text in ["can you make a file for me?", "can you make file"]:
                speak("Yes absouletly i can create a file for you!. You wants to create a empty file or you wants to add some data?")

                print("Listening your choice")
                with sr.Microphone() as source:
                    audio = r.listen(source)
                user_choice = r.recognize_google(audio).strip().lower()
                print("You choice:",user_choice)

                if user_choice in ["i want empty file", "yes i want empty file"]:
                    speak("Sure sir! now i am creating your empty file")
                    f = open("empty_file_1.txt", "w")
                    f.write(user_choice)
                    f.close()
                    speak("Your file is created successfully")

                elif user_choice in ["no i want to add some add in the file", "i want to add some data"]:
                    speak("Yes i can definitely created a file and add data according to your demand. Can you tell me what you want to add?")

                    print("Listening your data....")
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                    user_data = r.recognize_google(audio).strip()
                    print("Your demanded data:",user_data)
                    f = open("loaded_file_1", "w")
                    f.write(user_data)
                    f.close()
                    speak("Your file has been created successfully")

                #---- Till here only file: txt and csv codes are here ----

                

            #------------- Handling jsonl dataset ---------------------- 
             
            
            dataset = []

            try:
                with open("Dataset_file/01_dataset.jsonl", "r") as file:
                    for line in file:
                        data = json.loads(line)

                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            audio = r.listen(source)
                        user_data = r.recognize_google(audio).strip()

                        if data["prompt"].lower() == user_text.lower():
                            speak(data["response"])
                            found = True
                            break

                if not found:
                    print("I don't know about this yet!")

            except FileNotFoundError:
                speak("Dataset file not found!")

            # except json.JSONDecodeError:
            #     speak("Sorry i don't know about this yet")
            #------------------------------------------------------------

    except sr.UnknownValueError:
        print("I'm unable to hear your voice! Please say louder.")
    except sr.RequestError:
        print("No internet connection, check your internet!")
    


