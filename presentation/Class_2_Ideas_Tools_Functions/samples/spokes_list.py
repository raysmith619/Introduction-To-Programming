# spokes_list.py    13Jul2022, crs, increasing dot size
#                   25Feb2022  crs, from spokes.py
# Display a star with spokes using list


from turtle import *    # Bring in turtle graphic functions

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]

#colors = 2*colors      # Double list
nspoke = len(colors)
spoke_len = 300
for i in range(nspoke):
    color(colors[i%len(colors)])    # Wrap around list
    forward(spoke_len)
    dot((i+1)*20)
    backward(spoke_len)
    right(360/nspoke)
