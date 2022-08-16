# fireworks.py  19Feb2022  crs, Author
"""
Simple fireworks like display

Each firework's current state is stored in a dictionary.
The fireworks' dictionaries are stored in the list
fireworks_list.

This program runs in an implicit infinite loop.
This loop is driven by on turtle's ontimer function
first called from fireworks_start.  ontimer is
subsequently called from fireworks_update.
"""
from turtle import *
from random import randint, uniform
import time

speed("fastest")        # 0 - fastest drawing - no delay
hideturtle()
penup()
# screen dimensions in pixels
window_width = 800
window_height = 800
window_size = min(window_width, window_height)
x_edge_min = -window_width/2
x_edge_max = window_width/2
y_edge_min = -window_height/2
y_edge_max = window_height/2
print(f"window_width:{window_width} window_height:{window_height}")
print(f"x_edge_min:{x_edge_min} y_edge_min:{y_edge_min}")
print(f"y_edge_max:{y_edge_max} y_edge_max:{y_edge_max}")
screen = Screen()
screen.setup(window_width, window_height)   # Window size.
screen.tracer(0)                    # Turn-off animation.
update_time = .01                   # Our update event time
running = False                     # True -> updating

            
n_fwork = 10         # Number of fire works

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo", "violet",
          ###"gray", "black", "pink"
          ]
fw_size_min = window_size*.05
fw_size_max = window_size/n_fwork
firework_list = []      # List of firework objects


def firework_create():
    """ Create firework to initial state
    :returns: new firework object (dictionary)
    """
    fw_size = uniform(fw_size_min, fw_size_max)
    boarder = fw_size*1.1
    x = uniform(x_edge_min+boarder, x_edge_max-boarder)
    y = uniform(y_edge_min+boarder, y_edge_max-boarder)
    #print(f"x:{x} y:{y}")
    colr = colors[randint(0,len(colors)-1)]
    firework = {}      # Start fire work
    firework['x'] = x    # initial location
    firework['y'] = y
    firework['size'] = fw_size
    firework['size_inc'] = fw_size*.01
    firework['color'] = colr
    return firework

def firework_start(fw):
    """ Start firework activity by setting event timer
    :fw: firework object / dictionary
    """
    pass    # Nothing yet

def firework_display(fw):
    """ Display firework
    :fw: firework object
    """
    size = fw['size'] 
    x = fw['x']
    y = fw['y']
    penup()
    goto(x,y)
    pendown()
    dot(fw['size'], fw['color'])
    
    
def firework_update(fw):
    """ Update this firework
    :fw: firework object (updated in place)
    """
    size = fw['size']
    radius = size/2
    x = fw['x']
    y = fw['y']
    size_inc = fw['size_inc']
    # Grow firework until it hits a display edge
    if (x-radius <= x_edge_min or x+radius >= x_edge_max
        or y-radius <= y_edge_min or y+radius >= y_edge_max):
        # Then create replacement firework
        fw_new = firework_create()
        fw.clear()          # remove all dictionary elements
        fw.update(fw_new)   # Add elements from fw_new
        return

    size += size_inc
    fw['size'] = size
    
def fireworks_update():
    """ Up fireworks and redisplay
    """
    if not running:
        return

    for fw in firework_list:
        firework_update(fw) 
    clear()                 # Clear whole display
    for fw in firework_list:
        firework_display(fw)
    ontimer(fireworks_update, int(update_time*1000))  # reprime
    
    
def fireworks_start():
    """ Startup all fire works
    """
    global running
    
    running = True      # Signal we are running    
    ontimer(fireworks_update, int(update_time*1000))

# Create fireworks
for i in range(n_fwork+1):
    firework = firework_create()
    firework_list.append(firework)

# Start each firework
# Separated from above to delay any action
# till all fireworks are setup
fireworks_start()

# All subsequent activity is driven by events
# setup by fireworks_start()

mainloop()      # Do event processing

    
    
