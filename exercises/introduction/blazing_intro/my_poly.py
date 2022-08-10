# my_poly.py    11Jan2022  crs, turtle polygon, loop
from turtle import *    # Turtle stuff
print("Make polygon")
clr = "orange"
side = 200
color(clr)
nside = 7
angle = 360/nside
i = 0
while i < nside:
    right(angle)
    forward(side)
    i = i + 1

