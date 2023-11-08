#turtle_prog_list.py 15Nov2020 crs     from turtle_prog_1
"""
Playing with turtle graphics
"""
from turtle import *    # Get all graphics stuff
side = 200
rainbow = ["red", "orange", "yellow", "green",
           "blue", "indigo", "violet"]
for col in rainbow:
    color(col)
    right(90)
    forward(side)

''' More (Place "#" at line start to enable more)
print("rainbow length:", len(rainbow))
for i in range(len(rainbow)):
    col = rainbow[i]
    color(col)
    right(90)
    forward(side*i*.5)
#'''


