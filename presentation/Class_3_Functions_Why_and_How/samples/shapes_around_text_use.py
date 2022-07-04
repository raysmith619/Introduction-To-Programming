# shapes_around_text_use.py  03Jul2022  crs, from shapes_around_text
"""
Use shapes_around_text.py
"""
from shapes_around_text import *

colors = ["red","orange", "yellow"
              "green", "blue", "indigo",
              "violet"]
nside = 4
#polygon(setup=True,x=-400,y=-400)
for color in colors:
    polygon(nside=nside, colr=color)
