# line_function.py    08Aug2022  crs, simple line
"""
Short line function
Random lines
"""

def line(x1,y1, x2,y2):
    """ Display line
    :x1: starting x position
    :y1: starting y position
    :x2: ending x position
    :y2: ending y position
    """
    penup()
    goto(x1,y1)
    pendown()
    goto(x2,y2)

#
# Testing code
#
from random import randint
from turtle import *    # Bring in turtle graphic functions

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]
nline = 30
win_size = 800
radius = win_size/2
for i in range(nline):
    x1 = randint(-radius,radius)
    y1 = randint(-radius,radius)
    x2 = randint(-radius,radius)
    y2 = randint(-radius,radius)
    colr = colors[i%len(colors)]    # next color, wraps
    linewidth = randint(4,i+4)
    width(linewidth)
    color(colr)
    line(x1,y1,x2,y2)
