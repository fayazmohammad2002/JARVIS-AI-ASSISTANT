import pyttsx3 #pyttsx3 is package used to convert msg to speech
import datetime #gets time and date dynamically
import speech_recognition as sr #used to recogize speech through mic
import wikipedia # it is used fetch info from wikipedia and summarize it
import smtplib
import webbrowser as web
import os 
import pyjokes
import pyautogui
import psutil
import requests
from bs4 import BeautifulSoup
import openai

# data = input("enter text which you want ot convert to speech:\n")
openai.api_key=""#place your chatgpt api key in ""


engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# speak("this is a python generated ai assistant")

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
# time()
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)
# date()
def wishme():
    speak("Welcome back sir!")
    #time()
    #date()
    hour = datetime.datetime.now().hour

    # if hour>=6 and hour<12:
    #     # speak("Good mornining sir!")
    # elif hour >=12 and hour < 18:
    #     # speak("Good afternoon sir!")
    # elif hour>=18 and hour <24:
    #     # speak("Good evening sir!")
    # else:
    #     # speak("Good Night sir !")
    speak("this is python generated ai assistant at your service. Please tell me how can i help you sir?")
# wishme()
# import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return ""

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('192.168.12.12',12345)
    server.ehlo()
    server.starttls()
    server.login('MAIL ID','*PASSWORD')
    server.sendmail('201fa04035@gmail.com',to,content)
    server.close()

def jokes():
    joke = pyjokes.get_joke()
    speak(joke)
    print(joke)

def screenshot():
    img = pyautogui.screenshot()
    img.save(".\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+ usage)
    battery = psutil.sensors_battery()
    speak("battery is at ")
    speak(battery.percent)


def generate(prompt):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 500,
        n = 1,
        stop = None,
        temperature = 0.5,
    )
    print(response["choices"][0]["text"])
    return response["choices"][0]["text"]


def find():
    try:
        speak("what should i search")
        data = takeCommand().lower()
        res = generate(data)
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        with open(f"Openai/{''.join(data)}.txt","w") as f:
            f.write(res)

        speak(res)
        # res = wikipedia.summary(res,sentences=2)
        print(res)
    except Exception as e:
        print(e)
        speak("sorry no results found, please be clear")


# takeCommand()
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'email' in query:
            try:
                speak("what should I say ?")
                content = takeCommand()
                to = 'receiver mail id'
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send email")
                print("unable to send email")

        elif 'browser' in query:
            speak("What should i search ?")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            web.get(chromepath).open_new_tab(search + '.com')

        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir ='D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'joke' in query:
            jokes()        

        elif 'stop' in query:
            quit()

        elif 'remember that' in query:
            speak('what should i remember ?')
            data = takeCommand()
            speak("you said me to remember that "+data)
            remember = open('data.txt' , 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you said me to remember that"+ remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")

        elif 'cpu details' in query:
            cpu()

        elif 'google' in query:
            find()

        elif 'open' in query:
            website_links = {    'Google'.lower(): 'https://www.google.com',
                                'Facebook'.lower(): 'https://www.facebook.com',
                                'YouTube'.lower(): 'https://www.youtube.com',
                                'Twitter'.lower(): 'https://www.twitter.com',
                                'Instagram'.lower(): 'https://www.instagram.com',
                                'LinkedIn'.lower(): 'https://www.linkedin.com',
                                'Reddit'.lower(): 'https://www.reddit.com',
                                'Pinterest'.lower(): 'https://www.pinterest.com',
                                'Amazon'.lower(): 'https://www.amazon.com',
                                'Netflix'.lower(): 'https://www.netflix.com',
                                'Wikipedia'.lower(): 'https://www.wikipedia.org',
                                'Ebay'.lower(): 'https://www.ebay.com',
                                'Tumblr'.lower(): 'https://www.tumblr.com',
                                'Yahoo'.lower(): 'https://www.yahoo.com',
                                'CNN'.lower(): 'https://www.cnn.com',
                                'GitHub'.lower(): 'https://www.github.com',
                                'Stack Overflow'.lower(): 'https://stackoverflow.com',
                                'WordPress'.lower(): 'https://wordpress.com',
                                'Quora'.lower(): 'https://www.quora.com',
                                'Dropbox'.lower(): 'https://www.dropbox.com'
                            }
            app = ''.join(query.split('open')[1:]).strip()
            web.open(website_links[app])
        elif 'who are you' in query:
            remember = open('data1.txt' , 'r')
            speak(remember.read())