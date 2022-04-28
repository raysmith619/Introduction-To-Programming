#my_square_keyw.py   13Jan2022  crs, square using keywords
# Make a square
from turtle import *

prev_color = "black"
def square(x=0, y=0, side=200, clr=None):
    """ Draw a square
    :x: x position default: 0
    :y: y position default: 0
    :side: length of side default: 200
    :clr: square color default: previous
    """
    global prev_color   # Don't create local copy
    penup()     # raise pen
    goto(x,y)
    pendown()   # lower pen
    if clr is None:
        clr = prev_color
    prev_color = clr    # Record for future
    color(clr)
    for i in range(4):
        forward(side)
        right(90)

square(0,0,200,clr="red")
square()    # Use all defaults
square(x=50, y=50, clr="blue")
square(x=100,y=150,side=50,clr="green")
square(x=200,y=250)  #Use default side,color
        
