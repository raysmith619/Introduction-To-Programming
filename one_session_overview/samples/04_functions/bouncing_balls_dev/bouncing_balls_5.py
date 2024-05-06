# bouncing_balls_5.py  03Apr2024  crs, from bouncing_balls_4.py
"""
Simple program to demonstrate functions development

Let's do something to emphasize each collision
Using:
    -- record collision
    -- change ball color

History:
+ Display ball
+ Update ball (simple)
+ Edge detection
+ Liven up collisions
"""
import time
import turtle

# screen dimensions
window_width = 800
window_height = 800
x_edge_min = -window_width/2
x_edge_max = window_width/2
y_edge_min = -window_height/2
y_edge_max = window_height/2


screen = turtle.Screen()
screen.setup(window_width, window_height)   # Window size.
screen.tracer(0)        # Turn-off animation.

update_loop_time = .01   # Our update loop time
#update_loop_time = .1    # Slow down for development

b_t = turtle.Turtle()
b_t.hideturtle()
running = True
b_x = b_y = b_vx = b_vy = 0 # Set via start_ball
b_vx = 500
b_vy = 200        # Simple seting

ball_radius = 100

ball_color_index = 4        # Index into colors
colors = ["red", "orange", "yellow"
          "green", "blue", "indigo", "violet"]

trace_level = 9     # Trace level higher == more
trace_level = 0     # Stop tracing

def start_ball():
    """ Setup ball, size, position, velocity
    """
    print("start_ball()")

def ball_display():
    """ Display ball
    """
    if trace_level > 0:
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
    if trace_level > 0:
        print("ball_edge_check()")
    global b_vx, b_vy
    global ball_color_index
    global n_collision
    
    collision = False   # -- record if collision
    if b_vx > 0:        # Going right
        if b_x > x_edge_max-ball_radius:
            b_vx = - b_vx
            collision = True
    elif b_vx < 0:        # Going left
        if b_x < x_edge_min+ball_radius:
            b_vx = - b_vx
            collision = True    # -- record collision
    if b_vy > 0:        # Going up
        if b_y > y_edge_max-ball_radius:
            b_vy = - b_vy
            collision = True
    elif b_vy < 0:        # Going down
        if b_y < y_edge_min+ball_radius:
            b_vy = - b_vy
            collision = True
    if collision:
        ball_color_index = (ball_color_index+1)%len(colors) # -- change color
            
def ball_update():
    """ Update ball
        Includes handeling edge collisions
    """
    if trace_level > 0:
        print("ball_update()")
    global b_x, b_y

    ball_edge_check()
    b_x += b_vx*update_loop_time
    b_y += b_vy*update_loop_time
    ball_display()

def screen_update():
    """ Update screen display
    """
    if trace_level > 0:
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
