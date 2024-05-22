# bouncing_balls_3.py  03Apr2024  crs, from bouncing_balls_2.py
"""
Simple program to demonstrate functions development
We're adding code to update the picture (ball's location)
Including:
    -- balls velocity
    -- ball_update: location change per velocity*time
History:
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
b_x = b_y = 0           # Set via start_ball
b_vx = b_vy = 10        # Simple intial velocity setting --

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
    b_x += b_vx*update_loop_time    # loc change = velocity*time --
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
