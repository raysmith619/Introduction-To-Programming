#my_picture_3a.py     25Aug2021  crs, Author
""" A little fun with turtle graphics
    A growing square spiral
"""
from turtle import *    # Bring in all turtle functions
colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]
c3 = colors*3
for i in range(len(c3)):
    color(c3[i])    # Set color from list
    side = i*50        # side increases
    forward(side)       # make a line
    right(90)           # Make right turn
    
