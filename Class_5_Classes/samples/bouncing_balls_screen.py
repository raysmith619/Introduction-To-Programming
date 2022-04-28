# bouncing_balls_screen.py  17Feb2022  crs, Author
"""
Demonstration of class/object usage
in depicting bouncing ball(s)
Screen class
"""
import turtle
from random import randint
import time

class BouncingBallScreen:
    def __init__(self,
        tu,
        window_width=800,
        window_height=800,
        x_edge_min=None,
        x_edge_max=None,
        y_edge_min=None,
        y_edge_max=None,
        ):
        """ Create screen based on turtle
        NOTE: We are using turtle default of 0,0 at center
        :tu: turtle object
        :window_width: width of window default: 800
        :window_height: height of window default: 800
        :x_edge_min: minimum x edge default: -window_width/2
        :y_edge_min: minimum y edge default: -window_height/2
        """
        self.tu = tu
        self.window_width = window_width
        self.window_height = window_height
        if x_edge_min is None:
            x_edge_min = -window_width/2
        self.x_edge_min = x_edge_min
        if x_edge_max is None:
            x_edge_max = window_width/2
        self.x_edge_max = x_edge_max
        if y_edge_min is None:
            y_edge_min = -window_height/2
        self.y_edge_min = y_edge_min
        if y_edge_max is None:
            y_edge_max = window_height/2
        self.y_edge_max = y_edge_max
        screen = tu.Screen()
        self.screen = screen
        screen.setup(window_width, window_height)   # Window size.
        screen.tracer(0)        # Turn-off animation.
        self.nt = 1                  # Number of seconds to travers screen
        self.update_loop_time = .01   # Our update loop time

        tu.hideturtle()
        self.running = True
        ### Setup access to enable window closing
        self.canvas = tu.getcanvas()
        self.root = self.canvas.winfo_toplevel()
        """
        Enable clicking window close to do
        clean program stop
        """
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)    

    def screen_update(self):
        """ Update screen display
        """
        #print("screen_update")
        self.screen.update()     # In each while loop, refresh the screen with the new drawing.

    def on_close(self):
        """ Stop display loop and close window
        """
        self.running = False
        print("Stopping display")
        self.root.destroy()
    

if __name__ == '__main__':
    
    bs = BouncingBallScreen(turtle)
    while bs.running:
        bs.screen_update()
