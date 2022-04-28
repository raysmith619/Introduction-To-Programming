#my_polygon.py 11Jan2022  crs, turtle polygon

from turtle import *    # Get turtle stuff
nside = 6
colors = ["red","orange","yellow","green",
          "blue", "indigo","violet"]
side = 200
ang = 360/nside
for i in range(nside):
    color(colors[i])
    right(ang)
    forward(side)
    
