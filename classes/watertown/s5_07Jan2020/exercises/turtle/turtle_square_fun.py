# turtle_square.py    05Nov2020 from
#  https://www.youtube.com/watch?v=pxKu2pQ7ILo
# Make a square
from turtle import *
side = 100
angle = 90
def right_turn(col, side, angle):
    color(col)
    forward(side)
    left(angle)

colors = ["blue", "red", "green", "orange"]
for side in [100, 200, 300, 400]:
    for col in colors:
        right_turn(col, side, angle)
