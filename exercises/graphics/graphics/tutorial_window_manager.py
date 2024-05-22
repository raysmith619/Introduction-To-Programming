# tutorial_window_manager.py  12Aug2021  crs IDLE tutorial
"""

 Python »
 3.9.4 Documentation » 
 The Python Standard Library »
 Graphical User Interfaces with Tk »
 
The Window Manager
Here are some examples of typical usage:
"""

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

# start the program
myapp.mainloop()

