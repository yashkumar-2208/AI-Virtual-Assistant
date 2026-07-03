#-------- Imports -------------
import pyttsx3
import speech_recognition as sr
import json 
import pandas as pd
import webbrowser as wb
import random 
import re
import nltk
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer #future use 
from nltk.tokenize import word_tokenize 
import webbrowser
import wikipediaapi

#--------------------------------------

#-----------NLTK-------------------#
# nltk.download('punkt_tab')
# nltk.download('stopwords')
# nltk.download('punkt')
#for future use:
# ps = PorterStemmer()
# words = ["program", "programs", "programmer", "programming", "programmers"]
# for w in words:
#     print(w, " : ", ps.stem(w))
#----------------------------------#

class Mahiru_Model():

    
    #------- Pyttsx3 ---------
    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    #-------------------------


    greetings = ["Go ahead", "Welcome", "Great to see you", "Nice to see you","Go for it",
                "Move ahead", "Hi there!", "Hello", "Hello master", "Greetings sir",
                 "Hello there", "Ready to assist", "Great day", "Always at your service"]

    print("╔═════════════════════════════════════════╗")
    print(f"║      {random.choice(greetings):<34} ║")
    print("╚═════════════════════════════════════════╝")

    speak("Artificial Intelligence core activated and fully operational. All primary systems are online, neural processing units synchronized, voice recognition modules loaded, and command interface ready. Awaiting user instructions.") 
    speak("Speech recognition, Pyttsx3, Pyaudio system initialized successfully")
    speak("Text to speech system initialized successfully")
    speak("Watching system dataset to response for your queries")

    # print("Initalizing")
    #----------------------



    while True:
        try:

            # ----------Speech recognition module here:-------------------#
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Recognition your voice....")
                audio = r.listen(source)
                found = False
                user_text = r.recognize_google(audio).strip()
                print("You said:",user_text)
            #------------- End of speech recognition module ---------------#
            

                #Preprocess input (typo correction etc.)
                user_text = user_text.lower().strip()
                command = {'hlw':'hello','helo': 'hello', 'hlo': 'hello', 'hello ji': 'hello','hloo':'hello', 'hlooo':'hello', 'hello world': 'hello world is basic programming codes.',
                    'hi': 'hello', 'hey': 'hello', 'wat': 'what', 'wut': 'what', 'hows': 'how is', 'howz': 'how is','how\'s':'how is',"you're":"you are","u'r":"you are",'u': 'you','Hey':'Hi','Hi':'hey',
                    'pls': 'please', 'plz': 'please', 'plez': 'please',  'r': 'are', 'yr': 'your', 'ur': 'your', "I'm":"I am",'l8r': 'later','gr8': 'great', "an":"the","the":"an","a":"an",
                    'thx': 'thanks', 'tnx': 'thanks', 'thanx': 'thanks', 'sry': 'sorry', 'brb': 'be right back','lol': 'laughing out loud','smh': 'shaking my head',"I":"i","i":"I",
                    'btw': 'by the way', 'omg': 'oh my god', 'np': 'no problem','idk': 'I don\'t know','jk': 'just kidding', 'afaik': 'as far as I know', 
                    'imo': 'in my opinion', "b/w":"between",'hf': 'have fun', 'wdym': 'what do you mean','gotta': 'got to', 'outta': 'out of','gonna': 'going to',  
                    'tbh': 'to be honest', 'fyi': 'for your information', "abba":"father", "amma":"mummy","amma":"mother","thxxx":"thanks", "abba":"papa", 
                    'yw': 'you\'re welcome', 'gg': 'good game', 'gl': 'good luck',  'def': 'definitely','cuz': 'because', 'sup': 'what\'s up','lemme': 'let me',
                    'irl': 'in real life', 'atm': 'at the moment', 'b4': 'before', "plz":"please", "hehe":"happy😂", 'sorta': 'sort of','yea': 'yes','ya': 'you', 
                    'dunno': 'don\'t know', 'gimme': 'give me', 'kinda': 'kind of', 'ty': 'thank you', 'tho': 'though', 'til': 'until', 'vs': 'versus', 
                    'wanna': 'want to', 'yep': 'yes', 'yup': 'yes', 'nah': 'no', 'nope': 'no', 'gm': 'good morning', 'gn': 'good night','Wat': 'What', 'Wut': 'What',
                    'an': 'afternoon', 'Helo': 'Hello', 'Hi': 'Hello', 'Hey': 'Hello', 'R': 'Are', 'Thx': 'Thanks', 'Sry': 'Sorry','Plz': 'Please', 'U': 'You',"u":"are","u":"you",
                    'Lol': 'Laughing out loud', 'Idk': 'I don\'t know', 'Tbh': 'To be honest', 'Jk': 'Just kidding','Pls': 'Please', 'Sup': 'What\'s up', 
                    'Np': 'No problem', 'Yw': 'You\'re welcome', 'Gg': 'Good game', 'Gl': 'Good luck', 'Nope': 'No', 'Kinda': 'Kind of','Yup': 'Yes', 'Nah': 'No', 
                    'Gonna': 'Going to', 'Wanna': 'Want to', 'Cuz': 'Because', 'Tho': 'Though', 'Ya': 'You', 'Omg': 'Oh my god','Brb': 'Be right back', 'Yep': 'Yes', 
                    'Imo': 'In my opinion','Smh': 'Shaking my head', 'Fyi': 'For your information', 'Irl': 'In real life', 'Atm': 'At the moment',
                    'Gimme': 'Give me', 'Lemme': 'Let me', 'Outta': 'Out of', 'Sorta': 'Sort of', 'Ty': 'Thank you','Wdym': 'What do you mean', 'Yea': 'Yes', 'Yaya':'Yes',
                    'Afaik': 'As far as I know', 'Til': 'Until', 'Vs': 'Versus', 'Dunno': 'Don\'t know', 'Def': 'Definitely', 'B4': 'Before',
                    'Hf': 'Have fun', 'Gr8': 'Great', 'L8r': 'Later', 'Thanx': 'Thanks', 'Tnx': 'Thanks', 'Ur': 'Your', 'Hows': 'How is', 'Plez': 'Please', 
                    'Yr': 'Your', 'Howz': 'How is',"gf":"girl friend", "bf":"boyfriend","frnd":"friend","thxx":"thanks", "hehe":"happy", "hehehe":"happy","he":"hello",
                    "hehehehe":"happy", "hehhehehe":"hehe", "hehehehhehe":"hehe","hehhehehehhe":"hehehe", "hehhee":"hehehehe", "gc":"group chat", "vn":"voice note",
                    "an":"after noon", "ha":"yes", "hh":"yes", "yup":"yes", "haa":"yes", "hn":"yes", "hhh":"yes", "hmm":"yes", "y tho": "but why",
                    "srk":"shah rukh khan", "gadha":"Gawar", "anpad":"Gawar","useless":"Non-sense","dumb":"Non-sense","use less":"Non-sense","use-less":"Non-sense",
                    "without brain":"Non-sense", "pagal":"Gawar" , "pgal":"Gawar" , "paghl":"Gawar", "Suar":"Gawar", "Ohh":"Oh","Ohhh":"Oh","Ohhhh":"Oh","yayaya":"yaya","ya":"yaya",
                    "Elon musk":"elon musk on wikipedia", "ove":"love","love":"ove", "AI":"Artificial Intelligence", "Ohhhhh":"Oh",'Artificial Intelligence':'AI',
                    "umm":"um","ummm":"um","ummmm":"um","ummmmm":"um","ummmmmm":"um","ummmmmmm":"um","uum":"um","uuum":"um","uuuum":"um","uuuuum":"um","uumm":"um","uuumm":"um","uuuummmm":"um",
                    "wah":"waah","wahh":"waah","wahhh":"waah","waaah":"waah","waaahh":"waah","waaahhh":"waah","Okk":"Ok","Ook":"Ok","Ookk":"Ok","Okkk":"Okay","Oookkk":"Okay","Okokok":"Ok","okokkokok":"Okay",
                    "bio":"biography", "info":"information", "first":"1","1st":"1", "second":"2", "2nd":"2", "third":"3", "3rd":"3", "fouth":"4","4th":"4",
                    "yo":"hello","hola":"hello","haan":"yes","han":"yes","haa":"yes","haanji":"yes","bilkul":"yes","sure":"yes","ok":"yes","okay":"yes","okey":"yes",
                    "na":"no","nahi":"no","nhi":"no","never":"no","thank you":"thanks","thanku":"thanks","thankuu":"thanks","thankyou":"thanks","thanks a lot":"thanks",
                    "bye":"goodbye","bye bye":"goodbye","good bye":"goodbye","see you":"goodbye","see ya":"goodbye","take care":"goodbye",
                    "whats up":"what is up","wassup":"what is up","sup bro":"what is up","how r u":"how are you","how ru":"how are you","how are u":"how are you",
                    "yt":"youtube","utube":"youtube","you tube":"youtube","google chrome":"chrome","g chrome":"chrome",
                    "ml":"machine learning","dl":"deep learning","nlp":"natural language processing","cv":"computer vision",
                    "py":"python","js":"javascript","cpp":"c plus plus","c#":"c sharp","html5":"html","css3":"css",
                    "txt":"text file","csv":"comma separated values file","pdf":"portable document format","doc":"document","docs":"document",
                    "insta":"instagram","ig":"instagram","fb":"facebook","msg":"message","dm":"direct message",
                    "happyyy":"happy","sadyy":"sad","angryyy":"angry","awesomee":"awesome","greattt":"great",
                    "kr":"kar","krna":"karna","krdo":"kar do","krde":"kar de","bta":"bata","btao":"batao",
                    "mujhe":"me","mera":"my","meri":"my","kya":"what","kaise":"how","kab":"when","kaha":"where","kyu":"why",
                    "bro":"brother","sis":"sister","fr":"for real","ikr":"i know right","rofl":"rolling on floor laughing","asap":"as soon as possible",
                    "tmrw":"tomorrow","tmrw":"tomorrow","tdy":"today","ystrdy":"yesterday","msg me":"message me","call me":"phone me",
                    "luv":"love","lv":"love","fav":"favorite","favrt":"favorite","congrats":"congratulations","congo":"congratulations",
                    "photo":"image","pic":"picture","pics":"pictures","vid":"video","vids":"videos","dp":"profile picture",
                    "cpu":"processor","gpu":"graphics card","ram":"memory","ssd":"storage","hdd":"hard disk",
                    "wifi":"wireless internet","net":"internet","pc":"computer","lappy":"laptop","mob":"mobile","cell":"phone",
                    "gtg":"got to go", "ttyl":"talk to you later", "omw":"on my way", "idc":"I don't care", "ily":"I love you", "ilysm":"I love you so much",
                    "wbu":"what about you", "hbu":"how about you", "nvm":"never mind", "rn":"right now", "tbf":"to be fair", "ngl":"not gonna lie", "fomo":"fear of missing out",
                    "yolo":"you only live once", "bff":"best friend forever", "omfg":"oh my god", "wtf":"what the heck", "idek":"I don't even know", "smth":"something", "sth":"something",
                    "rly":"really", "prolly":"probably", "probs":"probably", "obvi":"obviously", "obv":"obviously", "totes":"totally", "srsly":"seriously",
                    "k":"okay", "kk":"okay", "aight":"alright", "ight":"alright", "hmu":"hit me up", "wym":"what you mean", "tysm":"thank you so much",
                    "nm":"nothing much", "wyd":"what you doing", "hbd":"happy birthday", "gn8":"good night", "cya":"see you", "l8":"late", "m8":"mate",
                    "str8":"straight", "w8":"wait", "h8":"hate", "2day":"today", "2morrow":"tomorrow", "4ever":"forever", "rmb":"remember", "rmbr":"remember",
                    "pix":"pictures", "fam":"family", "bestie":"best friend", "squad":"friend group", "lit":"amazing", "fire":"amazing", "sus":"suspicious",
                    "cap":"lie", "no cap":"no lie", "bet":"agreed", "lowkey":"somewhat secretly", "highkey":"very openly", "deadass":"seriously",
                    "finna":"going to", "tryna":"trying to", "mighta":"might have", "coulda":"could have", "shoulda":"should have", "woulda":"would have",
                    "cmon":"come on", "dis":"this", "dat":"that", "wen":"when", "wer":"where", "wy":"why", "thru":"through", "altho":"although",
                    "nite":"night", "rite":"right", "lyk":"like", "jus":"just", "frm":"from", "wit":"with", "evry":"every", "evryone":"everyone",
                    "sumtimes":"sometimes", "neva":"never", "betta":"better", "tgthr":"together", "wknd":"weekend", "bday":"birthday", "anniv":"anniversary",
                    "vac":"vacation", "apt":"appointment", "mtg":"meeting", "appt":"appointment", "sched":"schedule", "addy":"address", "rec":"recommendation",
                    "recs":"recommendations", "specs":"specifications", "convo":"conversation", "convos":"conversations", "sitch":"situation", "deets":"details",
                    "yikes":"oh no", "oof":"ouch", "rip":"rest in peace", "fml":"frustrated with my life", "smdh":"shaking my darn head", "istg":"I swear to god",
                    "idts":"I don't think so", "imy":"I miss you", "jic":"just in case", "fwiw":"for what it's worth", "iirc":"if I recall correctly",
                    "ymmv":"your mileage may vary", "eli5":"explain like I'm five", "tldr":"too long didn't read", "op":"original poster", "pm":"private message",
                    "rt":"retweet", "tt":"tiktok", "snap":"snapchat", "wp":"whatsapp", "wa":"whatsapp", "tg":"telegram", "disc":"discord", "gh":"github","meh":"not interested", "msgd":"messaged", "newb":"beginner",
                    "app":"application", "apps":"applications", "sw":"software", "hw":"hardware", "db":"database", "api":"application programming interface",
                    "ui":"user interface", "ux":"user experience", "vpn":"virtual private network", "url":"web address", "www":"world wide web",
                    "faq":"frequently asked questions", "diy":"do it yourself", "eta":"estimated time of arrival", "aka":"also known as", "etc":"et cetera",
                    "eg":"for example", "ie":"that is", "w/":"with", "w/o":"without", "b/c":"because", "b/t":"between", "tba":"to be announced", "fren":"friend", "goat":"greatest of all time", "gratz":"congratulations", "gud":"good", "gud mrng":"good morning",
                    "tbd":"to be decided", "tbc":"to be confirmed", "nsfw":"not safe for work", "fyp":"for you page", "ide":"integrated development environment",
                    "repo":"repository", "pr":"pull request", "ci":"continuous integration", "cd":"continuous deployment", "qa":"quality assurance","yeee":"yes", "yeeep":"yes", "cmon bro":"come on brother", "sup dude":"what is up",
                    "sdk":"software development kit", "lan":"local area network", "wan":"wide area network", "iot":"internet of things", "vr":"virtual reality",
                    "ar":"augmented reality", "accha":"good", "theek":"fine", "theek hai":"fine", "chalo":"let's go", "chal":"go", "jaldi":"quickly", "okii":"okay", "ppl":"people", "prob":"problem", "sec":"second",
                    "abhi":"now", "kal":"tomorrow", "phir":"then", "sach":"true", "jhooth":"lie", "paisa":"money", "khana":"food", "pani":"water","yo bro":"hello brother", "yooo":"hello", "yuppers":"yes",
                    "ghar":"home", "kaam":"work", "samay":"time", "subah":"morning", "shaam":"evening", "raat":"night", "din":"day", "saal":"year","tru":"true", "u there":"are you there", "urself":"yourself", "vry":"very",
                    "kyun":"why", "kahan":"where", "kaun":"who", "lekin":"but", "agar":"if", "matlab":"meaning", "pata":"know", "sahi":"correct", "kkk":"okay", "mhm":"yes", "mmk":"okay", "npnp":"no problem",
                    "asl":"age sex location", "bae":"before anyone else", "bc":"because", "cya later":"see you later", "dm me":"send me a direct message", "goated":"excellent", "drip":"fashionable",
                    "gud nyt":"good night", "hows life":"how is life", "hw":"how", "ily2":"i love you too", "izzit":"is it", "kewl":"cool", "lmk":"let me know", 
                    "np bro":"no problem brother", "ofc":"of course", "ohk":"okay", "ohkay":"okay", "okie":"okay", "okies":"okay","cos":"because", "abt":"about", "frfr":"for real",
                    "soz":"sorry", "supa":"super", "tc":"take care", "thnk":"think", "thnks":"thanks", "thnk u":"thank you", "dope":"awesome", "savage":"bold", "flex":"show off", "vibe":"feeling",
                    "welp":"well", "whatcha":"what are you", "whos":"who is", "wid":"with", "wlc":"welcome", "wrk":"work", "yaar":"friend", "bussin":"very tasty", "periodt":"end of discussion",
                    "zzz":"sleeping", "2nite":"tonight", "2gether":"together", "4u":"for you", "4me":"for me", "bcoz":"because", "coz":"because",  "based":"agreeable", "sigma":"independent person", "alpha":"leader",
                    "ggs":"good games", "hru":"how are you", "hwru":"how are you", "ic":"i see", "imoo":"in my opinion", "jk lol":"just kidding", "cop":"buy", "dub":"victory", "opp":"opponent",
                    "roger":"understood", "thooo":"though", "ttys":"talk to you soon", "wassgood":"what is good", "wtv":"whatever", "yaa":"yes", "wildin":"acting crazy",
                    "broski":"brother", "homie":"friend", "wassup dude":"what is up", "yo wassup":"hello", "bruh":"brother", "legit":"genuine",  "gang gang":"close friends",
                    "flex":"show off", "vibe":"feeling", "ghosted":"stopped replying", "stan":"big fan", "slay":"do very well", "mood":"same feeling", "clutch":"critical success",
                    "tea":"gossip", "spill the tea":"tell the gossip", "snatched":"looks amazing", "salty":"upset", "pressed":"annoyed", "shook":"surprised", 
                    "main character":"center of attention", "npc":"boring person", "mid":"average", "clout":"fame", "rizz":"charm", "w":"win", "l":"loss", "aura":"presence",
                    "cook":"do something well", "let him cook":"let him continue", "simp":"overly affectionate person", "delulu":"delusional", "cringe":"embarrassing",
                    "frfr":"for real", "no shot":"impossible", "say less":"I understand", "bet that":"agreed", "facts":"true", "big yikes":"very awkward", "sheesh":"wow", 
                    "fam":"family/friends", "brodie":"brother", "bestie":"best friend", "squad":"friend group", "ride or die":"loyal friend", "day one":"old friend", "gng":"gang",
                    "lowkey":"secretly", "highkey":"openly", "extra":"overdramatic", "sus":"suspicious", "cap":"lie", "no cap":"truth", "deadass":"seriously", "on god":"I swear",
                    "fumble":"miss an opportunity", "bag secured":"success achieved", "glow up":"major improvement", "touch grass":"go outside", "rent free":"constantly on mind",
                    "locked in":"fully focused", "cooked":"in trouble", "cookin":"doing great", "sweat":"tryhard player", "grind":"work hard", "afk":"away from keyboard", "ez":"easy", 
                    "yeet":"throw forcefully", "skrrt":"leave quickly", "finna":"going to", "trippin":"overreacting", "capper":"liar", "goofy":"silly", "banger":"excellent", "fire":"amazing"
}

                user_text = command.get(user_text, user_text)

                #------------------------ Clean punctuation -----------------------------#
                # user_text = re.sub(r"[^0-9A-Z\s]","", user_text)
                # print(user_text)
                #----------------------------- End --------------------------------------#

                #------------ Using NLTK ------------#
                # #1:
                sentence = user_text
                words = word_tokenize(sentence)

                #2:
                tokens = word_tokenize(user_text)
                clean_text = [
                word for word in tokens
                if word.isalnum()
                    ]
                (''.join(clean_text))
            #------------- End of NLTK --------------#
            

                #-------- Mahiru ----------#
                if user_text in ["mahiru", "hey mahiru", "hello mahiru", "mahiru suno",
                                "suno mahiru", "maheeru", "hi mahiru","maheru","maheeru",
                                "maheru","myra"]:
                    speak("Jii boss! Mah yahan hoon. Aapne mujhe yaad kiya? Mah poori tarah taiyar hoon aapki madad karne ke liye. Bataiye, aaj hum kya interesting karne wale hain?")
                    continue
                #------ End Mahiru -------#

                #---Only file like: txt, csv codes are here:---------
                elif user_text in ["open my file","open csv file"]:
                    speak("Opening your csv file")
                    df = pd.read_csv("open_file.csv")
                    print(df)
                    continue
                    

                elif user_text in ["open my txt file", "open my file.txt", "open text file", "open txt file", "open my text file",
                                "show my txt file", "show text file", "read my txt file", "read text file", "display my txt file",
                                "display text file", "open the txt file", "open the text file", "load my txt file", "access my txt file",
                                "view my txt file", "meri txt file kholo", "meri text file kholo", "txt file open karo", "text file open karo",
                                "meri file dikhao", "text file dikhao", "txt file dikhao", "meri text file padho", "file padh ke sunao"
                                ]:
                    speak("Opening your txt file")
                    speak("Your txt file opened successfully")
                    print("--Here is your txt file--")
                    with open("Back-end/file.txt","r") as f:
                        content = f.read()
                        print(content)
                        f.close()
                    print("--End of txt file--")
                    continue

                elif user_text in ["can you make a file for me", "can you make file", "create a file for me", "mere liye ek file banao", "ek new file create karo",
                                "can you make a file for me", "can you make file", "create a file for me", "make a new file", "please create a file", "create file", "make file", "generate a file",
                                    "open a new file", "start a new file", "create an empty file", "make an empty file", "i need a file", "create a text file", "make a text file",
                                    "mere liye ek file banao", "ek new file create karo", "file banao", "nayi file banao", "ek file bana do"]:
                    speak("Yes absouletly i can create a file for you!. You wants to create a empty file or you wants to add some data?")

                    print("Listening your choice")
                    with sr.Microphone() as source:
                        audio = r.listen(source)
                    user_choice = r.recognize_google(audio).strip()
                    print("You choice:",user_choice)

                    if user_choice in ["i want empty file", "yes I want empty file"]:
                        speak("Sure sir! now i am creating your empty file")
                        f = open("empty_file_1", "w")
                        f.write(user_choice)
                        speak("Your file is created successfully")
                        continue

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
                        continue

                #---- Till here only file: txt and csv codes are here ----#

                    
                    

                #-------------------- Social Media Links Handling-------------------------

                    user_text = ""
                    
                links = {
                    "youtube": "https://www.youtube.com", "instagram": "https://www.instagram.com", "facebook": "https://www.facebook.com", "twitter": "https://www.twitter.com", "linkedin": "https://www.linkedin.com",
                    "github": "https://www.github.com", "reddit": "https://www.reddit.com", "pinterest": "https://www.pinterest.com", "snapchat": "https://www.snapchat.com", "tiktok": "https://www.tiktok.com",
                    "whatsapp": "https://web.whatsapp.com", "telegram": "https://web.telegram.org", "discord": "https://discord.com", "quora": "https://www.quora.com", "tumblr": "https://www.tumblr.com",
                    "medium": "https://medium.com", "stackoverflow": "https://stackoverflow.com", "wikipedia": "https://www.wikipedia.org", "amazon": "https://www.amazon.com", "flipkart": "https://www.flipkart.com",
                    "ebay": "https://www.ebay.com", "netflix": "https://www.netflix.com", "primevideo": "https://www.primevideo.com", "hotstar": "https://www.hotstar.com", "spotify": "https://www.spotify.com",
                    "apple": "https://www.apple.com", "microsoft": "https://www.microsoft.com", "google": "https://www.google.com", "yahoo": "https://www.yahoo.com", "bing": "https://www.bing.com",
                    "duckduckgo": "https://duckduckgo.com", "openai": "https://www.openai.com", "chatgpt": "https://chat.openai.com", "canva": "https://www.canva.com", "figma": "https://www.figma.com",
                    "coursera": "https://www.coursera.org", "udemy": "https://www.udemy.com", "edx": "https://www.edx.org", "khanacademy": "https://www.khanacademy.org", "codecademy": "https://www.codecademy.com",
                    "leetcode": "https://leetcode.com", "hackerrank": "https://www.hackerrank.com", "geeksforgeeks": "https://www.geeksforgeeks.org", "w3schools": "https://www.w3schools.com", "replit": "https://replit.com",
                    "notion": "https://www.notion.so", "trello": "https://trello.com", "zoom": "https://zoom.us", "meet": "https://meet.google.com", "dropbox": "https://www.dropbox.com","razorpay":"https://razorpay.com", "coinbase":"https://www.coinbase.com", "binance":"https://www.binance.com", 
                    "githubgist":"https://gist.github.com", "gitlab":"https://gitlab.com", "bitbucket":"https://bitbucket.org", "sourceforge":"https://sourceforge.net", "npm":"https://www.npmjs.com",
                    "pypi":"https://pypi.org", "docker":"https://hub.docker.com", "huggingface":"https://huggingface.co", "kaggle":"https://www.kaggle.com", "colab":"https://colab.research.google.com",
                    "codepen":"https://codepen.io", "jsfiddle":"https://jsfiddle.net", "codesandbox":"https://codesandbox.io", "glitch":"https://glitch.com", "vercel":"https://vercel.com",
                    "netlify":"https://www.netlify.com", "render":"https://render.com", "railway":"https://railway.app", "heroku":"https://www.heroku.com", "firebase":"https://firebase.google.com",
                    "supabase":"https://supabase.com", "mongodb":"https://www.mongodb.com", "mysql":"https://www.mysql.com", "postgresql":"https://www.postgresql.org", "sqlite":"https://sqlite.org",
                    "oracle":"https://www.oracle.com", "digitalocean":"https://www.digitalocean.com", "aws":"https://aws.amazon.com", "azure":"https://azure.microsoft.com", "cloudflare":"https://www.cloudflare.com",
                    "brave":"https://brave.com", "opera":"https://www.opera.com", "mozilla":"https://www.mozilla.org", "firefox":"https://www.mozilla.org/firefox", "chromium":"https://www.chromium.org",
                    "vivaldi":"https://vivaldi.com", "tor":"https://www.torproject.org", "protonmail":"https://proton.me", "icloud":"https://www.icloud.com", "outlook":"https://outlook.live.com",
                    "yandex":"https://yandex.com", "ask":"https://www.ask.com", "ecosia":"https://www.ecosia.org", "aol":"https://www.aol.com", "baidu":"https://www.baidu.com","zerodha":"https://zerodha.com", "groww":"https://groww.in",
                    "naver":"https://www.naver.com", "vk":"https://vk.com", "weibo":"https://weibo.com", "line":"https://line.me", "wechat":"https://www.wechat.com",
                    "behance":"https://www.behance.net", "dribbble":"https://dribbble.com", "deviantart":"https://www.deviantart.com", "pixabay":"https://pixabay.com", "pexels":"https://www.pexels.com",
                    "unsplash":"https://unsplash.com", "freepik":"https://www.freepik.com", "shutterstock":"https://www.shutterstock.com", "adobe":"https://www.adobe.com", "photoshop":"https://www.adobe.com/products/photoshop",
                    "airbnb":"https://www.airbnb.com", "booking":"https://www.booking.com", "tripadvisor":"https://www.tripadvisor.com", "makemytrip":"https://www.makemytrip.com", "goibibo":"https://www.goibibo.com",
                    "expedia":"https://www.expedia.com", "uber":"https://www.uber.com", "ola":"https://www.olacabs.com", "zomato":"https://www.zomato.com", "swiggy":"https://www.swiggy.com",
                    "paytm":"https://paytm.com", "phonepe":"https://www.phonepe.com", "gpay":"https://pay.google.com", "paypal":"https://www.paypal.com", "stripe":"https://stripe.com",
                    
                                    }

                if 'open' in user_text:
                    for site in links:
                        if site in user_text:
                            speak(f"Opening {site}")
                            webbrowser.open(links[site]) 
                
                #-----------------------------------------------------------------------------

                #------------- Handling jsonl dataset ----------------------#           
                found = False
                dataset = []
                with open("Dataset/01_dataset.jsonl", "r") as file:
                    for line in file:
                        data = json.loads(line)

                        if data["prompt"].lower() == user_text.lower():
                            speak(data["response"])
                            found = True
                            break

                    else:
                        speak("I don't know about this yet!")
    
                #------------------------------------------------------------#                
                

        except sr.UnknownValueError:
            print("I'm unable to hear your voice! Please say louder.")
        except sr.RequestError:
            print("No internet connection, check your internet!")
        

            
