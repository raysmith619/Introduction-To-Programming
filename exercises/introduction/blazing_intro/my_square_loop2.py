# my_square_loop2.py    11Jan2022  crs, sq double loop
from turtle import *    # Turtle stuff
print("Make square loop loop")
clr = "blue"
side = 200
color(clr)
i = 0
max = 10
tilt=60
grow=.7
while i < max:
    j = 0
    forward(side/grow)
    side = side*grow
    right(tilt)
    while j < 4:
        right(90)
        forward(side)
        j = j + 1
    i = i + 1
