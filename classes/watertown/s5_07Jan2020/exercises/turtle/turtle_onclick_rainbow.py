# turtle_on_click_rainbow.py    27Nov2020  crs, from turtle_onclick
""" Adding color to turtle_onclick.py
Operation:
  Repeat:
    1. Position the mouse inside graphics screen
    2. Click mouse (button one)
    A line is draw to the mouse position
"""

from turtle import * 
  
rainbow = ["red", "orange", "yellow", "green",
           "blue", "indigo", "violet"]
color_index = len(rainbow)  # Starting color
# screen object 
wn = Screen()   # Required for events(e.g. click) 
  
# method to perform action 
def fxn(x, y):
  global color_index  # Required if changing outside var
          # Change to next rainbow color
          # Wraps to first at end of list
  color_index = (color_index + 1)%len(rainbow)
  color(rainbow[color_index])
  goto(x, y) 
  
# onclick action  
wn.onclick(fxn) 
wn.mainloop()
