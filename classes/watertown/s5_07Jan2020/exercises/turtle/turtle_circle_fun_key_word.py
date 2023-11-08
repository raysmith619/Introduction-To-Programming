#15Dec05Nov2020 from
#  https://www.youtube.com/watch?v=pxKu2pQ7ILo
# Note that this video uses the following style
# import turtle
# bob = turtle.Turtle()
# bob.forward(100)
# ...
# back to our example...
# Make a square
from turtle import *

def right_turn(col, side, angle=90):
    color(col)
    forward(side)
    left(angle)
    
def my_circle(col, rad):
    color(col)
    circle(rad)
    
colors = ["blue", "red", "green", "orange"]
rainbow = ["red", "orange", "green"] 
adj = 0
for side in [100, 200, 300, 400]:
    for col in rainbow:
        my_circle(col, side)
