import warnings
import pyttsx3
import speech_recognition as sr
import random


warnings.filterwarnings("ignore")

engine = pyttsx3.init()

voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female


def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def rec_audio():
    # to pickup our voice and return as text data
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening")
        audio = recog.listen(source)
        data = " "
    try:
        data = recog.recognize_google(audio)
        print("Your said" + data)
    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    except sr.RequestError as ex:
        print("Google could not understand the request" + ex)
    return data

def call(text):

    action_call = "assistant"

    text = text.lower()

    if action_call in text:
        return True

    return False


def say_hello(text):
    greet = ["hai", "hi", "hey", "hola", "greetings", "massup", "hello", "howdy", "what's good", "hey there"]

    response = ["hi", "hey", "hola", "greetings", "massup", "hello", "howdy", "what's good", "hey there"]


    for word in text.split():
        if word.lower() in greet:
            talk(random.choice(response) + ".")

    tocontinue = True

    while tocontinue:
        text = rec_audio()
        if "who are you" in text or "are you" in text or "define you" in text:
            talk("I am Domino's voice assistant")
        elif "how about you" in text or "how do you do" in text:
            talk("I am fine" + "\n how about you")
        elif "I am ok" in text or "I'm ok" in text or "I'm fine" in text or "OK I'm fine" in text:
            talk("OK would you like to order pizza")
            tocontinue = False
        else:
            text = "no"
    return text


def say_bye(text):
    action_end = ["no", "thanks", "thank you", "bi", "bye", "no thanks", "sorry", "sorry not now"]
    response = ["welcome", "you are welcome", "most welcome"]

    for word in text.split():
        if word.lower() in action_end:
            return random.choice(response) + " . "

    return " "






