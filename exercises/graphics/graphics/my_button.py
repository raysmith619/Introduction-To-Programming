# my_button.py
import tkinter as tk

mw = tk.Tk()

def ok_cmd():
    print("ok_cmd")

def not_ok_cmd():
    print("not_ok_cmd")

def quit_cmd():
    print("quit_cmd")
    mw.destroy()
    
button = tk.Button(mw, text="OK", command=ok_cmd,
                fg="green", bg="light gray")
button.pack(side=tk.LEFT)
    
button = tk.Button(mw, text="Not OK", command=not_ok_cmd,
                font="12",
                fg="blue", bg="light gray")
button.pack(side=tk.LEFT)
    
button = tk.Button(mw, text="QUIT", command=quit_cmd,
                font="Tahoma 24",
                fg="red", bg="light gray")
button.pack(side=tk.LEFT)

mw.mainloop()                   # Loop till quit
print("After mainloop")
