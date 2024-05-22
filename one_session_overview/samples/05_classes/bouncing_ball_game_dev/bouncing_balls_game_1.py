# bouncing_balls_game_1.py  03Apr2024  crs, from bouncing_balls_1.py
"""
Simple program to demonstrate class development
We hope to show how a progam might start with a simple
form and be modified, in steps, to add functionality,
ending in a working program.
To shorten our path we will start assuming we have an
idea how to divide up the labor into a class(object)
with thought out group of classes / functions.  Production
would probably involve in trial and error
in creating our classes / functions.
History:
    + Move function group into a main class
    + Put the main loop in a member function run()
"""
import time
update_loop_time = .01   # 
running = True

class BouncingBallGame:
    def __init__(self, update_time=None):
        """ Do bouncing ball
        :update_time: Our update loop time
                        default: .01 second
        """
        if update_time is None:     # Check if absent ==> default
            update_time = .01
        self.update_time = update_time
        self.running = True
    
    def run(self):
        self.start_ball()            # Setup ball inital properties
        while self.running:
            time.sleep(self.update_time)
            self.screen_update()

    def start_ball(self):
        """ Setup ball, size, position, velocity
        """
        print("start_ball()")

    def ball_display(self):
        """ Display ball
        """
        print("ball_display()")

    def ball_edge_check(self):
        """ Adjust motion if/when edge touched
            Simple physics of edge collision says
                The velocity perpendicular to the
                collision edge is reversed.

        """
        print("ball_edge_check()")
                
    def ball_update(self):
        """ Update ball
            Includes handeling edge collisions
        """
        print("ball_update()")
        self.ball_display()

    def screen_update(self):
        """ Update screen display
        """
        print("screen_update()")
        self.ball_update()


"""
Run our own loop
"""
ut = None   # Use the default (internal) time
ut = .1    # Slow down for development
bg = BouncingBallGame(update_time = ut)
bg.run()
