"""
                                  M&T AI 
Version: 1.0.1

                                                        developed by M&T Developers 
                                                        Copyright (c) 2020 M&T 
                                                        Licensed under MIT
"""

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
import  mysql.connector as sqltor
conn = sqltor.connect(host='localhost', user='root', password='mysql', database='iduli')
cursor  =  conn.cursor ()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("good afternoon Sir")
    else :
        speak("Good Evening Sir ")
    speak("I am Chintu sir. Please tell me how may i help you")




def takeCommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening sir...")
        r.pause_threshold=1 
        audio=r.listen(source,timeout=7,phrase_time_limit=5)
    try:
        print("Recognizing Sir...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}")
    except sr.UnknownValueError:
        speak('Sorry sir!I did not get that! Try typing the command!')
        query=str(input('Command:'))
        
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('taher13j@gmail.com','taher/781')
    server.sendmail('chikujhabuawala@gmail.com',to,content)
    server.close()



if __name__ =="__main__":
    wishMe()
    #while True:
    if 1:
        query=takeCommand().lower()

#logix for executing tasks basd on query
#search wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
#open YT       
        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")
#open google       
        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")
#open stackoverflow        
        elif 'open stackoverflow' in query:
            webbrowser.get(chrome_path).open("stackoverflow.com")
#play music       
        elif 'play music' in query:
            music_loc='C:\\Users\\Iduli\\Music\\Playlists'
            songs=os.listdir(music_loc)
            print(songs)
            os.startfile(os.path.join(music_loc,songs[1]))
#show time       
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
#vscode open       
        elif "open code" in query:
            pathcode="C:\\Users\\Iduli\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(pathcode)
        
#not sure
        elif "show task" in query:
            print(showtask())

        #random message
        elif 'are you there' in query:
            msgs=['At your service , Sir']
            speak(msgs)
        
        #search
        elif 'what is' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

#search for
        elif 'search for ' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

#Shutdown pc
        elif 'shutdown the pc' in query:
            choice=input("please confirm to shutdown the pc(y or n)")
            if choice=='n':
                exit()
            else:
                os.system("shutdown /s /t 1")
            
#EXIT AI
        elif 'exit' in query:
            sys.exit(speak("Ok sir ,Take Care"))
            
#Email
        elif "email to chiku" in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="chikujhabuawala@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except sr.UnknownValueError:
                speak('Sorry sir!I did not get that! Try typing the body!')
                query=str(input('Body:'))

        print(query)
        cursor.execute("INSERT INTO query(user_asked_for) VALUES (%s);", (query,))
        conn.commit()
def showtask():
    print("""
+---------------------------------+---------------------------------+
|                         Task AI can Perform                       |                          
|                         -------------------                       |                                
|                                                                   |                                                   
| COMMANDS FOR AI Program:                                          |                                                   
|                                                                   |                                                   
| wikipedia          > Search for given data in wikipedia.          |                                                   
| open youtube       > It opens youtube in chrome.                  |                                                   
| open google        > It opens Google chrome.                      |                                                   
| open stackoverflow > It opens stackoverflow.com.                  |                                                  
| play music         > It plays music from the device.              |                                                                                           |
| time               > Return the current time.                     |
| email to @         > Email's to the recipient                     |
|___________________________________________________________________|
|___________________________________________________________________|
""")                                                                        