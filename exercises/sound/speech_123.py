#speach_123.py
import pyttsx3
engine = pyttsx3.init()
engine.say("12,34,567,8,9,10")
engine.say("1+9=10")
engine.say("How are you today Alex and Declan?")
engine.setProperty('rate',120)
engine.setProperty('volume', 0.9)
engine.runAndWait()
