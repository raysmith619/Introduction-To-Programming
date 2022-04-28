#my_picture_2.py     25Aug2021  crs, Author
""" A little fun with turtle graphics
    A growing square spiral
"""
from turtle import *    # Bring in all turtle functions

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]
c2 = colors*2       # double list
for i in range(len(c2)):
    color(c2[i])    # Set color from list
    side = i*50        # side increases
    forward(side)       # make a line
    right(90)           # Make right turn
    
