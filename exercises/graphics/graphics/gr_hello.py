# gr_hello.py   12Aug2021   crs, use tkMessageBox
#               07Mar2019   crs Author
"""

Put up a message
Simplest graphics example I know.
"""
import tkinter as tk
from tkinter import messagebox  # from tk import fails
root = tk.Tk()
root.withdraw()     # To avoid root window display
title = "Hello"
message = "Hello World!"
messagebox.showinfo(title, message)

# Let's do another.
title = "New Title"
message = """ Longer message
- Multiple Lines
are supported.
"""
messagebox.showinfo(title, message)


