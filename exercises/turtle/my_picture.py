#my_picture.py     25Aug2021  crs, Author
""" A little fun with turtle graphics
    A growing square spiral
"""
from turtle import *    # Bring in all turtle functions
colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]
for i in range(len(colors)):
    color(colors[i])    # Set color from list
    side = i*50        # side increases
    forward(side)       # make a line
    right(90)           # Make right turn
    
