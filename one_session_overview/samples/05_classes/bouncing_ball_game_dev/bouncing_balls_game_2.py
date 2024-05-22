# bouncing_balls_game_2.py  03Apr2024  crs, from bouncing_balls_1.py
"""
Simple program to demonstrate class development
Using:
    -- Add Ball class to contain ball specific data/state and function
        data: size, color, location, position
                turtle object for display
        function: display, update
    -- Add turtle display basics
    -- Place turtle code in Ball.display()
    
+ Display ball
"""
import time
import turtle

screen = turtle.Screen()
screen.tracer(0)        # Turn-off animation.

class Ball:
    """ Ball object with functions and state of a ball
    """
    def __init__(self, radius=100, color="blue",
                 v_x=0, v_y=0,
                loc_x=0, loc_y=0):
        self.radius = radius
        self.color = color
        self.v_x = v_x
        self.v_y = v_y
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.b_t = turtle.Turtle()  # -- Create turtle object
        self.b_t.hideturtle()       # -- Hide turtle figure

    def display(self):
        """ Display ball
        """
        # Use turtle object as access to display commands --
        self.b_t.clear()
        self.b_t.up()
        self.b_t.goto(self.loc_x, self.loc_y)   # All is in object via self --
        self.b_t.down()
        self.b_t.dot(self.radius*2, self.color)
        self.b_t.up()
        

class BouncingBallGame:
    def __init__(self, update_time=None):
        """ Do bouncing ball
        :update_time: Our update loop time
                        default: .01 second
        """
        if update_time is None:
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
        self.ball = Ball(radius=100, color="red")
        

    def ball_display(self):
        """ Display ball
        """
        print("ball_display()")
        self.ball.display()

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
        screen.update()     # In each while loop, refresh the screen with the new drawing.


"""
Run our own loop
"""
ut = None   # Use the default (internal) time
ut = 1    # Slow down for development
bg = BouncingBallGame(update_time = ut)
bg.run()
