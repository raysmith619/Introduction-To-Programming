#my_polygons.py 11Jan2022  crs, turtle polygons

from turtle import *    # Get turtle stuff
nsides = 10
colors = ["red","orange","yellow","green",
          "blue", "indigo","violet"]
speed(0)
penup()
goto(0,250)                 # Move up abit
pendown()
for ns in range(3, nsides+1): # Start with triangle
    nside = ns
    side = 200+ns*10
    penup()
    left(75)
    forward(side*.1)
    right(75)
    pendown()
    ang = 360/nside
    for i in range(nside):
        color(colors[i%len(colors)])    # wrap on colors
        right(ang)
        forward(side)
    
