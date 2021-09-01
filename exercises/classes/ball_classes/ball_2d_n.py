#ball_2d_n.py  12Aug2021  crs, from ball_2d_n.py
"""
Two dimentional ball
with number
"""
class Ball2dN:
    def __init__(self, number=None,
                 color="black", fill=None,
                 radius=1,
                 pos_x=0, pos_y=0,
                 vel_x=0, vel_y=0,
                 time_prev=0):
        """ Define/Setup Ball's attributes
        :number: ball number
                default: REQUIRED for now. In the
                        future we might generate
                        the number based on what
                        balls are currently available
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
        if number is None:
            print("REQUIRED ball number is missing")
            exit()
        self.number = number
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
        ball_str = f"Ball2dN: {self.number} {self.color}"
        ball_str += f" r:{self.radius}"
        ball_str += f" x:{self.pos_x} y:{self.pos_y}"
        ball_str += f" vx:{self.vel_x} vy:{self.vel_y}"
        if self.fill is not None:
            ball_str += f" filled:{self.fill}"
        return ball_str
        
    def set_pos(self, x=None, y=None):
        """ Add to position
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
        """ Add to position
        :x_inc: add to x coordinate/position
            default: don't change x position
        :y_inc: add to y coordinate/position
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
    b1 = Ball2dN(number=1)
    b2 = Ball2dN(number=9, color="blue", fill="blue", radius=3,
                pos_x=2, pos_y=4)
    b3 = Ball2dN(number=15, color="red", radius=2, vel_x=2, vel_y=3)
    for i in range(4):
        print(f"{i:4}\n\tb1: {b1}\n\tb2: {b2}\n\tb3: {b3}")
        b1.new_time()
        b2.new_time()
        b3.new_time()
        b2.add_pos(x=1, y=2)
        
r'''
>>> 
= RESTART: C:/Users/raysm/workspace/python/
IntroductionToProgramming/exercises/classes/
ball_classes/ball_2d_n.py
   0
	b1: Ball2dN: 1 black r:1 x:0 y:0 vx:0 vy:0
	b2: Ball2dN: 9 blue r:3 x:2 y:4 vx:0 vy:0 filled:blue
	b3: Ball2dN: 15 red r:2 x:0 y:0 vx:2 vy:3
   1
	b1: Ball2dN: 1 black r:1 x:0 y:0 vx:0 vy:0
	b2: Ball2dN: 9 blue r:3 x:3 y:6 vx:0 vy:0 filled:blue
	b3: Ball2dN: 15 red r:2 x:2 y:3 vx:2 vy:3
   2
	b1: Ball2dN: 1 black r:1 x:0 y:0 vx:0 vy:0
	b2: Ball2dN: 9 blue r:3 x:4 y:8 vx:0 vy:0 filled:blue
	b3: Ball2dN: 15 red r:2 x:4 y:6 vx:2 vy:3
   3
	b1: Ball2dN: 1 black r:1 x:0 y:0 vx:0 vy:0
	b2: Ball2dN: 9 blue r:3 x:5 y:10 vx:0 vy:0 filled:blue
	b3: Ball2dN: 15 red r:2 x:6 y:9 vx:2 vy:3
>>>'''
