# bouncing_balls_1.py  03Apr2024  crs, from bouncing_balls.py
"""
Simple program to demonstrate functions development
We hope to show how a progam might start with a simple
form and be modified, in steps, to add functionality,
ending in a working program.

To shorten our path we will start assuming we have an
idea how to divide up the labor into a small
group of functions below.  Production would probably
involve in trial and error in creating our function
group.
"""
import time
update_loop_time = .01   # Our update loop time
update_loop_time = 1    # Slow down for development
running = True


def start_ball():
    """ Setup ball, size, position, velocity
    """
    print("start_ball()")

def ball_display():
    """ Display ball
    """
    print("ball_display()")

def ball_edge_check():
    """ Adjust motion if/when edge touched
        Simple physics of edge collision says
            The velocity perpendicular to the
            collision edge is reversed.

    """
    print("ball_edge_check()")
            
def ball_update():
    """ Update ball
        Includes handeling edge collisions
    """
    print("ball_update()")
    ball_display()

def screen_update():
    """ Update screen display
    """
    print("screen_update()")
    ball_update()


"""
Run our own loop
"""
start_ball()            # Setup ball inital properties
while running:
    time.sleep(update_loop_time)
    screen_update()
