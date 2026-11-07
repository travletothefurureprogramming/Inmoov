import pyttsx4

engine = pyttsx4.init()

def speak(text:str):
    engine.say(text)
    engine.runAndWait()    