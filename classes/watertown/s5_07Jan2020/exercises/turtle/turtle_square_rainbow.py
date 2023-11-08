# turtle_square.py    05Nov2020 from
#  https://www.youtube.com/watch?v=pxKu2pQ7ILo
# Make a square
from turtle import *
side = 100
angle = 90

def right_turn(col, side, angle=90):
    color(col)
    forward(side)
    left(angle)

#colors = ["blue", "red", "green", "orange"]
rainbow = ["black", "red", "orange", "yellow", "green", "blue"] 
adj = 0
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

for side in [100, 200, 300, 400]:
    for col in rainbow:
        right_turn(col, side, angle=45)
