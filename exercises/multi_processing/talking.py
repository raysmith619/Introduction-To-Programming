# talking   14Oct2023  crs, Author
""" Simple example of text to speech
module pyttsx3 or pyttsx4
"""
import pyttsx3 as pyttsxN

engine = pyttsxN.init()
            
def talk(text):
    """ Say text
    """
    engine.say(text)
    engine.runAndWait()
    
if __name__ == "__main__":
    talk("Hello World")
    #talk("How are you?")
    #talk("How's the weather?")
    talk("Good Bye for now.")