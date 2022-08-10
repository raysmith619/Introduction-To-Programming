#ball_2d.py  29Jul2022  crs, Author
"""
Two dimentional ball, using turtle.Vec2D
position, velocity represented as vectors
"""
import turtle as tu
import time

class Ball2D:
    """ Two dimentioal ball
    """
    ball_id = 0             # Unique ball id
    color_prev = "blue"
    color_index = 0
    colors = ["red", "orange", "yellow",
              "green", "blue", "indigo",
              "violet"]
    time_base = time.time()
    track_ball = False
    
    @classmethod
    def set_track(level=True):
        Ball2D.track_ball = level
        
    def __init__(self, x=0,y=0, vx=0, vy=0,
                 r=None, color=None):
        """ Initialize ball
        :x: position x pixels default: 0
        :y: position y  pixels default: 0
        :vx: velocity x in pixel per second
        :vy: velocity y in pixel per second
        :r: radius pixels default: previous [100]
        :color: color default: previous ["blue"]
        """
        self.tur = tu.Turtle()
        self.tur.hideturtle()
        self.ball_id = Ball2D.ball_id
        Ball2D.ball_id += 1
        self.ball_id = Ball2D.ball_id
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        if r is None:
            r = Ball2D.r_prev
        Ball2D.r_prev = self.r = r
        if color is None:
            color = Ball2D.color_prev
        Ball2D.color_prev = self.color = color    
        self.time_prev = self.time = None

    def __str__(self):
        """ String representation, mostly for
            debugging / diagnostic use
        """
        st = f"Ball2D[{self.ball_id}]: x:{self.x:.3f} y:{self.y:.3f}"
        st += f" vx:{self.vx:.3f} vy:{self.vy:.3f}"
        st += f" {self.color}"
        return st

    def reset(self):
        """ Reset ball info
        """
        self.tur.reset()
        
    def display(self):
        """Display ball
        """
        tur = self.tur
        ne = tur.undobufferentries()    # Remove previous display
        for i in range(ne):             # by undoing all actions
            tur.undo()
        tur.hideturtle()    # Looks like undo shows turtle
        tur.penup()
        tur.goto(x=self.x, y=self.y)
        tur.pendown()
        tur.color(self.color)
        tur.dot(2*self.r, self.color)

    def update(self):
        """ Update ball state based on velocity, position
        Assuming no collision adjustments
        """
        self.time = time.time()
        if self.time_prev is None:
            self.time_prev = self.time

        time_delta = self.time-self.time_prev

        prev_x = self.x
        prev_y = self.y 
        self.x += self.vx*time_delta
        self.y += self.vy*time_delta
        self.time_prev = self.time
        if Ball2D.track_ball:
            print(f"time_delta:{time_delta:.3f} {self}")
            print(f"   chg_x:{self.x-prev_x} chg_y:{self.y-prev_y}")

        
if __name__ == "__main__":
    from random import randint, uniform
    colors = ["red", "orange", "yellow",
              "green", "blue", "indigo",
              "violet"]
    h = 800
    top = h/2
    bottom = -top
    w = h/2
    left = -w/2
    right = -left
    balls = []      # balls
    nballs = 10
    #nballs = 1
    r_max = int(h/20)
    r_min = int(r_max/3)
    v_max = h/500
    v_min = -v_max
    margin = 5      # margin
    for i in range(nballs):
        r = randint(r_min, r_max)
        min_ball_y = int(bottom+r+margin/2)
        max_ball_y = int(top-r-margin/2)
        min_ball_x = int(left+r+margin/2)
        max_ball_x = int(right-r-margin/2)
        
        bx = randint(min_ball_x,max_ball_x)
        by = randint(min_ball_y,max_ball_y)
        vx = uniform(v_min,v_max)
        vy = uniform(v_min, v_max)
        ball = Ball2D(x=bx, y=by, vx=vx, vy=vy, r=r,
                      color=colors[i%len(colors)])
        balls.append(ball)

    for i in range(nballs):
        ball = balls[i]
        print(i, ball)
        ball.display()
    
    # Group actions

    def ball_display():
        for ball in balls:
            ball.display()
        tu.update()


    def ball_update():
        for ball in balls:
            ball.update()


    td_delta = .01
    tbeg = time.time()
    Ball2D.set_track()    # Track ball changes
    while True:
        ninside = 0
        ball_update()
        ball_display()
        if Ball2D.track_ball:
            ts = time.time()
            td = ts-tbeg
            print(f"after balls {td:.3f} Ball[0]:{balls[0]}")
        time.sleep(.01)
