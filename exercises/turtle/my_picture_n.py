#my_picture_n.py     25Aug2021  crs, Author
""" A little fun with turtle graphics
    A growing square spiral
"""
from turtle import *    # Bring in all turtle functions

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]
colors = colors*3
for i in range(len(colors)):
    width(4)
    color(colors[i])    # Set color from list
    side = (i+1)*50        # side increases
    forward(side)       # make a line
    right(90)           # Make right turn
    
