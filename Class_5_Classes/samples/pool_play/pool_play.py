

def start_ball():
    """ Setup ball, size, position, velocity
    """
    global b_x, b_y, b_vx, b_vy
    global n_start
    global n_collision
    global ball_radius
    
    n_collision = 0
    n_start += 1
    if n_start == 1:
        b_x = randint(int(x_edge_min),int(x_edge_max))
        b_y = randint(int(y_edge_min),int(y_edge_max))
    ball_radius = randint(ball_radius_min, ball_radius_max)

    b_vx = randint(window_width//2, window_width)/nt
    b_vy = randint(window_height//2, window_height)/nt
    print(f"b_x:{int(b_x)}, b_y:{int(b_y)}  b_vx={b_vx:0.7} b_vy:{b_vy:0.7}")
    b_t.penup()
    b_t.goto(b_x, b_y)       # Starting position

def ball_display():
    """ Display ball
    """
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
    global b_vx, b_vy
    global ball_color_index
    global n_collision
    
    collision = False
    if b_vx > 0:        # Going right
        if b_x > x_edge_max-ball_radius:
            b_vx = - b_vx
            collision = True
    elif b_vx < 0:        # Going left
        if b_x < x_edge_min+ball_radius:
            b_vx = - b_vx
            collision = True
    if b_vy > 0:        # Going down
        if b_y > y_edge_max-ball_radius:
            b_vy = - b_vy
            collision = True
    elif b_vy < 0:        # Going right
        if b_y < y_edge_min+ball_radius:
            b_vy = - b_vy
            collision = True
    if collision:
        ball_color_index = (ball_color_index+1)%len(colors)
        n_collision += 1
        if n_collision >= ncol_to_restart:
            # Change ball,... after a few bounces
            turtle.ontimer(start_ball)  # when we get a chance
            
def ball_update():
    """ Update ball
        Includes handeling edge collisions
    """
    global b_x, b_y

    ball_edge_check()
    b_x += b_vx*update_loop_time
    b_y += b_vy*update_loop_time
    ball_display()

#pool_play.py

def screen_update():
    """ Update screen display
    """
    #print("screen_update")
    ball_update()
    screen.update()     # In each while loop, refresh the screen with the new drawing.

def on_close():
    """ Stop display loop and close window
    """
    global running
    running = False
    print("Stopping display")
    root.destroy()
    
"""
Enable clicking window close to do
clean program stop
"""
root.protocol("WM_DELETE_WINDOW", on_close)    


"""
Run our own loop
"""
start_ball()            # Setup ball inital properties
while running:
    time.sleep(update_loop_time)
    screen_update()
