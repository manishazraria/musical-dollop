import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import os
import pyautogui #pip instal pyautogui
import random
import wolframalpha #pip install wolframalpha




engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S") #for 12 hour clock
    speak("The current time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back Manish Azraria!")
    time_()
    date_()

#greetings

hour = datetime.datetime.now().hour

if hour>=6 and hour<12:
    speak("Good Morning Manish")
elif hour>=12 and hour<18:
    speak("Good Afternoon Manish")
elif hour>=18 and hour<24:
    speak("Good Evening Manish")
else:
    speak("Good night Manish")

speak("Aggarwal aapki service mei haazeer hai. please tell me how can i help you")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #for this function You must enable low Security in Your Gmail which You are going to use as sender

    server.login('manishazraria@gmail.com','manishazrariasheetalqwe123r45t67y89u0')
    server.sendmail('manishazraria@gmail.com',to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/manis/Pictures/AI/screenshot.png')    


def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at'+usage)

    battery = psutil.sensors_battery()
    speak('battery is at')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())     


if __name__ == "__main__":
    
     wishme()

     while True:
         query = TakeCommand().lower()


         if 'time' in query:
             time_()

         if 'date' in query:
             date_()
         
         elif 'wikipedia' in query:
             speak("Searching...")
             query=query.replace('wikipedia','')
             result=wikipedia.summary(query,sentences=3)
             speak('According to wikipedia')
             print(result)
             speak(result)    
         
         elif 'send email' in query:
            try:
                 speak("what should i say?")
                 content=TakeCommand()
                 #provide reciever email address

                 speak("who is the reciever?")
                 reciever=input("Enter reciever's email : ")
                 to = reciever
                 sendEmail(to,content)
                 speak(content)
                 speak("email has been sent")

            except Exception as e:
                 print(e)
                 speak("unable to send email.")

         
         elif 'search in chrome' in query:
             speak('what should i search')
             chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
             #chromepath is location of chrome's installation on computer

             search = TakeCommand().lower()
             wb.get(chromepath).open_new_tab(search+'.com') #only open those websites which ends with '.com'
         
         
         elif 'search youtube' in query:
             speak('what should i search')
             search_Term = TakeCommand().lower()
             speak("here we go to youtube!")
             wb.open('https://www.youtube.com/results?search_query='+search_Term)
         
         elif 'search in google' in query:
             speak('what should i search')
             search_Term = TakeCommand().lower()
             speak("here we go")
             wb.open('https://www.google.com/search?q='+search_Term)
         
         
         elif 'cpu' in query:
             cpu()
         
         elif 'joke' in query:
             joke()
         
         elif 'go offline' in query:
             speak('going offline sir')
             quit()
         
         elif 'word' in query:
             speak('opening ms word')
             ms_word = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013'
             os.startfile(ms_word)
         
         elif 'write a note' in query:
             speak('what should i write, sir?')
             notes = TakeCommand()
             file = open('notes.txt','w')
             speak('should i include date and time?')
             ans = TakeCommand()
             if 'yes' in ans or 'sure' in ans:
                 strTime = datetime.datetime.now().strftime("%H:%M:%S")
                 file.write(strTime)
                 file.write(':-')
                 file.write(notes)
                 speak('Done taking notes')
             else:
                 file.write(notes)
         
         elif 'read notes' in query:
             speak('reading notes')
             file = open('notes.txt','r')
             speak(file.read())
             print(file.read())
         
         elif 'take screenshot' in query:
             screenshot()
             speak('screenshot has been taken')

         elif 'play music' in query:
             songs_dir = 'C:/Users/manis/Downloads/Video'
             music = os.path.join(songs_dir)
             speak('what should i play?')
             speak('select a number')
             ans = TakeCommand().lower()
             if 'number' in ans:
                 no = int(ans.replace('number',''))
             elif 'random' or 'you choose' in ans:
                 no = random.randint(1,100)

             os.startfile(os.path.join(songs_dir,music[no]))

             
                 



                  









    