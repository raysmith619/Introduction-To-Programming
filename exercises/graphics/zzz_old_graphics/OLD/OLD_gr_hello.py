# gr_hello.py   07Mar2019   crs Author
"""

Put up a message
Simplest graphics example I know.
"""
from tkinter import messagebox
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


