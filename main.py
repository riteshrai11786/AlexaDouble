import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from datetime import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def send_whatsAppMsg(text):
    phone_number = text.split("to ", 1)[1]
    phone_number = "+91" + phone_number.split("that ", 1)[0]
    phone_number = phone_number.replace(" ", "")
    my_msg = text.split("that ", 1)[1]
    time_now = datetime.now()
    #pywhatkit.sendwhatmsg('+917702677997', text, time_now.hour, time_now.minute + 1)
    print(text)
    print(phone_number)
    print(my_msg)
    pywhatkit.sendwhatmsg(phone_number, my_msg, time_now.hour, time_now.minute + 2)


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'whatsapp' in command:
        whatsapp_msg = command.replace('send whatsapp message', '')
        send_whatsAppMsg(whatsapp_msg)
    elif 'stop' in command:
        talk('Thank You! Bye bye!')
        exit(0)
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
