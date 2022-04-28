# square_list.py    25Feb2022  crs, from spokes.py
# Display a set of colored squares
# Use colors from a list
# square function with keyword parameter defaults

from turtle import *    # Bring in turtle graphic functions


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
    

"""
Testing / Exercise function square
"""
colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]

win_size = 800
nsquare = len(colors)
sq_size_min = win_size/(nsquare+1)
begin = -int(win_size/2)   # lower left corner
for i in range(nsquare):
    sq_size = .7*sq_size_min + i/nsquare*sq_size_min
    x = (i-1)*sq_size + begin
    y = i*sq_size + begin
    colr = colors[i%len(colors)]
    ''' Disable debugging lines
    print("i:", i, "square(x=",x,
          "y=",y, "size=", sq_size,
           "colr=", colr, "wid=", i+1)
    '''
    square(x=x, y=y, size=sq_size,
           colr=colr, wid=i+1)
