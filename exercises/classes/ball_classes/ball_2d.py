#ball_2d.py  12Aug2021  crs, Author
"""
Two dimentional ball
"""
class Ball2d:
    def __init__(self, color="black", fill=None,
                 radius=1,
                 pos_x=0, pos_y=0,
                 vel_x=0, vel_y=0,
                 time_prev=0):
        """ Define/Setup Ball's attributes
        :color: ball's color default: black
        :fill: ball fill color
                default: not filled
                "" -> same as color
        :radius: radius in default units
                default: 1
        :pos_x: x (horizontal right) in default units
                default: 0
        :pos_y: y (vertical down) in default units
                default: 0
        :vel_x: x (horizontal right) default
                    units, default time inc
                default: 0
        :vel_y: y (vertical down)
                default: 0
        :prev_time: Time of previous activity
                    in default time inc
                default: 0
        """
        self.color = color
        self.fill = fill
        self.radius = radius
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.time_prev = time_prev
        
    def __str__(self):
        """ String representation of ball
        """
        ball_str = f"Ball2d:{self.color}"
        ball_str += f" r:{self.radius}"
        ball_str += f" x:{self.pos_x} y:{self.pos_y}"
        ball_str += f" vx:{self.vel_x} vy:{self.vel_y}"
        if self.fill is not None:
            ball_str += f" filled:{self.fill}"
        return ball_str
        
    def set_pos(self, x=None, y=None):
        """ Set to position
        :x: set x coordinate/position
            default: don't change x position
        :y: set y coordinate/position
            default: don't change y position
        """
        if x is not None:
            self.pos_x = x
        if  y is not None:
            self.pos_y = y 
        
    def add_pos(self, x=None, y=None):
        """ Add offset to current position
        :x: add to x coordinate/position
            default: don't change x position
        :y: add to y coordinate/position
            default: don't change y position
        """    
        if x is not None:
            self.pos_x += x
        if y is not None:
            self.pos_y += y
        
    def set_vel(self, x=None, y=None):
        """ Set velocity
        :x: set x velocity
            default: don't change x velocity
        :y: set y velocity
            default: don't change y position
        """
        if x is not None:
            self.vel_x = x
        if y is not None:
            self.vel_y = y 
        
    def add_vel(self, x=None, y=None):
        """ Add to position
        :x_inc: add to x velocity
            default: don't change x velocity
        :y_inc: add to y velocity
            default: don't y velocity
        """    
        if x_inc is not None:
            self.vel_x += x
        if y_inc is not None:
            self.vel_y += y

    def new_time(self, time=None):
        """ Adjust per new time
        :time: New time in units of default time inc
                default: add one to previous time
        """
        if time is None:
            time = self.time_prev + 1
        time_delta = time - self.time_prev
        if time_delta != 0:
            self.pos_x += (self.vel_x*time_delta)
            self.pos_y += (self.vel_y*time_delta)
        self.time_prev = time    # Record time
        
# Self Test
if __name__ == "__main__":
    b1 = Ball2d()
    b2 = Ball2d(color="blue", fill="blue", radius=3,
                pos_x=2, pos_y=4)
    b3 = Ball2d(color="red", radius=2, vel_x=2, vel_y=3)
    for i in range(4):
        print(f"{i:4}\n\tb1: {b1}\n\tb2: {b2}\n\tb3: {b3}")
        b1.new_time()
        b2.new_time()
        b3.new_time()
        b2.add_pos(x=1, y=2)
        
