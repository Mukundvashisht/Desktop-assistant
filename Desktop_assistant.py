import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
#from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)
#engine.setProperty('rate',170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning sir!")
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        print("Good Afternoon sir!")
        speak("Good Afternoon sir!")   

    else:
        print("Good Evening sir!")
        speak("Good Evening sir!")  

    print("I am HP. How can I help you?")
    speak("I am HP. How can I help you?")       


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-us')
        #if ("HP") in query:
        print(f"You said: {query}\n")
        #else:
            #return "None"

    except Exception as e:
        print(e)    
        print("Sorry sir, I don't understand")  
        speak("Sorry sir, I don't understand")  
        return "None"
    return query

#def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mukundvashisht3@gmail.com', 'mukund557')
    server.sendmail('mukundvashisht3@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)  
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open("https://google.com")

        elif 'open stack overflow' in query:
            webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open("https://stackoverflow.com")   

        elif 'open gfg' in query:
            webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open("https://www.geeksforgeeks.org")   

        #elif 'open gmail' in query:
            #webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open("https://accounts.google.com/b/0/AddMailService")   


        elif 'play music' in query:
            n=random.randint(0,3)
            #print(n)
            music_dir = r'C:\Users\mukun\Music\Music'
            songs = os.listdir(music_dir)
            #print(songs)    
            os.startfile(os.path.join(music_dir,songs[n]))
            print("playing music")
            speak("playing music")
            break

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'open Visual Studio' in query:
            codePath = r"E:\Microsoft VS Code\Code.exe "
            speak("opening...")
            os.startfile(codePath)
            
            
        elif 'open python 310' in query:
            codePath =r"C:\Users\mukun\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10\IDLE (Python 3.10 64-bit)"
            speak("opening...")
            os.startfile(codePath)
        

        elif 'open python 38' in query:
            codePath =r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.8\IDLE (Python 3.8 64-bit)"
            speak("opening...")
            os.startfile(codePath)
            

        elif 'open edge' in query:
            codePath ="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            speak("opening...")
            os.startfile(codePath)
            

        #elif 'open chrome' in query:
            #codePath ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            #speak("opening...")
            #os.startfile(codePath)
            

        elif 'open control panel' in query:
            codePath ="C:\\Users\\mukun\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk"
            speak("opening...")
            os.startfile(codePath)

        elif 'open screen recorder' in query:
            codePath ="E:\\OBS\\obs-studio\\bin\\64bit\\obs64.exe"
            speak("opening...")
            os.startfile(codePath)
            
            
        #elif 'send a mail' in query:
        #    try:
        #       speak("what should I say...")
        #        content = takeCommand()
        #       to = ("mukundvashisht3@gmail.com")    
        #       sendEmail(to, content)
        #        speak("Email has been sent!")
        #    except Exception as e:
        #        print(e)
        #       speak("Sorry sir, email not sent")

        elif 'exit' in query:
            print("Exiting...")
            speak("Exiting...")
            break

        elif 'take a break' in query:
            print("Ok sir, if need any help you can call me")
            speak("Ok sir, if need any help you can call me")
            print("I am there for you")
            speak("I am there for you")
            break

        elif 'youtube search' in query:
            print("ok sir, This is what I found")
            speak("ok sir, This is what I found")
            query=query.replace("youtube search","")
            web='https://www.youtube.com/results?search_query='+query
            webbrowser.open(web)
            speak("Done Sir")


        elif 'google search' in query:
            print("ok sir, This is what I found")
            speak("ok sir, This is what I found")
            query=query.replace("google search","")
            web='https://www.google.com/search?q='+query
            webbrowser.open(web)
            speak("Done Sir")
