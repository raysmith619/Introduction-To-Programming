# square_function.py    25Feb2022  crs, from spokes.py
# Display a set of colored squares
# Use colors from a list
# square function with keyword parameter defaults

from turtle import *    # Bring in turtle graphic functions

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]


def square(x=0, y=0, size=300, colr="red", wid=1):
    """ Display square
    :x: x location of lower left corner default:0
    :y: y location of lower left corner default:0
    :colr: color of spoke default: red
    :size: size of side default:300
    :wid: line width default: 1
    """
    penup()
    goto(x,y)
    pendown()
    color(colr)
    width(wid)
    for i in range(4):  # Do 4 times
        forward(size)
        right(90)
    

#colors = 2*colors      # Double list
nsquare = len(colors)
sq_size_min = 10
begin = -int(sq_size_min*nsquare/2)   # lower left corner
for n in range(1, nsquare+1):
    sq_size = n*sq_size_min
    x = n*sq_size + begin
    y = n*sq_size + begin
    colr = colors[n%len(colors)]
    square(x=x, y=y, size=sq_size,
           colr=colr, wid=n)
