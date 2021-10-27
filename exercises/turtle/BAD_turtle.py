#BAD_turtle.py     25Aug2021  crs, Author
# CAUTION: delete or rename this file
#          to something other than turtle.py
#          its presence will keep turtle programs
#          from running properly
#
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
    
