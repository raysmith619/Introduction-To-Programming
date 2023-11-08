# turtle_onclick_then_drag.py    27Nov2020  crs, from geeksforgeeks
"""
Click add item, then drag it
"""
import turtle

wn = turtle.Screen()    
  
def mydrag(x, y):
    """drag to point
    :x: x-location
    :y: y-location
    """
    print(f"mydrag(x={x}, y={y}")
    turtle.ondrag(None)  # Supress recall while here 
    turtle.goto(x, y)
    turtle.ondrag(mydrag)

def myrelease(x, y):
    """ Drop connection
          Disable drag
          Disable release
          Enable click
    """
    print(f"myrelease(x={x}, y={y}")
    turtle.onrelease(None)
    turtle.ondrag(None)
    turtle.onclick(myclick)
    
# method to perform action 
def myclick(x, y):
    turtle.onclick(None)
    print(f"myclick(x={x}, y={y}")
    turtle.penup()
    turtle.shape("circle") 
    turtle.goto(x, y)
    turtle.stamp()
    turtle.pendown()
    turtle.ondrag(mydrag)
    turtle.onrelease(myrelease)
    

turtle.speed("fastest")
wn.onclick(myclick)
wn.mainloop()