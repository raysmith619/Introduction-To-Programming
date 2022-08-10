#ball_table_2d.py  30Jul2022  crs, Author
"""
Two dimentional ball table, using turtle
"""
import time
from random import randint, uniform
import turtle as tu
from ball_2d import Ball2D
from edge_2d import Edge2D
from ball_collision_2d import BallCollision2D

class BallTable2D:
    """ Two dimentioal ball table
    """
    tu.tracer(0)
    tu.hideturtle()
    def __init__(self, x=0,y=0, w=400, h=800,
                 balls=None,
                 color="blue",
                 edge_color=None,
                 t_update=1.e-12):
        """ Initialize table
        :x: center position x pixels default: 0
        :y: center y  pixels default: 0
        :w: width default: 400
        :h: height default: 800
        :color: table color default:"blue"
        :edge_color: edge color default: color
        :balls: list of balls (Ball2D) default: None
        :t_update: time update default
                    default: 1.e-12 seconds
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.x_min = x - w/2    # Record edges
        self.x_max = x + w/2
        self.y_min = y - h/2
        self.y_max = y + h/2
        self.v_max = h/5
        self.v_min = -self.v_max
        self.table_changed = True  # Table view changed
        self.color = color
        if edge_color is None:
            edge_color = self.color
        self.edge_color = edge_color
        if balls is None:
            balls = []
        self.balls = balls
        self.t_update = t_update
        self.bcoll = BallCollision2D(balls)
        self.setup_table()
        
    def __str__(self):
        """ String representation, mostly for
            debugging / diagnostic use
        """
        st = f"BallTable2D: x:{self.x} y:{self.y}"
        st += f" w:{self.w}"
        st += f" h:{self.h}"
        st += f" {self.color}"
        if len(self.balls) == 0:
            st += " Empty"
        else:
            st += f" {len(self.balls)} balls"
        return st

    def add_ball(self,ball):
        """ Add ball to table
        :ball: ball (Ball2D) to add
        """
        self.balls.append(ball)

    def ball_collision_update(self):
        self.bcoll.ball_collision_update()
        
    def display(self):
        """Display table plus balls, if any
        """
        if self.table_changed:
            self.display_table()
            self.table_changed = False
        for ball in self.balls:
            ball.display()
        tu.update()
        
    def edge_collision(self, ball):
        """ Check if ball is colliding with
        an edge currently only vertical, horizontal edges
        :ball: ball to check
        :returns: 0 - no collision
                    1 - top, 2-right, 3-bottom, 4-left
        """
        if ball.y >= self.y_max-ball.r:
            return 1    # Top

        if ball.x >= self.x_max-ball.r:
            return 2    # Right

        if ball.y <= self.y_min+ball.r:
            return 3    # Bottom

        if ball.x <= self.x_min+ball.r:
            return 4    # Left

        return 0        # No edge collision

    def delete_ball(self,ball):
        """ Delete ball from balls
            One can do better. How?
        ":ball: ball to delete
        """
        new_list = []
        for b in self.balls:
            if ball.ball_id != b.ball_id:
                new_list.append(b)
            else:
                b.tur.clear()
        self.balls = new_list
        
    def delete_balls(self, balls):
        """ Delete zero or more balls from table
            One can do better. How?
        :balls: list of balls to delete
        """
        for ball in balls:
            self.delete_ball(ball)

    def display_table(self):
        """ Display table part, edges, surface,
            pockets, if any.
        """
        tu.color(self.edge_color, self.color)
        tu.begin_fill()
        for edge in self.edges:
            edge.display()
        tu.end_fill()

    def edge_collision_update(self, ball):
        """ Check for edge collision
            Update ball if appropriate
        :ball:  ball to check
        """
        coll_no = self.edge_collision(ball)
        if coll_no == 0:
            return

        if coll_no == 1:   # Top
            if ball.vy > 0:     # Only if still going to edge
                ball.vy = -ball.vy
            ball.y = self.y_max-ball.r
        elif coll_no == 2:   # Right
            if ball.vx > 0:
                ball.vx = -ball.vx
            ball.x = self.x_max-ball.r
        elif coll_no == 3:  # Bottom
            if ball.vy < 0:
                ball.vy = -ball.vy
            ball.y = self.y_min+ball.r
        elif coll_no == 4:  # Left
            if ball.vx < 0:
                ball.vx = -ball.vx
            ball.x = self.x_min+ball.r 
        
    def place_ball(self, ball):
        """ Place ball on table
        :ball: ball to place
        """
        self.add_ball(ball)
            
    def setup_table(self):
        """ Setup table space
        """
        edges = []      # Setup table edges
        left = self.x - self.w/2
        right = self.x + self.w/2
        top = self.y + self.h/2
        bottom = self.y - self.h/2
        etop = Edge2D(x1=left, y1=top, x2=right, y2=top,
                    width=10, color=self.edge_color)
        edges.append(etop)
        eright = Edge2D(x1=right, y1=top, x2=right, y2=bottom)
        edges.append(eright)
        ebottom = Edge2D(x1=right, y1=bottom, x2=left, y2=bottom)
        edges.append(ebottom)
        eleft = Edge2D(x1=left, y1=bottom, x2=left, y2=top)
        edges.append(eleft)
        self.edges = edges

    def update(self):
        """ Update table state
            no display here
        """
        for ball in self.balls:
            self.edge_collision_update(ball)
            ball.update()
        self.ball_collision_update()    
        
if __name__ == "__main__":
    from random import randint
    colors = ["red", "orange", "yellow",
              "green", "blue", "indigo",
              "violet"]
    x = 400
    top = x
    bottom = -x
    left = -x
    right = x
    balls = []      # balls
    nballs = 10
    #nballs = 3
    tlen = top-bottom
    twid = tlen/2
    tleft = -twid/2
    tright = twid/2
    r = tlen/(9*12/(2.25/2))    # Scall to 9ft table,2.25" ball
    r *= 4          # Expand for viewing
    #r *= 2         # Expand more for 3 balls
    margin = 0      # margin
    tbl = BallTable2D(h=tlen, w=twid, color="pale green")
    for i in range(nballs):
        min_ball_y = int(bottom+r+margin)
        max_ball_y = int(top-r-margin)
        min_ball_x = int(tleft+r+margin)
        max_ball_x = int(tright-r-margin)
        vx = uniform(tbl.v_min, tbl.v_max)
        vy = uniform(tbl.v_min, tbl.v_max)
        bx = randint(min_ball_x,max_ball_x)
        by = randint(min_ball_y,max_ball_y)
        ball = Ball2D(x=bx, y=by, r=r,
                      vx=vx, vy=vy,
                      color=colors[i%len(colors)])
        tbl.place_ball(ball)
    tbl.display()
    

    """
    Enable clicking window close to do
    clean program stop
    """
    ### Setup access to enable window closing
    canvas = tu.getcanvas()
    root = canvas.winfo_toplevel()
    running = True          # Set False to stop loop
    def on_close():
        """ Stop display loop and close window
        """
        global running
        running = False
        time.sleep(.1)       # Give time to wind down
        print("Stopping display")
        root.destroy()
        print("Window destroyed")
    
    root.protocol("WM_DELETE_WINDOW", on_close)
    
    td_delta = tbl.t_update     # Seconds
    def update():
        if running:
            tbl.display()
            tbl.update()
            tu.ontimer(update,t=int(td_delta*1000))
        else:
            print("running stopped")

    update()    # start controled looping
    tu.done()    # Catch first update return




