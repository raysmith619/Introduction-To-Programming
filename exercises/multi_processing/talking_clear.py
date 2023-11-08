# talking_clear.py   14Oct2023  crs, Author
""" Simple example of text to speech
module pyttsx3 or pyttsx4
with queued entries using multiprocessing
Supporting clear to stop pending
plus current uterance.
"""
import multiprocessing as mp
import pyttsx4 as pyttsxN

class Talking:
    def __init__(self, qlen=10):
        """ Setup for queued talking
        :qlen: input/output queue length
                default: 10
        """
        self.qlen = qlen
        self.setup_proc()

    def setup_proc(self):
        self.pyt_proc = mp.Process(target=self.pyt_proc_proc)
        self.pyt_queue = mp.Queue(self.qlen)  # speech queue of SpeakerControlCmd 

        # Output queue provides engine status
        self.pyt_out_queue = mp.Queue(self.qlen)
        self.pyt_engine_busy = False   # Updated with status 
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
        if self.pyt_proc is None:
            self.setup_proc()
        self.pyt_queue.put(text)
        
    def do_talk(self, text):
        """ do talking, waiting till done
        :text: text to say
        """
        self.pyt_out_queue.put(True)    # engine status
        self.engine.say(text)
        self.engine.runAndWait()
        self.pyt_out_queue.put(False)
    
    def clear(self):
        """ Stop pending plus
        current utterance
        """
        if self.pyt_proc is None:
            return
        
        self.pyt_proc.kill()
        self.pyt_proc.join()
        self.pyt_proc = None
            
    def quit(self):
        """ Quit talking
        """
        self.wait_while_busy()
        self.clear()
        
    def wait_while_busy(self):
        while True:
            if not self.is_busy():
                break

    def is_busy(self):
        """ Check if busy talking or
        getting ready to talk
        """
        if self.pyt_queue.qsize()>0:
            return True

        while self.pyt_out_queue.qsize() > 0:
            self.pyt_engine_busy = self.pyt_out_queue.get()
        return self.pyt_engine_busy
            
if __name__ == "__main__":
    import time
    
    tt = Talking()
    tt.talk("Hello World")
    tt.talk("How are you?")
    for i in range(8):  # in parallel with talking
        print(i, "\a")
        time.sleep(.25)
    tt.talk(" ".join([str(i) for i in range(100,0,-1)]))
    time.sleep(4)
    tt.clear()      # Stop talking in mid-utterance
    tt.talk("After clear")
    tt.talk("Good Bye for now.")
    tt.quit()       # Stop talking process
    print("End of Test")
