# spokes_list.py    25Feb2022  crs, from spokes.py
# Display a star with spokes using list


from turtle import *    # Bring in turtle graphic functions

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]

#colors = 2*colors      # Double list
nspoke = len(colors)
spoke_len = 300
for colr in colors:
    color(colr)
    forward(spoke_len)
    dot(50)
    backward(spoke_len)
    right(360/nspoke)
