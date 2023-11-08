#turtle_obj_circle_square.py    21Dec2020  crs
"""
Object oriented turtle
"""
from math import *
import turtle
ts = []         # List of turtle objects
rainbow = ["red", "orange", "yellow", "green",
           "blue", "indigo", "violet"]
rainbow[2] = rainbow[-1]    # Yellow is too hard to see
colors = rainbow[:4]    # First four colors
colors[2] = "blue"      # Yellow is too hard to see

side = 200
off_center = 250
nseg = len(rainbow)     # number of segments

radius = side*sqrt(2)
# Setup turtles around a circle
for i in range(nseg):
    angle = i*360/nseg
    tu = turtle.Turtle()
    tu.speed("fastest")
    ts.append(tu)       # Add turtle instance to list
    tu.color(rainbow[i])
    tu.penup()
    tu.setposition(off_center*cos(angle),
                   off_center*sin(angle))
    tu.pendown()
    tu.dot(10)
    tu.penup()
    tu.setposition(0,0)
    tu.setheading(angle-90)
    tu.pendown()
    tu.circle(off_center)
    tu.penup()
    if i >= nseg:
        break

# Create figure with each turtle
for i in range(nseg):
    tu = ts[i]
    angle = i*360/nseg
    tu.setposition(off_center*cos(angle), off_center*sin(angle))
    tu.pendown()
    for col in colors:
        tu.color(col)
        tu.right(90)
        tu.forward(side)
    if i >= nseg:
        break
