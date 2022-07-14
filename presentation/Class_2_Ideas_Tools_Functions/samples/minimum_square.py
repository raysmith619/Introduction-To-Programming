# minimum_square.py 13Jul2022  crs, minimum function
# Display a set of colored squares
# Use colors from a list
# 

from turtle import *    # Bring in turtle graphic functions

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]


def square(size):
    """ Display square
        position, color, line width must be already set
    :size: size of side default:300
    """
    for i in range(4):  # Do 4 times
        forward(size)
        right(90)

for i in range(8):
    colr = colors[i%len(colors)]    # wrap colors
    color(colr)
    side = (i+1)*15
    square(side)
    #penup()            # So we don't drag pen
    forward(side*1.1)
    #pendown()
