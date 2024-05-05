# bouncing_balls_0_1.py  03Apr2024  crs, from bouncing_balls)1.py
"""
Bare bones program to demonstrate functions development
"""
import time
update_loop_time = .01   # Our update loop time
update_loop_time = 1    # Slow down for development
running = True

def start_ball():
    """ Startup
    """
    print("start_ball()")
    
def screen_update():
    """ Update screen display
    """
    print("screen_update()")


"""
Run our own loop
"""
start_ball()            # Setup ball inital properties
while running:
    time.sleep(update_loop_time)
    screen_update()
