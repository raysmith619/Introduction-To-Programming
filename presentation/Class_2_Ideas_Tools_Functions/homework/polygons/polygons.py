# polygons.py   04-Aug-2021  crs, Author
"""
Create polygons, using turtle
"""
from turtle import *

def rectangle(x=0, y=0, height=75, width=75,
              col="red"):
    """ Create a rectangle
        moving to corner with pen up (no line)
    :x: x coordinate of lower left corner
        default:0
    :y: y coodinate of lower left corner
    :height: height
            default: 75
    :width: width
            default: 75
    :col: figure's color
            default: "red"
    """
    penup()             # Raise pen - no writing
    setpos(x=x, y=y)    # Go to x,y
    pendown()           # Lower pen - start writing
    setheading(0)       # Set direction in deg (0 - east)
    color(col)
    forward(width)      # move forward width pixels
    left(90)            # Turn left (counter clockwise)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    left(90)            # Set back to east

# Testing
test_no = 4         # The higher - the more
#test_no = 3         # Limit to first 3 tests
                    # Comment out to continue

if test_no >= 1:
    print("Simple Test - default rectangle")
    rectangle()     # All defaults

if test_no >= 2:
    print("Simple Test - default size")
    rectangle(x=-300, y=200)

if test_no >=3:
    print("Simple Test - one rectangle")
    rectangle(x=-500, y=-50, width=300, height=200,
              col="green")
if test_no >=4:
    print("\nTesting rectangle")
    nrec = 7
    rwidth = 150
    rheight = 200
    x = -rwidth
    y = -rheight*1.5
    incx = rwidth/nrec
    incy = rheight/nrec
    colors = ["red", "orange", "yellow",
              "green", "blue", "indigo",
              "violet"]
    for i in range(nrec):
        col = colors[i%len(colors)]
        rwidth = rwidth + incx
        rheight = rheight + incy
        rectangle(x=x, y=y,
                  width=rwidth, height=rheight,
                  col=col)
        x = x + incx
        y = y + incy
   
