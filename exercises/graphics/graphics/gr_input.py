# gr_input.py   12Aug2021   crs, Catch Return/ENTRY
#               07Mar2019   crs Author
"""
Prompt User and accept input
"""
from tkinter import *       # Get all tkinter functions

def gr_input(prompt="Enter"):
    global entry_var, entry_text
    mw = Tk()
    entry_var = StringVar()         # Holds the entry text
    entry_text = None               # Set if OK
   
    def ok_cmd():
        """ Function called  upon "OK" button
        """
        global entry_text
        entry_text = entry_var.get()    # Retrieve
        mw.quit()                       # Exit tk mainloop
        
    def return_process(event):
        ###print("Processing <Return>")
        ok_cmd()
        
    label = Label(mw, text=prompt)    # Create Label with prompt
    label.pack(side=LEFT)

    entry = Entry(mw, textvariable=entry_var, bd=3) # Create Entry space on right
    entry.bind("<Return>", return_process)  # Catch <Return>
    entry.pack(side=LEFT)

    button = Button(mw, text="OK", command=ok_cmd, fg="blue", bg="light gray")
    button.pack(side=RIGHT)
    mw.mainloop()                   # Loop till quit
    mw.destroy()                    # cleanup
    return entry_text 

"""
Testing Code which only gets run if this file is
executed by itself
"""
if __name__ == '__main__':
    inp = gr_input("Enter Number:")
    print(inp, " Entered")



