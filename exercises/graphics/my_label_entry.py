# my_label_entry.py

import tkinter as tk

mw = tk.Tk()
    
entry_var = tk.StringVar()         # Holds the entry text

label_text = "Input Here:"        
def return_process(event):
    print(f"{label_text} {entry_var.get()}")

# Label code
label = tk.Label(mw, text=label_text)
label.pack(side=tk.LEFT)

# Entry code
entry = tk.Entry(mw, textvariable=entry_var, bd=3) # Create Entry space on right
entry.bind("<Return>", return_process)  # Process <Return>
entry.pack(side=tk.LEFT)


tk.mainloop()
