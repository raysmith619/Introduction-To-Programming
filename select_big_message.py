# select_big_message.py
import tkinter
from tkinter import messagebox
class BigMessage:
    
    def __init__(self, title, message):
        self.mb  = messagebox.showinfo(title, message)
        
        
if __name__ == "__main__":
    # hide main window
    root = tkinter.Tk()
    root.withdraw()
    bb = BigMessage("Hi Decklan", "It's your turn")
            