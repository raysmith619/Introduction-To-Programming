# my_entry.py

import tkinter as tk

mw = tk.Tk()
    
entry_var = tk.StringVar()         # Holds the entry text
        
def return_process(event):
    print(f"entry: {entry_var.get()}")


entry = tk.Entry(mw, textvariable=entry_var, bd=3) # Create Entry space on right
entry.bind("<Return>", return_process)  # Catch <Return>
entry.pack(side=tk.LEFT)


tk.mainloop()
