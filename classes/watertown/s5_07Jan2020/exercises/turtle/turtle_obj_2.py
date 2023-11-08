#turtle_obj_2.py    21Dec2020  crs
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
radius_min = side*.1
radius_max = side//3
loc_dist = radius_min*2

def balloons(tu):
    pos_x, pos_y = tu.position()
    for i in range(5):
        pos_x, pos_y = tu.position()
        radius = random.randint(radius_min, radius_max)
        loc_x = random.randint(-loc_dist, loc_dist)
        loc_y = random.randint(-loc_dist, loc_dist)
        tu.penup()
        tu.setposition(pos_x+loc_x, pos_y+loc_y)
        tu.pendown()
        tu.circle(radius)
    tu.penup()
    
for i in range(len(rainbow)):
    tu = turtle.Turtle()
    tu.speed("fastest")
    tu.penup()
    tu.color(rainbow[i])
    tu.setposition(random.randint(-side,side),
                   random.randint(-side,side))
    balloons(tu)
