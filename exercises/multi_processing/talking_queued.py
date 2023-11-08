# talking_queued   14Oct2023  crs, Author
""" Simple example of text to speech
module pyttsx3 or pyttsx4
with queued entries using multiprocessing
"""
import multiprocessing as mp

import pyttsx4 as pyttsxN

class Talking:
    def __init__(self):
        """ Setup for queued talking
        """
        self.pyt_queue = mp.Queue(10)  # speech queue of SpeakerControlCmd 
        self.pyt_proc = mp.Process(target=self.pyt_proc_proc)
        self.pyt_proc.start()

            
    def pyt_proc_proc(self):
        """ Process pending talk requests
        """
        self.engine = pyttsxN.init()
        while True:
            text = self.pyt_queue.get()
            self.do_talk(text)
            
    def talk(self, text):
        """ Say text
        :text: text to speak
        """
        self.pyt_queue.put(text)
        
    def do_talk(self, text):
        """ do talking, waiting till done
        :text: text to say
        """
        self.engine.say(text)
        self.engine.runAndWait()
    
    def quit(self):
        """ Quit talking
        """
        self.pyt_proc.kill()
        self.pyt_proc.join()
    
if __name__ == "__main__":
    import time
    
    tt = Talking()
    tt.talk("Hello World")
    tt.talk("How are you?")
    for i in range(8):  # In parallel with talking
        print(i, "\a")
        time.sleep(.25)
    tt.talk("How's the weather?")
    time.sleep(2)
    tt.talk("Good Bye for now.")
    time.sleep(4)
    tt.quit()
    print("End of Test")
