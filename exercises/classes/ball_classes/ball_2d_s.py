#ball_2d_s.py  11Oct2021  crs, Author
"""
Simple ball action
Uses turtle for display
"""
import turtle
import random

from pgm_time import PgmTime

from ball_2d_n import Ball2dN

tracing = False    # True - trace action

class Ball2dS:
    def __init__(self, update_time=.1,
                 update_fun=None):
        """ Support simple ball action
        """
        self.raise_move = True # raise pen on move
        self.pt = PgmTime()
        self.balls_d = {}     # Hash by unique id
        self.tu = turtle.Turtle()
        self.update_time = update_time
        self.update_fun = update_fun
        turtle.ontimer(self.update, int(self.update_time*1000))
        self.tu.speed(0)    # Instantaneous move
        
    def __str__(self):
        """ String representation of ball
        """
        ball_str = f"Ball2dS:{self.balls}"
        return ball_str
        
    def add_ball(self, ball):
        """ Add ball to list
            Adds unique id to ball
        :ball: ball to add
        """
        self.balls_d[ball.id] = ball

    def new_time(self, time=None):
        """ Adjust each ball per new time
        :time: New time in units of default time inc
                default: add one to previous time
        """
        for ball_id in self.balls_d:
            ball = self.balls_d[ball_id]
            ball.new_time(time)

    def display_ball(self, ball):
        x = ball.pos_x
        y = ball.pos_y
        radius = ball.radius
        color = ball.color
        if tracing:
            print(f"{self.pt.pt()}: display_ball:{ball}")
        tu = self.tu
        if self.raise_move:
            isdown = tu.isdown()
            if isdown:
                tu.penup()     # raise pen if down
        tu.goto(x,y)
        tu.dot(radius, color)
        if self.raise_move:
            if not isdown:
                tu.pendown()    # return pen state
        

        
    def display(self):
        """ Display all balls
        """
        if tracing:
            print(f"{self.pt.pt()}: display:")
        for ball_id in self.balls_d:
            ball = self.balls_d[ball_id]
            self.display_ball(ball)

    def update(self):
        """ Update scene
        """
        self.new_time()
        self.display()
        if self.update_fun is not None:
            self.update_fun()
        turtle.ontimer(self.update,
                       int(self.update_time*1000))
            
# Self Test
if __name__ == "__main__":
    radius = 5
    starts_xy_d = {}  # starting(x,y) by ball_id
    width = 1200
    height = 1200
    update_time = .01  # Display update time in seconds
    vel_mult = .1    # Velocity multiplier
    colors = ["red","orange", "yellow",
              "green", "blue", "indigo",
              "violet"]
    def update_fun():
        """ Remove balls which cross center,
        i.e., positions change sign
        """
        #print("update_fun")
            
        ids = list(starts_xy_d)
        if len(ids) == 0:
            print("Balls all gone!")
            exit()
            
        for ball_id in ids:
            start_x, start_y = starts_xy_d[ball_id]
            ball = bs.balls_d[ball_id]
            if ((ball.pos_x > 0 and start_x > 0)
                or (ball.pos_x < 0 and start_x < 0)
                ):
                pass
            else:
                print(f"Ball:{ball} done")
                del bs.balls_d[ball_id] # gone past - Remove
                del starts_xy_d[ball_id]
                
    bs = Ball2dS(update_time=update_time,
                 update_fun=update_fun)
    for i in range(7):
        color = colors[i%len(colors)]
        irad = radius*(i+1)
        b_vel_mult = random.uniform(.5*vel_mult,
                                             vel_mult)
        x_min = -i*radius-width/2
        x_max = i*radius+width/2
        x = random.randint(x_min, x_max)
        vel_x = -x*b_vel_mult
        y_min = -i*radius-width/2
        y_max = i*radius+width/2
        y = random.randint(y_min, y_max)
        vel_y = -y*b_vel_mult
        ball = Ball2dN(radius=irad, color=color,
                       pos_x=x, pos_y=y,
                       vel_x=vel_x, vel_y=vel_y)
        bs.add_ball(ball)       # Note: adds ball.id
        starts_xy_d[ball.id] = (x,y)
    turtle.mainloop()
