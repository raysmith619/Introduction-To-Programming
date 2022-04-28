#my_polygon_keyw.py   13Jan2022  crs, from my_square_keyw.py
# Make a regular polygons
from turtle import *

# Previous values
prev_color = "black"    # color
prev_side = 200         # side in pixels
prev_nside = 4          # number of sides

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]
def polygon(nside=None,
            x=0, y=0,
            side=None,
            clr=None):
    """ Draw a square
    :nside: number of sides default:previous (e.g. 4-square)
    :x: x position default: 0
    :y: y position default: 0
    :side: length of side default: previous side
    :clr: square color default: previous color
    """
    global prev_nside   # Don't create local variable
    global prev_side    # Don't create local variable
    global prev_color   # Don't create local variable
    
    penup()     # raise pen
    goto(x,y)
    pendown()   # lower pen
    if nside is None:
        nside = prev_nside
    prev_nside = nside
        
    if side is None:
        side = prev_side
    prev_side = side
    
    if clr is None:
        clr = prev_color
    prev_color = clr    # Record for future
    
    color(clr)
    angle = 360/nside
    for i in range(nside):
        forward(side)
        right(angle)

#testing
nfig = 6
xbeg  = -600
xend = 600
xrange = xend-xbeg
ybeg = -600
yend = 600
yrange = yend-ybeg
side = .85*min(xrange,yrange)/nfig
xoff = 40   # offsets for second polygon
yoff = 20   
for i in range(nfig):
    nside = i + 3       # Start with triangle
    width(4)            # Width of line
    x = xbeg + i*side
    y = ybeg + side/2 +(i+1)*side
    polygon(nside=nside, x=x, y=y,
            side=side*(1-((i-1)/nfig)), # Shrink polygons
            clr=colors[i%len(colors)])
    
    polygon(x=x+xoff, y=y+yoff) # Second with defaults
                                # except for offset position
        
