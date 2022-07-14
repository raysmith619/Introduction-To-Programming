# spokes_function_minimum.py    13Jul2022  crs
#                               25Feb2022  crs, from spokes.py
# Display a star with spokes using list
# Define function spoke to do spoke action
# MINIMUM FUNCTION functionality

from turtle import *    # Bring in turtle graphic functions

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]

def spoke(spoke_len, dot_size):
    """ Make line(spoke) with dot at end
    :len: length of line in pixels
    :dot_size: size of dot
    """
    forward(spoke_len)
    dot(dot_size)
    backward(spoke_len)
    
    

#colors = 2*colors      # Double list
nspoke = len(colors)
spoke_len = 300
for i in range(nspoke):
    color(colors[i%len(colors)])    # Wrap around list
    spoke(spoke_len,(i+1)*20)
    right(360/nspoke)
    
