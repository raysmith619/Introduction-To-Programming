# bouncing_balls_game_3.py  03Apr2024  crs, from bouncing_balls_2.py
"""
Simple program to demonstrate class development
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

class Ball:
    """ Ball object with functions and state of a ball
    """
    def __init__(self, game, radius=100, color="blue",
                 v_x=0, v_y=0,
                loc_x=0, loc_y=0):
        """ Setup ball
        :game: game of which we are a part
        """
        self.game = game
        self.radius = radius
        self.color = color
        self.v_x = v_x
        self.v_y = v_y
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.b_t = turtle.Turtle()
        self.b_t.hideturtle()

    def display(self):
        """ Display ball
        """
        self.b_t.clear()
        self.b_t.up()
        self.b_t.goto(self.loc_x, self.loc_y)
        self.b_t.down()
        self.b_t.dot(self.radius*2, self.color)
        self.b_t.up()

    def update(self):
        """ Update ball, e.g. position
        """
        print("ball.update()")

        self.game.ball_edge_check()
        self.loc_x += self.v_x*self.game.update_time
        self.loc_y += self.v_y*self.game.update_time
        self.display()

        

class BouncingBallGame:
    def __init__(self, update_time=.01):
        """ Do bouncing ball
        :update_time: Our update loop time
        """
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
        self.ball = Ball(self, radius=100, color="red",
                         v_x=200, v_y=500)
        

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
        self.ball.update()
        self.ball.display()

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
ut = .1    # Slow down for development
bg = BouncingBallGame(update_time = ut)
bg.run()
