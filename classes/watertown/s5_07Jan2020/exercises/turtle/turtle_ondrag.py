#turtle_ondrag.py    26Nov2020  crs
from turtle import *

""" Simple demonstration of mouse dragging
Operation:
    Repeat:
        1. Mouse down on Turtle figure
        2. While mouse button is down, drag mouse
            Line is drawn

"""
# screen object 
wn = Screen()   # Required for events(e.g. click) 
def mydrag(x,y):
    ondrag(None)        # Disable to avoid possible event
    goto(x,y)
    ondrag(mydrag)

ondrag(mydrag)
wn.mainloop()                  # Necessary for events
