import speech_recognition as sr  # recognise speech
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import random
from time import ctime  # get time details
import webbrowser  # open browser
import ssl
import certifi
import time
import os  # to remove created audio files
from PIL import Image
import subprocess
import pyautogui  # screenshot
import pyttsx3
import bs4 as bs
import urllib.request


class person:
    name = ''

    def setName(self, name):
        self.name = name


class asis:
    name = ''

    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()  # initialise a recogniser
# listen for audio and convert it to text:


def record_audio(ask=""):
    with sr.Microphone() as source:  # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(
                audio, language="ro-RO")  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            # error: recognizer is not connected
            engine_speak('Sorry, the service is down')
        print(">>", voice_data.lower())  # print what user said
        return voice_data.lower()

# get string and make a audio file to be played


def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='ro')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print(asis_obj.name + ":", audio_string)  # print what app said
    os.remove(audio_file)  # remove audio file


def respond(voice_data):
    # 1: greeting
    if there_exists(['hey', 'hi', 'hello', 'buna']):
        greetings = ["hey, ce faci iubire" + person_obj.name, "hey, iubi?" + person_obj.name,
                     "ascult" + person_obj.name, "cu ce te pot ajuta?" + person_obj.name, "buna" + person_obj.name]
        greet = greetings[random.randint(0, len(greetings)-1)]
        engine_speak(greet)

    # 2: name
    if there_exists(["care este numele tau", "cum te numești", "spunemi numele tau"]):
        if person_obj.name:
            engine_speak("numele meu este " + asis_obj.name)
        else:
            engine_speak("nustiu numele meu . Care e numele tau?")

    if there_exists(["mă numesc"]):
        person_name = voice_data.split("numesc")[-1].strip()
        engine_speak(
            "okay, o sa imi aduc aminte numele tau iubitul meu " + person_name)
        person_obj.setName(person_name)  # remember name in person object

    if there_exists(["numele tău este"]):
        asis_name = voice_data.split("este")[-1].strip()
        engine_speak("okay, o sa imi aduc aminte ca ma numesc " + asis_name)
        asis_obj.setName(asis_name)  # remember name in asis object

    # 3: greeting
    if there_exists(["ce faci", "ce ai de gand sa faci"]):
        engine_speak("Sunt bine iubire " + person_obj.name)

    # 3-1: love
    if there_exists(["ma iubesti", "mă iubești"]):
        engine_speak(
            "Cum poți să mă întrebi așa ceva? Bineînţeles ca te iubesc iubirea mea")

    # 4: time
    if there_exists(["cât e ceasul", "spunemi cât e ceasul", "ce ora este"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minute"
        engine_speak(time)

    # 5: search google
    if there_exists(["cauta pe"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("pe")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Asta e ce am gasit Dragoste " +
                     search_term + " pe google")

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("pe")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Asta e ce am gasit Dragoste " +
                     search_term + " pe youtube")

     # 7: get stock price
    if there_exists(["pretul pentru"]):
        search_term = voice_data.split("pentru")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Asta e ce am gasit Dragoste " +
                     search_term + " pe google")

     # 8 time table
    if there_exists(["show my time table"]):
        im = Image.open(r"D:\WhatsApp Image 2019-12-26 at 10.51.10 AM.jpeg")
        im.show()

     # 9 weather
    if there_exists(["vremea", "spunemi vremea"]):
        search_term = voice_data.split("pentru")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Asta e ce am gasit pe google Dragoste")

     # 10 stone paper scisorrs
    if there_exists(["joc"]):
        voice_data = record_audio("alege piatra foarfeca sau hartie")
        moves = ["piatra", "hartie", "foarfeca"]

        cmove = random.choice(moves)
        pmove = voice_data

        engine_speak("Eu am ales " + cmove)
        engine_speak("tu ai ales " + pmove)
        # engine_speak("hi")
        if pmove == cmove:
            engine_speak("egalitate")
        elif pmove == "piatra" and cmove == "foarfeca":
            engine_speak("Ai castigat iubire")
        elif pmove == "piatra" and cmove == "paper":
            engine_speak("Am castigat")
        elif pmove == "hartie" and cmove == "piatra":
            engine_speak("Ai castigat iubire")
        elif pmove == "hartie" and cmove == "foarfeca":
            engine_speak("Am castigat")
        elif pmove == "foarfeca" and cmove == "hartie":
            engine_speak("Ai castigat iubire")
        elif pmove == "foarfeca" and cmove == "piatra":
            engine_speak("Am castigat")

     # 11 toss a coin
    if there_exists(["toss", "flip", "coin"]):
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        engine_speak("The computer chose " + cmove)

     # 12 calc
    if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(
                int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(
                int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(
                int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(
                int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(
                int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")

     # 13 screenshot
    if there_exists(["capture", "my screen", "screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('D:/screenshot/screen.png')

     # 14 to search wikipedia for definition
    if there_exists(["definition of"]):
        definition = record_audio("what do you need the definition of")
        url = urllib.request.urlopen(
            'https://en.wikipedia.org/wiki/'+definition)
        soup = bs.BeautifulSoup(url, 'lxml')
        definitions = []
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak(
                    'im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                engine_speak('here is what i found '+definitions[1])
            else:
                engine_speak('Here is what i found '+definitions[2])
        else:
            engine_speak(
                "im sorry i could not find the definition for "+definition)

    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("bye")
        exit()


time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'kiki'
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Ascult")  # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data)  # respond
