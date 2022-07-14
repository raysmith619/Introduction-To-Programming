# spokes_function_2.py  13Jul2022  crs, incease spoke len
#                       25Feb2022  crs, from spokes.py
# Display a star with spokes using list
# Define function spoke to do spoke action

from turtle import *    # Bring in turtle graphic functions

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]

def spoke(spoke_len, colr, dot_size):
    """ Make line(spoke) with dot at end
    :len: length of line in pixels
    :colr: color of spoke
    :dot_size: size of dot
    """
    color(colr)
    forward(spoke_len)
    dot(dot_size)
    backward(spoke_len)
    
    

#colors = 2*colors      # Double list
nspoke = len(colors)
spoke_len = 300
for i in range(nspoke):
    colr = colors[i%len(colors)]    # Wrap around list
    spoke(spoke_len*(1+i/nspoke), colr, (i+1)*20)
    right(360/nspoke)
