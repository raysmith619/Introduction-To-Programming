#turtle_obj_lines_dbg.py    21Dec2020  crs
"""
Object oriented turtle
"""
from math import *
import random
import turtle
ts = []         # List of turtle objects
rainbow = ["red", "orange", "yellow", "green",
           "blue", "indigo", "violet"]
rainbow[2] = rainbow[-1]    # Yellow is too hard to see
colors = rainbow[:4]    # First four colors
colors[2] = "blue"      # Yellow is too hard to see

side = 400
side_min = side*.2
side_max = side*.8
loc_dist = side_min

def lines(tu):
    pos_x, pos_y = tu.position()
    for i in range(15):
        line_side = random.randint(side_min, side_max)
        loc_x = random.randint(-loc_dist, loc_dist)
        loc_y = random.randint(-loc_dist, loc_dist)
        tu.pendown()
        tu.setposition(pos_x+loc_x, pos_y+loc_y)
        pos_x, pos_y = tu.position()
    tu.penup()
    
for i in range(len(rainbow)):
    tu = turtle.Turtle()
    pw = random.randint(2,10)
    tu.pensize(pw)
    #tu.speed("fastest")
    tu.penup()
    tu.color(rainbow[i])
    tu.setposition(random.randint(-side,side),
                   random.randint(-side,side))
    lines(tu)
