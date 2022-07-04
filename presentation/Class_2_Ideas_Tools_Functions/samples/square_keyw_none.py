#my_square_keyw_none.py   13Jan2022  crs, square using defaults
# Make a square function
# Use None to give flexible missing parameter processing
from turtle import *

prev_color = "blue"
prev_side = 200
prev_wid = 1
def square(x=0, y=0, side=None, colr=None,
           wid=None):
    """ Draw a square
    :x: x position default: 0
    :y: y position default: 0
    :side: length of side default: previous side
    :colr: square color default: previous
    :wid: line width default: previous
    """
    global prev_color   # Don't create local copy
    global prev_side
    global prev_wid
    
    penup()     # raise pen
    goto(x,y)
    pendown()   # lower pen
    if colr is None:
        colr = prev_color   # Use default
    prev_color = colr    # Record for future
    if side is None:
        side = prev_side    # Use default
    prev_side = side    # Record for future
    if wid is None:
        wid = prev_wid    # Use default
    prev_wid = wid    # Record for future
    color(colr)
    width(wid)
    for i in range(4):
        forward(side)
        right(90)

square()    # Use all defaults
square(100, 300,side=300, colr="red", wid=3)
square(x=50, y=50, colr="blue")
square(x=100, y=150, side=50, colr="green", wid=6)
square(x=200,y=250)  #Use default side,color,width
square(x=-300, y=-200, side=200, colr="orange", wid=10)
