# turtle_onclick.py    30Nov2020  crs, from geeksforgeeks
""" Simple demonstration of mouse click interaction
Operation:
  Repeat:
    1. Position the mouse inside graphics screen
    2. Click mouse (button one)
    A line is draw to the mouse position
"""
from turtle import * 
# screen object 
wn = Screen()   # Required for events(e.g. click) 
  
# method to perform action 
def fxn(x, y):
  goto(x, y) 
  
# onclick action  
wn.onclick(fxn) 
wn.mainloop()
