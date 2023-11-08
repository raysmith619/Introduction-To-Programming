# turtle_onclick_ondrag.py    27Nov2020  crs, from geeksforgeeks

import turtle 
  
  
# screen object 
wn = turtle.Screen() 
  
# method to perform action 
def fxn(x, y): 
  turtle.goto(x, y) 
  turtle.write(str(x)+","+str(y)) 
  
def mydrag(x, y):
    """drag to point
    :x: x-location
    :y: y-location
    """
    ondrag(None)  # Supress recall while here 
    turtle.goto(x, y)
    ondrag(mydrag) 
  
# onclick action  
wn.onscreenclick(fxn)
turtle.ondrag(mydrag) 
wn.mainloop()