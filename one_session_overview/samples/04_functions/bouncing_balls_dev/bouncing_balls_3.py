# bouncing_balls_3.py  03Apr2024  crs, from bouncing_balls_2.py
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
+ Display ball
+ Update ball (simple)
"""
import time
import turtle
screen = turtle.Screen()
screen.tracer(0)        # Turn-off animation.

update_loop_time = .01   # Our update loop time
update_loop_time = 1    # Slow down for development

b_t = turtle.Turtle()
b_t.hideturtle()
running = True
b_x = b_y = b_vx = b_vy = 0 # Set via start_ball
b_vx = b_vy = 10        # Simple seting

ball_radius = 100

ball_color_index = 4        # Index into colors
colors = ["red", "orange", "yellow"
          "green", "blue", "indigo", "violet"]

trace_level = 9   # Trace level higher == more

def start_ball():
    """ Setup ball, size, position, velocity
    """
    print("start_ball()")

def ball_display():
    """ Display ball
    """
    print("ball_display()")
    if trace_level > 0:
        print("ball_display()")
    ball_color = colors[ball_color_index]
    b_t.clear()
    b_t.up()
    b_t.goto(b_x,b_y)
    b_t.down()
    b_t.dot(ball_radius*2, ball_color)
    b_t.up()

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
    global b_x, b_y

    ball_edge_check()
    b_x += b_vx*update_loop_time
    b_y += b_vy*update_loop_time
    ball_display()

def screen_update():
    """ Update screen display
    """
    print("screen_update()")
    ball_update()
    screen.update()     # In each while loop, refresh the screen with the new drawing.


"""
Run our own loop
"""
start_ball()            # Setup ball inital properties
while running:
    time.sleep(update_loop_time)
    screen_update()
