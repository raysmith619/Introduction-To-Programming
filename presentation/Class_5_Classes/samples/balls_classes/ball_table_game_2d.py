#ball_table_game_2d.py  30Jul2022  crs, Author
"""
Two dimentional ball table game, using turtle
"""
from random import randint, uniform
import turtle as tu
from ball_2d import Ball2D
from edge_2d import Edge2D
from ball_table_2d import BallTable2D

class BallTableGame2D:
    """ Two dimentioal ball table game
    """
    def __init__(self, x=0,y=0, w=400, h=800,
                 balls=None,
                 color="green",
                 update_time=.01):
        """ Initialize game
        :x: center position x pixels default: 0
        :y: center y  pixels default: 0
        :w: width default: 400
        :h: height default: 800
        :color: color default: "green"
        :balls: list of balls (Ball2D) default: None
        :update_time: in seconds default:.01
        """
        self.table = BallTable2D(x=x, y=y, w=w, h=h)
        self.update_time = update_time
        
    def add_ball(self, ball):
        """ Add ball to game
        :ball: ball(Ball2D) to add to game
        """
        self.table.add_ball(ball)

    def place_ball(self, ball):
        """ Place ball in game
        :ball: ball(Ball2D) to add to game
        """
        self.table.place_ball(ball)
        
    def display(self):
        """ Display current game
        """
        self.table.display()
        
    def start(self):
        """ Start game play
        """
        tu.ontimer(self.update)
        
    def update(self):
        """ Update game and display
        """
        self.table.update()
        self.display()
        tu.ontimer(self.update,
                   int(1000*self.update_time))
        
if __name__ == "__main__":
    from random import randint
    colors = ["red", "orange", "yellow",
              "green", "blue", "indigo",
              "violet"]
    x = 350
    top = x
    bottom = -x
    left = -x
    right = x
    balls = []      # balls
    nballs = 10
    tlen = top-bottom
    twid = tlen/2
    tleft = -twid/2
    tright = twid/2
    r = tlen/(9*12/(2.25/2))    # Scall to 9ft table,2.25" ball
    r *= 4          # Expand for viewing
    margin = 0      # margin
    game = BallTableGame2D(h=tlen, w=twid)
    
    for i in range(nballs):
        min_ball_y = int(bottom+r+margin)
        max_ball_y = int(top-r-margin)
        min_ball_x = int(tleft+r+margin)
        max_ball_x = int(tright-r-margin)
        
        bx = randint(min_ball_x,max_ball_x)
        by = randint(min_ball_y,max_ball_y)
        vx = uniform(game.table.v_min, game.table.v_max)
        vy = uniform(game.table.v_min, game.table.v_max)
        ball = Ball2D(x=bx, y=by, vx=vx, vy=vy,r=r,
                      color=colors[i%len(colors)])
        game.place_ball(ball)

    game.start()    




