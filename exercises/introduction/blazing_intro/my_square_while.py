# my_square_while.py    11Jan2022  crs, turtle square, loop
from turtle import *    # Turtle stuff
print("Make square loop")
clr = "blue"
side = 200
color(clr)
i = 0
max = 4
while i < max:
    right(90)
    forward(side)
    i = i + 1

