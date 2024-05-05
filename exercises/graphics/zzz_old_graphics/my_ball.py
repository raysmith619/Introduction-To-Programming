# my_ball.py    27Oct2022  crs, split from canvas_time.py
# MyBall
# event time (tk.after)
#
import math

class MyBall:
    tag_prefix = "Ball_"
    tag_no = 0
    def __init__(self, canvas, x=0, y=0, r=100,
                x_min=None,x_max=None,
                y_min=None,y_max=None,
                color="blue", width=2,
                ball_collision_proc=None,
                vx = None,     # velocity (pixel/sec)
                vy = None,
                delta_time = .01,   # time step in seconds
                tag=None,
                balls={},
                running=True):
        """ Setup initial MyBall
        :canvas: canvas widget
        :x: center x-coordinate
        :y: center y-coordinate
        :r: radius radius default: 100
        :n: number of spokes default: 10
        :color: color default: "blue"
        :ball_collision_proc: process ball-ball
            collision: default: delete us
        :width: spoke line width default: 2
        :vx: x-velocity pixel/sec
        :vy: y-velocity pixel/sec
        :delta_time: time step in seconds
        :tag: object's components tag default: generated
        :running: ball is running default: True
        :balls: dictionary (by tag) of balls used for ball collision
                detection
        """
        self.star_legs = []
        self.canvas = canvas
        self.x = x
        self.y = y
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.r = r
        self.delta_time = delta_time
        self.color = color
        self.ball_collision_proc = ball_collision_proc
        self.width = width
        self.vx = vx
        self.vy = vy
        if tag is None:
            MyBall.tag_no += 1
            tag = f"{MyBall.tag_prefix}{MyBall.tag_no}"
        self.tag = tag
        self.running = running
        self.balls = balls
        x1 = x - self.r
        y1 = y - self.r
        x2 = x + self.r
        y2 = y + self.r
        self.tag_no = self.canvas.create_oval(x1,y1,x2,y2,
                                fill=self.color,
                                tag=self.tag)

    def move_to(self, x=None, y=None):
        """ Move MyBall to new place
        :x: new x-coordinate default: keep old x
        :y: new y-coordinate default: keep old y
        """
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        x_chg = x - self.x
        y_chg = y - self.y
        if self.tag is not None:
            self.canvas.move(self.tag, x_chg, y_chg)
        ###print(f"move_to({x:.0f},{y:.0f})"
        ###      f" chg:{x_chg:.0f},{y_chg:.0f}")
        self.x = x  # Update location
        self.y = y

    def start(self):
        """ Start activity
        """
        self.running = True
        self.update()

    def stop(self):
        """ Stop running, delete canvas object
        """
        if self.tag is not None:
            self.canvas.delete(self.tag)
        if self.tag is not None:
            if self.tag in self.balls:
                del self.balls[self.tag]

            
    def collision_check(self):
        """ Check for and update if collsion
        """
        if not self.running:
            return          # No checking after we're stopped
        # Simple ball-ball
        # destroy ball if colliding with another
        for ball_key in self.balls:
            if ball_key == self.tag:
                continue        # Don't check against us
            
            ball = self.balls[ball_key]
            dist = math.sqrt((self.x-ball.x)**2
                             +(self.y-ball.y)**2)
            if dist <= self.r+ball.r:
                if self.ball_collision_proc is not None:
                    self.ball_collision_proc(self,ball)
                else:
                    self.canvas.after(0,self.stop)
                return
            
        if self.vx > 0 and self.x > self.x_max-self.r:
            self.vx = -self.vx
        if self.vx < 0 and self.x < self.x_min+self.r:
            self.vx = -self.vx
        if self.vy > 0 and self.y > self.y_max-self.r:
            ###print(f"self.vy:{self.vy:.0f} self.y:{self.y:.0f}")
            if self.vy > 0: # Only if still going to edge
                self.vy = -self.vy
        if self.vy < 0 and self.y < self.y_min+self.r:
            self.y = self.y_min+self.r  # place at edge
            ###print(f"self.vy:{self.vy:.0f} self.y:{self.y:.0f}")
            if self.vy < 0: # Only if still going to edge
                self.vy = -self.vy
        delta_x = self.delta_time*self.vx
        delta_y = self.delta_time*self.vy
        new_x = self.x+delta_x
        new_y = self.y+delta_y
        self.move_to(x=new_x, y=new_y)
        

    def update(self):
        """ Update object
        """
        self.collision_check()
        self.canvas.update()    # DBG - show display
        self.canvas.after(
                 int(self.delta_time*1000),
                 self.update)
