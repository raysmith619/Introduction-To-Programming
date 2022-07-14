# spokes_function_defaults.py    25Feb2022  crs, from spokes.py
# Display a star with spokes using list
# Define function spoke to do spoke action
# Provide function with default parameter values

from turtle import *    # Bring in turtle graphic functions

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]

def spoke(spoke_len=300, colr="orange", dot_size=40):
    """ Make line(spoke) with dot at end
    :len: length of line in pixels default:300
    :colr: color of spoke default: red
    :dot_size: size of dot default:40
    """
    color(colr)
    forward(spoke_len)
    dot(dot_size)
    backward(spoke_len)
    
    

#colors = 2*colors      # Double list
nspoke = len(colors)
for colr in colors:
    color(colr)
    spoke()             # all defaults
    spoke(spoke_len=400, colr=colr, dot_size=100)
    spoke(spoke_len=150, colr=colr)  # Use default dot_size
    right(360/nspoke)
