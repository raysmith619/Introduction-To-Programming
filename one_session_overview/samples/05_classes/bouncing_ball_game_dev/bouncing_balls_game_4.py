# bouncing_balls_game_4.py  03Apr2024  crs, from bouncing_balls_3.py
"""
Simple program to demonstrate class development
Usage:
    -- Fleshout BouncingBallGame.ball_edge_check() with physics
        of bouncing balls

History:
    + Display ball
    + Update ball (simple)
    + Edge detection
"""
import time
import turtle

trace_level = 9     # Trace level higher == more
trace_level = 0     # Stop tracing

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
        self.ball_color_index = 4   # Index into colors
        self.colors = ["red", "orange", "yellow"
                  "green", "blue", "indigo", "violet"]
        
        self.game = game
        self.radius = radius
        self.radius_min = 50
        self.radius_max = 200
        self.n_collision = 0 # Number of edge collisions
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
        self.color = self.colors[self.ball_color_index]
        self.b_t.clear()
        self.b_t.up()
        self.b_t.goto(self.loc_x, self.loc_y)
        self.b_t.down()
        self.b_t.dot(self.radius*2, self.color)
        self.b_t.up()

    def update(self):
        """ Update ball, e.g. position
        """
        if trace_level > 0:
            print("ball.update()")

        self.game.ball_edge_check(self)
        self.loc_x += self.v_x*self.game.update_time
        self.loc_y += self.v_y*self.game.update_time
        self.display()

        

class BouncingBallGame:
    def __init__(self, update_time=None,
                 window_width=800, window_height=800):
        """ Do bouncing ball
        :update_time: Our update loop time default: .01
        """
        if update_time is None: # so the caller can force
                                # default by using None
            update_time = .01
        self.update_time = update_time
        self.running = True
        self.x_edge_min = -window_width/2
        self.x_edge_max = window_width/2
        self.y_edge_min = -window_height/2
        self.y_edge_max = window_height/2
        screen = turtle.Screen()
        screen.setup(window_width, window_height)   # Window size.
        screen.tracer(0)        # Turn-off animation.
        
    
    def run(self):
        self.start_ball()            # Setup ball inital properties
        while self.running:
            time.sleep(self.update_time)
            self.screen_update()

    def start_ball(self):
        """ Setup ball, size, position, velocity
        """
        if trace_level >= 0:
            print("start_ball()")
        self.ball = Ball(self, radius=100, color="red",
                         v_x=200, v_y=500)
        

    def ball_display(self):
        """ Display ball
        """
        if trace_level > 0:
            print("ball_display()")
        self.ball.display()

    def ball_edge_check(self, ball):
        """ Adjust motion if/when edge touched
            Simple physics of edge collision says
                The velocity perpendicular to the
                collision edge is reversed.
        :ball: ball (class Ball) to check
        """
        if trace_level > 0:
            print("ball_edge_check()")
    
        # -- basic bouncing ball physics
        if ball.v_x > 0:        # Going right
            if ball.loc_x > self.x_edge_max-ball.radius:
                ball.v_x = -ball.v_x
        elif ball.v_x < 0:        # Going left
            if ball.loc_x < self.x_edge_min+ball.radius:
                ball.v_x = -ball.v_x
        if ball.v_y > 0:        # Going up
            if ball.loc_y > self.y_edge_max-ball.radius:
                ball.v_y = -ball.v_y
        elif ball.v_y < 0:        # Going down
            if ball.loc_y < self.y_edge_min+ball.radius:
                ball.v_y = -ball.v_y


    def ball_update(self):
        """ Update ball
            Includes handeling edge collisions
        """
        if trace_level > 0:
            print("ball_update()")
        self.ball.update()
        self.ball.display()

    def screen_update(self):
        """ Update screen display
        """
        if trace_level > 0:
            print("screen_update()")
        self.ball_update()
        screen.update()     # In each while loop, refresh the screen with the new drawing.


"""
Run our own loop
"""
ut = None   # Use the default (internal) time
#ut = .1    # Slow down for development
bg = BouncingBallGame(update_time = ut)
bg.run()
