#wx_my_window.py

#  The following imports all wx contents
from wx import *

app = App()
frame = Frame(None)  # None is IMPORTANT otherwise nothing is displayed
frame.Show()

app.MainLoop()
