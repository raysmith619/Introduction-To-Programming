# shapes_around_text.py  16Feb2022  crs, from shapes_around
"""
Make a bunch of regular polygon shapes
using functions
Add optional text
"""
from turtle import *

nside_prev = 3
x_prev = 0
x_inc = 100
y_prev = 0
y_inc = x_inc
side_prev = 100
colr_prev = "blue"
wid_prev = 2

def polygon(nside=None, x=None, y=None,
            side=None, colr=None,
            text=None,
            text_font=("Arial", 16, "normal"),
            wid=None, setup=False):
    """ Create regular polygon
    :nside: number of sides default: previous number
    :x: initial position default: previous + 100
    :y: initial y position default previous + 100
    :side: side length default: previous side
    :colr: line color default: previous colr
    :text: add text to figure default: No text
    :text_font: text font default:("Arial", 14, "normal")
    :wid: line width default: previous wid
    :setup: False just set values, default: False
    """
    #NOTE: global is REQUIRED to allow modifying variables
    global nside_prev
    global x_prev
    global y_prev
    global side_prev
    global colr_prev
    global wid_prev
    
    if nside is None:
        nside = nside_prev
    nside_prev = nside
    if x is None:
        x = x_prev + x_inc
    x_prev = x
    if y is None:
        y = y_prev + y_inc
    y_prev =  y
    if side is None:
        side = side_prev
    side_prev = side
    if colr is None:
        colr = colr_prev
    colr_prev = colr
    if wid is None:
        wid = wid_prev
    wid_prev = wid
    if setup:
        return
    
    penup()
    goto(x,y)
    pendown()
    ext_angle = 360/nside
    x_min = x_max = xcor()         # Keep track of range
    y_min = y_max = ycor()
    width(wid)
    color(colr)
    for i in range(nside):
        forward(side)
        x = xcor()
        y = ycor()
        if x < x_min:
            x_min = x
        if x > x_max:
            x_max = x
        if y < y_min:
            y_min = y
        if y > y_max:
            y_max = y
            
        left(ext_angle)
    if text is not None:
        penup()
        #print(f"x_min:{x_min}  x_max:{x_max}")
        #print(f"y_min:{y_min}  y_max:{y_max}")
        text_x = (x_max+x_min)/2    # Center text in polygon
        text_y = (y_max+y_min)/2
        #print(f"text_x: {text_x:2.5}  text_y: {text_y:2.5}")
        goto(text_x, text_y)
        write(text, align="center", font=text_font)
        
""" Testing
Note that we use if __name__ == "__main__" to that
this code only gets executed if we are running this
file by itself
"""
if __name__ == "__main__":
    test = "list,random"
    test = "list"       # limit to simple
    
    colors = ["red","orange", "yellow"
                  "green", "blue", "indigo",
                  "violet"]
    if "list" in test:
        polygon(setup=True, x=-600,y=-600)
        for i in range(8):
            
            colr = colors[i%len(colors)]
            nside = i + 3
            polygon(nside=nside, colr=colr,
                    text=f"{nside} sided polygon")
            
    if "random" in test: 
        from random import randint
        clear()
        xside = yside = 600
        side_base = side_prev     # similar in size
        x_prev = 0
        y_prev = 0
        for i in range(15):
            colr = colors[i%len(colors)]
            nside = randint(0,6)+3
            side = randint(side_base//2,side_base*2)
            x = randint(-xside,xside)
            pwidth = nside/2*side
            if x > xside-pwidth:
                x = xside-pwidth
            y = randint(-yside,yside)
            if y > yside-pwidth:
                y = yside-pwidth
            polygon(nside=nside,
                    side=side,
                    colr=colr, x=x, y=y)
    
