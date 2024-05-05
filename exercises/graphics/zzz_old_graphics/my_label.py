#my_label.py    15Aug2021  crs, simple label
import tkinter as tk


root = tk.Tk()

# place a label on the root window

message = tk.Label(root, text="Here's my label!")
message.pack()

# keep the window displaying
root.mainloop()
