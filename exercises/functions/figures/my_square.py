#my_square.py   13Jan2022  crs, square function
# Make a square
from turtle import *

def square(x, y, side, clr):
    """ Draw a square
    :x: x position
    :y: y position
    :side: length of side
    :clr: square color     color name clashes with turtle
    """
    penup()     # raise pen
    goto(x,y)
    pendown()   # lower pen
    color(clr)
    for i in range(4):
        forward(side)
        right(90)

square()
square(0,0,200,"red")
square(50,50,100,"blue")
square(100,150,50,"green")
        
