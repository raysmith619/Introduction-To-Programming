# starry_night.py  16feb2022  crs, Simple picture
"""
Uses turtle to make a spiral star-like pattern
"""

from turtle import *    # Bring in the magic

# list of color names
colors_rainbow = ["red","orange", "yellow",
                  "green", "blue", "indigo",
                  "violet"]


n_colors = len(colors_rainbow)  # Get length of list
n_spokes = n_colors*4           # Get number of spokes

# Setup for gradual lenthening of spoke length
spoke_length_min = 100
spoke_length_max = 200
spoke_length_inc = (spoke_length_max-spoke_length_min)/n_spokes

# Setup for gradual widening of spokes
spoke_width_min = 3
spoke_width_max = 4
spoke_width_inc = (spoke_width_max-spoke_width_min)/n_spokes

angle_inc = 2.5*360/n_spokes    # make subsequent turns not overlap
for i in range(n_spokes):
    our_color = colors_rainbow[i % n_colors]    # get color, wrapping
    color(our_color)
    right(angle_inc)
    spoke_width = spoke_width_min + i*spoke_width_inc
    width(spoke_width)
    spoke_length = spoke_length_min + i*spoke_length_inc
    forward(spoke_length)
    backward(spoke_length)

mainloop()      # Keeps window arround
