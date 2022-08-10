#speach_123.py
import pyttsx3
engine = pyttsx3.init()
engine.say("How are you today Alex and Declan?")
engine.say("Maybe Avery and Charlie will come over one day soon")
engine.setProperty('rate',120)
engine.setProperty('volume', 0.9)
engine.runAndWait()
