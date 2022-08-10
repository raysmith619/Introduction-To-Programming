# line_function_2.py    08Aug2022  crs, simple line
"""
Short line function
star burst

"""
import math
from math import sin,cos
from random import randint
from turtle import *    # Bring in turtle graphic functions

def line(x1,y1, x2,y2):
    """ Display line
    :x1: starting x position
    :y1: starting y position
    :x2: ending x position
    :y2: ending y position
    """
    speed(0)
    penup()
    goto(x1,y1)
    pendown()
    goto(x2,y2)

def burst(x,y,size, n):
    """
    :x: center x position
    :y: center y position
    :size: burst size
    :n: number of spokes
    """
    speed(0)   # 0 - fastest, 1-10 slow to fast 
    penup()
    goto(x,y)
    for i in range(n):
        angle = (i*360)/n   # Circle of spokes
        rangle = math.radians(angle)    # math in radians
        x2 = x + size*cos(rangle)
        y2 = y + size*sin(rangle)
        #print(i,"angle:",angle,"cos:", cos(angle),
        #      "sin:", sin(angle),"x2:",x2,"y2:",y2)
        line(x,y,x2,y2)
        pass
    
    
#
# Testing code
#

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]
nstar = 30
win_size = 800
radius = win_size/2
for i in range(nstar):
    x1 = 0
    y1 = 0
    x2 = randint(-radius,radius)
    y2 = randint(-radius,radius)
    colr = colors[i%len(colors)]    # next color, wraps
    linewidth = 1
    width(linewidth)
    color(colr)
    line(x1,y1,x2,y2)
    burst_size = randint(5,30)
    width(4)
    burst(x2,y2,randint(10,30), 10)
