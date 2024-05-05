#canvas_time.py    24Oct2022  crs
import tkinter as tk
import math
import time
import random

from my_ball import MyBall

mw = tk.Tk()

# Establish sizes
cv_width = 300          # canvas size
cv_height = cv_width*2

colors = ["red","orange","yellow","green",
          "blue", "indigo","violet"]
        
# Coordinates within drawing area
x_min = cv_width*.05
x_max = cv_width*.95
x_range = (x_max-x_min)
x_mid = (x_min+x_max)/2
y_min = cv_height*.1
y_max = cv_height*.95
y_mid = (y_min+y_max)/2
y_range = abs(y_max-y_min)
ball_r = min(x_range,y_range)/2 * .2

balls = {}  # Balls is system by tag

vx = x_range/3     # velocity (pixel/sec)
vy = 4*vx
delta_time = .01
def find_ball_space(balls=balls, r=ball_r, max_try=100):
    """ Find a place for a new ball
        First try - keep trying random locations
                    untill found or max_try attempts
    :balls: list of balls in play
    :r: radius of ball
    :max_try: Number of tries till fail default: 100
    :returns: x,y or last x,y if none found
    """
    while True:
        x = random.randint(x_min+r, x_max-r)
        y = random.randint(y_min+r, y_max-r)
        min_dist = min(x_range,y_range)
        if balls is not None and len(balls) > 0:
            for ball in balls.values():
                dist = math.sqrt((x-ball.x)**2+(y-ball.y)**2)
                if dist < 2*r:
                    break       # Not suitable
            else:
                return x,y      # Acceptable
        return x,y          # give last try
    
    
p_ball_collision_proc = None    # For forward ref
def add_balls(n=1,color=None, colors=colors, balls=None):
    """ Add balls to space
    :n: number ofballs to add
    :color: preferred color
    :colors: list of colors to use, if no preferred color
    :balls: dictionary to which balls are added
    """
    for i in range(n):
        colr = color
        if color is None:
            colr = colors[i%len(colors)]
        x,y = find_ball_space(balls=balls, r=ball_r)
        
        ball = MyBall(canvas, x=x,y=y, color=colr,
                    x_min=x_min,x_max=x_max,
                    y_min=y_min,y_max=y_max,
                    vx=vx, vy=vy, r=ball_r,
                    ball_collision_proc=p_ball_collision_proc,
                    delta_time=delta_time,
                    balls=balls)
        balls[ball.tag] = ball
        ball.start()

def ball_collision_proc(ball,ball2):
    """ Process ball-ball collision
    :ball: ball (us) colliding
    :ball2: ball with which we are colliding
    """
    tag = ball.tag
    ball.stop()
    if tag is not None:
        if tag in ball.balls:
            ball.balls.pop(tag)
            add_balls(color=ball.color, balls=ball.balls)
    if len(ball.balls) < 2:
        add_balls(n=6, colors=colors, balls=ball.balls)
p_ball_collision_proc = ball_collision_proc

# Add drawing area
canvas = tk.Canvas(mw, width=cv_width, height=cv_height)
canvas.pack()
             
# Add Title Text    
canvas.create_text(x_mid, y_min/2,
                text="Balls controlled by events",
                font=20, fill="black")

# Create balls
nballs = len(colors)

add_balls(n=nballs, colors=colors, balls=balls)
# Start all
for ball in list(balls.values()):
    ball.start()

        
mw.mainloop()
