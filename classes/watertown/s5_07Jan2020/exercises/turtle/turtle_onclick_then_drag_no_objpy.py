# turtle_onclick_then_drag_no_obj.py    27Nov2020  crs, from geeksforgeeks
"""
DOESN'T WORK
Click add item, then drag it
"""
from turtle import *
  
def mydrag(x, y):
    """drag to point
    :x: x-location
    :y: y-location
    """
    print(f"mydrag(x={x}, y={y}")
    ondrag(None)  # Supress recall while here 
    turtle.goto(x, y)
    ondrag(mydrag)

def myrelease(x, y):
    """ Drop connection
          Disable drag
          Disable release
          Enable click
    """
    print(f"myrelease(x={x}, y={y}")
    onrelease(None)
    ondrag(None)
    onclick(myclick)
    
# method to perform action 
def myclick(x, y):
    print(f"myclick(x={x}, y={y}")
    penup() 
    goto(x, y)
    pendown()
    ondrag(mydrag)
    onrelease(myrelease)
    
onclick(myclick)
mainloop()