# makeentry.py    07Mar2019  crs
"""
Simple input example
"""
from tkinter import *

def okcmd(entry):
    print("ok got", entry)
    
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    button = Button(parent, text="OK", command=okcmd)
    return entry

top = Tk()
user_entry = makeentry(top, "User name:", 10)
password_entry = makeentry(top, "Password:", 10, show="*")
user = user_entry.get()
password = password_entry.get()
print("user=%s password=%s" % (user, password))