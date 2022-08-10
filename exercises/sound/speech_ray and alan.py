#speach_123.py
import pyttsx3
engine = pyttsx3.init()
#engine.say("How are you today Ray and Alan and Candy")
engine.say("123 4356 89 1,231,234,567")
engine.setProperty('rate',40)
engine.setProperty('volume', 0.9)
engine.runAndWait()
