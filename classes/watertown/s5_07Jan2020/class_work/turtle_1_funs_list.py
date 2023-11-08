#turtle_1_funs.py 17Nov2020 crs

from turtle import *
rainbow = ["red", "orange", "yellow", "green", "blue",
           "indigo", "violet"]
def rt_corn(col, angle, side):
    color(col)
    right(angle)
    forward(side)
    
for i in range(len(rainbow)):
    col = rainbow[i]
    rt_corn(col, 90*i*1.3, side=30*i)
