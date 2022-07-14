# square_list.py    25Feb2022  crs, from spokes.py
# Display a set of colored squares
# Use colors from a list
# inline - no square function

from turtle import *    # Bring in turtle graphic functions

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]
ncopy = 1
#ncopy = 2                   # Double list
colors = ncopy*colors      # multiply list
nsquare = len(colors)
win_size = 800  
sq_size_min = win_size/((nsquare+1)**2/2)     # Estimate size
begin = -win_size/2 - 2*sq_size_min   # lower left corner
prev_loc = begin
for i in range(nsquare):
    n = i + 1
    sq_size = n*sq_size_min
    x = prev_loc
    y = prev_loc
    wid =(i+1)*2 
    colr = colors[i%len(colors)]

    """ Display square
    """
    penup()
    goto(x,y)
    pendown()
    color(colr)
    wid = n*2
    width(wid)
    for i in range(4):  # Do 4 times
        forward(sq_size)
        left(90)
    prev_loc = x + sq_size + wid  # space next sq
