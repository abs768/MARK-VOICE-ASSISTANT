import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from requests import get  #importing get function from requests
import pywhatkit as kit
import sys
from pywikihow import search_wikihow

MASTER=" Sir BHAVANI SHANKAR " 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)
        print("Good Morning" + MASTER)
        
    elif hour>=12 and hour<17:
        speak("Good Afternoon" + MASTER)
        print("Good Afternoon" + MASTER)
        
    elif hour>=17 and hour<21:
        speak("Good Evening" + MASTER)
        print("Good Evening" + MASTER)
    else:
        speak("Good Night" + MASTER)
        print("Good Night" + MASTER)

    speak("I am Mark . Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your password')
    server.sendmail('anotheremail@gmail.com', to, content)
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
            
            
        elif 'thank you' in query:
            speak('Welcome..')
            
        
        elif 'open command prompt' in query:
            os.system("start cmd")
            
         
        elif 'open google' in query:
            url="google.com"
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)  
            
             
        elif 'open youtube' in query:
            url="youtube.com"
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
        
        elif 'open spotify' in query:
            url="https://open.spotify.com/?_ga=2.44898663.231215960.1646213540-1861760272.1646213540"
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
            
        
        elif 'activate how to do mode' in query:
            #from wikihow import search_wikihow..
            
            speak("How to do mode is activated")
            while(True):
                speak("please tell me what do you want to know")
                how=takeCommand()
                try:
                    if 'exit' in how or 'close' in how:
                        speak("Okay ma'am, how to do mode is closed")
                        break
                    else:
                        max_results=1
                        how_to = search_wikihow(how,max_results)
                        assert len(how_to)==1
                        how_to[0].print()
                        speak(how_to[0].summary)
                        
                except Exception as e:
                    speak("Sorry ma'am! I'm not able to find this")
        
        
        
        elif "send message" in query:
            kit.sendwhatmsg("+919871954506","hi tapan! kaise ho bhai coding mast chalrahi kya",21,57)
            
        elif 'open geeksforgeeks' in query:
            url="geeksforgeeks.org"
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)

        elif 'google search' in query:
            import wikipedia as googleScrap
            query= query.replace("David","")
            query= query.replace("google search","")
            query=query.replace("google","")
            speak("This is what i have Found!")
            kit.search(query)
            
            try:
                result=googleScrap.summary(query, sentences=2)
                speak(result)
            
            except:
                speak("No spekable data available!")
                
                
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open instagram' in query:
            url="instagram.com"
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
        
        elif 'open whatsapp' in query:
            url="web.whatsapp.com"
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(url)
        
        elif 'play a song on youtube' in query:
            kit.playonyt("light switch")

        elif 'email to jk' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "abs768shank@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak(f"Sorry my friend {MASTER}. I am not able to send this email")
        
        elif 'no thanks' in query:
           speak("thanks for using me Sir, had a good time talking to you")
           sys.exit()
        speak("Sir! Do you have any other work")

