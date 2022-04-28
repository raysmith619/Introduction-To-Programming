# firework_group.py  04MaR2022  crs, from fireworks.py
"""
FireworkGroup - group of fireworks
"""
import turtle as tu
from random import randint, uniform
import time

from firework import Firework

class FireworkGroup:
    """ Fireworks group
    """
    def __init__(self, window_width=800, window_height=None,
                 x_min=None, x_max=None,
                 y_min=None, y_max=None,
                 size_min=None, size_max=None,
                 boarder=None,
                 colors=None,
                 update_time = .01,
                 n_fwork = 10):
        """ Fireworks group
        :window_width: window width in pixels default: 800
        :window_height: window height in pixels
                        default: window_height
        :x_min: minimum for object default: - calculated
        :x_max: minimum for object default: - calculated
        :y_min: minimum for object default: - calculated
        :y_max: maximum for object default: - calculated
        :size_min: min fw size default: - calculated
        :size_max: max fw size default: - calculated
        :boarder: free area from edge default: calculated
        :colors: list of colors to  use
                default: rainbow + black + gray
        :n_fwork: number of fireworks default: 10
        :update_time: display update time(sec) default:.01
        """
        self.window_width = window_width
        if window_height is None:
            window_height = window_width
        self.window_height = window_height
        window_size = min(window_width, window_height)
        self.window_size = window_size
        if x_min is None:
            x_min = -window_width/2
        self.x_min = x_min
        if x_max is None:
            x_max = window_width/2
        self.x_max = x_max
        if y_min is None:
            y_min = -window_height/2
        self.y_min = y_min
        if y_max is None:
            y_max = window_height/2
        self.y_max = y_max
        print(f"window_width:{window_width} window_height:{window_height}")
        print(f"x_min:{x_min} y_min:{y_min}")
        print(f"y_max:{y_max} y_max:{y_max}")
        if boarder is None:
            boarder = min((x_max-x_min),(y_max-y_min))/10
        self.boarder = boarder
        if colors is None:
            colors = ["red", "orange", "yellow",
                      "green", "blue", "indigo", "violet",
                      "gray", "black", "pink"]
        self.colors = colors
        self.update_time = update_time      # Our update event time
        self.running = False                # True -> updating
        
        if size_min is None:
            size_min = window_size*.05
        self.size_min = size_min
        if size_max is None:
            size_max = window_size/n_fwork
        self.size_max = size_max
        self.n_fwork = n_fwork
        self.update_time = update_time
        self.setup()
        
    def update(self):
        """ Up fireworks and redisplay
        """
        if not self.running:
            return

        for fw in self.firework_list:
            fw.update() 
        tu.clear()                 # Clear whole display
        for fw in self.firework_list:
            fw.display()
        tu.ontimer(self.update, int(self.update_time*1000))  # reprime
        
        
    def start(self):
        """ Startup all fire works
        """
        self.running = True      # Signal we are running    
        tu.ontimer(self.update, int(self.update_time*1000))

    def setup(self):
        """ Create fireworks
        """
        tu.speed("fastest")        # 0 - fastest drawing - no delay
        tu.hideturtle()
        tu.penup()
        self.screen = tu.Screen()
        self.screen.setup(self.window_width,
                          self.window_height)   # Window size.
        self.screen.tracer(0)               # Turn-off animation.
  

        self.firework_list = []
        for i in range(self.n_fwork+1):
            firework = self.new_firework()
            self.firework_list.append(firework)

    def new_firework(self):
        """ Create new (random) firework
        :returns: random Firework object
        """
        fw_size = uniform(self.size_min, self.size_max)
        boarder = fw_size*1.1
        x = uniform(self.x_min+self.boarder,
                    self.x_max-self.boarder)
        y = uniform(self.y_min+boarder,
                    self.y_max-boarder)
        #print(f"x:{x} y:{y}")
        color = self.colors[randint(0,len(self.colors)-1)]

        firework = Firework(self, x=x, y=y,
                            size=fw_size, color=color)
        return firework
    
    def mainloop(self):
        """ Link to turtle mainloop
        """
        tu.mainloop()


""" Self testing
"""
if __name__ == "__main__":
    fwg = FireworkGroup(n_fwork=10)
    fwg.start()

    fwg.mainloop()
    
    
