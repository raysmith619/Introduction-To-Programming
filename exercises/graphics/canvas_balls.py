#canvas_balls.py    24Oct2022  crs
"""
Bouncing balls on a canvas
Demonstrates simple bouncing action
"""
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
"""
Ball to ball collision process
 1. Convert velocities (vx,vy) into normal,tangential (vn,vt)
 2. Exchange normal velocities vn2 = vn1_old, vn1 = vn2_old
 3. Convert vn,vt back to new velocities (vx,vy)
 """

def line_to_theta(x1,y1,x2,y2):
    """ Angle(radians) given line x1,y1 to x1,y2
    :x1,y1: beginning x,y-coordinates
    :x2,y2: ending x,y-coordinates
    returns: angle in radians
    """
    theta = math.atan2(y2-y1, x2-x1)
    return theta

def ball_ball_theta(ball,ball2):
    """ angle between ball centers
    """
    theta = line_to_theta(ball.x, ball.y, ball2.x, ball2.y)
    return theta

def ball_v_theta(ball):
    return line_to_theta(0,0, ball.vx, ball.vy)

def ball_ball_vn_vt(ball1,ball2):
    """ velocity normal,tantial pair of two colliding balls
    :ball: our ball
    :ball2: other ball
    :returns:vn_x,vn_y, vt_x,vt_y 
    """
    bb_theta = ball_ball_theta(ball1,ball2)
    v_theta = ball_v_theta(ball1)
    bb_to_v_theta = v_theta-bb_theta
    v_magsq = ball1.vx**2+ball1.vy**2
    v_mag = math.sqrt(v_magsq)
    vn = v_mag*math.cos(bb_to_v_theta)
    vt = math.sqrt(v_magsq-vn**2)
    vn_x = v_mag*math.cos(bb_theta)
    vn_y = v_mag*math.sin(bb_theta)
    bbt_theta = bb_theta + math.pi/4    # t is n + pi/4
    vt_x = v_mag*math.cos(bbt_theta)
    vt_y = v_mag*math.sin(bb_theta)
    return vn_x,vn_y, vt_x,vt_y

def ball_nt_to_xy(ball1,ball2, vn_x, vn_y, vt_x,vt_y):
    """ Convert ball vn, vt to vx,vy
    """
    bb_theta = ball_ball_theta(ball1,ball2)
    v_theta = ball_v_theta(ball1)
    v_to_bb_theta = bb_theta-v_theta
    v_magsq = ball1.vx**2+ball1.vy**2
    v_mag = math.sqrt(v_magsq)
    vx = v_mag*math.cos(v_to_bb_theta)
    vy = math.sqrt(v_magsq-vx**2)     # total = sum of parts
    ball1.vx, ball1.vy = vx,vy
    
def ball_collision_proc(ball,ball2):
    """ Process ball-ball collision
    :ball: ball (us) colliding
    :ball2: ball with which we are colliding
    """
    vn_x,vn_y, vt_x,vt_y = ball_ball_vn_vt(ball,ball2)
    vn2_x,vn2_y, vt2_x,vt2_y = ball_ball_vn_vt(ball2,ball)
    print(f" 1: vx,y:{ball.vx:.0f},{ball.vy:.0f}"
          f", n:{vn_x:.0f},{vn_y:.0f}"
          f" t:{vt_x:.0f},{vt_y:.0f} {ball.color}")
    print(f" 2: vx,y:{ball2.vx:.0f},{ball2.vy:.0f}"
          f", n:{vn2_x:.0f},{vn2_y:.0f}"
          f" t:{vt2_x:.0f},{vt2_y:.0f} {ball2.color}")
    ball.canvas.update()    # For DBG - display
    # Physics: tangential unchanged, normal exchanged
    tmp_vn_x, tmp_vn_y = vn_x,vn_y
    vn_x,vn_y = vn2_x,vn2_y
    vn2_x,vn2_y = tmp_vn_x, tmp_vn_y

    # Convert normal,tangential to vx,vy
    ball_nt_to_xy(ball,ball2, vn_x,vn_y, vt_x,vt_y)
    print("After")
    print(f" 1: vx,y:{ball.vx:.0f},{ball.vy:.0f}"
          f", n:{vn_x:.0f},{vn_y:.0f}"
          f" t:{vt_x:.0f},{vt_y:.0f} {ball.color}")
    ball_nt_to_xy(ball2,ball, vn2_x,vn2_y, vt2_x,vt2_y)
    print(f" 2: vx,y:{ball2.vx:.0f},{ball2.vy:.0f}"
          f", n:{vn2_x:.0f},{vn2_y:.0f}"
          f" t:{vt2_x:.0f},{vt2_y:.0f} {ball2.color}")
    print()    
    
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
