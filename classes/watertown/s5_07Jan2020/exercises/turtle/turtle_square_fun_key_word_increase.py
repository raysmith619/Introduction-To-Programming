# turtle_square_fun_key_increase.py    05Nov2020 from
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

colors = ["blue", "red", "green", "orange"]
rainbow = ["red", "orange", "green"] 
adj = .3
for i in range(5):
    side = i*100
    for col in rainbow:
        right_turn(col, side)
