#ball_collision_2d.py  02Aug2022  crs, from ball_table_2d
"""
Collision process for 2D balls
Used by BallTable2D
"""
from math import sqrt
from itertools import combinations
import turtle as tu
from ball_2d import Ball2D

class BallCollision2D:
    """ Two dimentioal ball collision processing
    """
    track_collision = False
    
    @classmethod
    def set_track(level=True):
        """ Set tracking printing on
        """
        BallCollision2D.track_collision = level
        
    def __init__(self, balls=None):
        """ Initialize collision processing
        :balls: list of balls (Ball2D)
        """
        if balls is None:
            balls = []
        self.balls = balls

    def ball_touch(self, ball1, ball2):
        """ Test if balls are touching
        :ball1: first ball
        :ball2: second ball
        :returns: True iff balls are touching
        """
        cdistsq = ((ball2.x-ball1.x)**2 +
            (ball2.y-ball1.y)**2)
        if cdistsq < (ball1.r+ball2.r)**2:
            return True
        return False
    
    def balls_colliding(self, balls=None):
        """ Return list of colliding ball pairs
            Start simple, get smarter, if necessary
            Look at all ball pairs
            :balls: balls to check default: self.balls
            :returns: list of colliding pairs
        """
        if balls is None:
            balls = self.balls

        colliding_pairs = []
        ball_pairs = list(combinations(balls, 2))
        for ball_pair in ball_pairs:
            b1, b2 = ball_pair
            if self.ball_touch(b1,b2):
                colliding_pairs.append(ball_pair)
        return colliding_pairs

    def ball_collision_update(self):
        """ Update all colliding balls
            no display
        """
        ball_pairs = self.balls_colliding()
        for ball_pair in ball_pairs:
            b1,b2 = ball_pair
            self.ball_pair_collision_update(b1,b2)

    def ball_display(self):
        for ball in self.balls:
            ball.display()
        tu.update()
            
    def ball_update(self):
        for ball in self.balls:
            ball.update()
            
    def ball_pair_collision_update(self, b1, b2):
        """ Update pair of balls colliding with each other
        :b1: first ball
        :b2: second ball
        """
        n_vec = tu.Vec2D(b2.x-b1.x,b2.y-b1.y)
        n_vec_mag = abs(n_vec)
        if n_vec_mag == 0:
            return      # too close

        sep_dist = n_vec_mag - b1.r - b2.r
        if sep_dist < -b1.r*.001:
            if BallCollision2D.track_collision:
                print(f"\nsep_dist:{sep_dist:.3f} {sep_dist/b1.r:.3f}*r"
                      f" {b1.color}:{b2.color}")
                print(f"    n_vec:{n_vec}")
            b1_vec = tu.Vec2D(b1.x, b1.y)
            b2_vec = tu.Vec2D(b2.x, b2.y)
            un_vec = n_vec * (1 / n_vec_mag)
            if BallCollision2D.track_collision:
                print(f"    un_vec:{un_vec}")
            sep_vec = (sep_dist/2)*un_vec         # Split the diff
            if BallCollision2D.track_collision:
                print(f"    sep_vec:{sep_vec}")
            b1_backoff_vec = b1_vec + sep_vec
            b2_backoff_vec = b2_vec - sep_vec
            b1.x, b1.y = b1_backoff_vec
            b2.x, b2.y = b2_backoff_vec
            new_dist = sqrt((b2.x-b1.x)**2 + (b2.y-b1.y)**2)
            new_sep = new_dist - b1.r - b2.r
            if BallCollision2D.track_collision:
                print(f"    new_sep:{new_sep/b1.r:.3f}*r: {b1.color}:{b2.color}")

                                # Setup based on adjusted positioning
            n_vec = tu.Vec2D(b2.x - b1.x, b2.y - b1.y)
            n_vec_mag = abs(n_vec)
            if n_vec_mag == 0:
                return  # too close

        un_vec = n_vec*(1/n_vec_mag)
        ut_vec = un_vec.rotate(-90)
        v1_vec = tu.Vec2D(b1.vx, b1.vy)
        v1n = un_vec*v1_vec
        v1t = ut_vec*v1_vec
        
        v2_vec = tu.Vec2D(b2.vx, b2.vy)
        v2n = un_vec*v2_vec
        v2t = ut_vec*v2_vec

        vp1t = v1t      # No change to tangential velocity
        vp2t = v2t

                        # given m1 == m2
                        # vp1n = v2n, vp2n = v1n
                        # Exchanging normal velocities
                        # If too overlapping don't change normal vel

        if sep_dist < -(b1.r+b2.r)*.2:
            vp1n = v1n
            vp2n = v2n
        else:
            vp1n = v2n
            vp2n = v1n

        vp1n_vec = vp1n*un_vec
        vp1t_vec = vp1t*ut_vec
        
        vp2n_vec = vp2n*un_vec
        vp2t_vec = vp2t*ut_vec

        vp1_vec = vp1n_vec + vp1t_vec
        vp2_vec = vp2n_vec + vp2t_vec

                        # Update each ball's vx,vy
        b1.vx, b1.vy = vp1_vec
        b2.vx, b2.vy = vp2_vec

    def reset(self, balls=None):
        """ Reset all ball to reset
        :balls: balls in collision system
                default: self.balls
        """
        if balls is None:
            balls = self.balls
        for ball in balls:
            ball.reset()

if __name__ == "__main__":
    
    import time
    from math import sqrt
    from ball_table_2d import BallTable2D

    clear_at_end = False
    clear_at_end = True
    
    tbl = BallTable2D()
    max_r_sq = tbl.x_max**2 + tbl.y_max**2
    t_update = tbl.t_update
    #BallCollision2D.set_track()     # Setup tracking
    def collision_1():
        """ Simple collision moving at center of stationary
        :clear_at_end: True - clear balls at end
                        default False - leave display
        """
        tu.reset()
        print("collision_1")
        r = 100
        b1 = Ball2D(r=r, x=0, y=tbl.y_min, vy=tbl.v_max, color="blue")
        b2 = Ball2D(r=r, x=0, y=0, color="red")
        bc = BallCollision2D(balls=[b1,b2])
        while (b2.x**2 + b2.y**2 < max_r_sq):
            bc.ball_display()
            bc.ball_collision_update()
            time.sleep(t_update)
            bc.ball_update()
        if clear_at_end:
            bc.reset()


    def collision_2():
        """ Simple collision moving at 45 degree of stationary
        """
        tu.reset()
        print("collision_2")
        r = 100
        b1 = Ball2D(r=r, x=r, y=tbl.y_min, vy=tbl.v_max, color="blue")
        b2 = Ball2D(r=r, x=0, y=0, color="red")
        bc = BallCollision2D(balls=[b1, b2])
        while (b1.x**2 + b1.y**2 < max_r_sq
               or b2.x**2 + b2.y**2 < max_r_sq):
            bc.ball_display()
            bc.ball_collision_update()
            time.sleep(t_update)
            bc.ball_update()
        if clear_at_end:
            bc.reset()


    def collision_3():
        """ Simple collision two moving and hitting at 0 deg
        """
        tu.reset()
        print("collision_3")
        r = 100
        b1 = Ball2D(r=r, x=0, y=tbl.y_min, vy=tbl.v_max, color="blue")
        b2 = Ball2D(r=r, x=0, y=tbl.y_max, vy=-tbl.v_max, color="red")
        bc = BallCollision2D(balls=[b1, b2])
        max_r_sq = tbl.x_max**2 + tbl.y_max**2
        while (b1.x**2 + b1.y**2 < max_r_sq
               or b2.x**2 + b2.y**2 < max_r_sq):
            bc.ball_display()
            bc.ball_collision_update()
            time.sleep(t_update)
            bc.ball_update()
        if clear_at_end:
            bc.reset()


    def collision_4():
        """ Simple collision two moving and hitting at 45 deg
        """
        tu.reset()
        print("collision_4")
        r = 100
        b1 = Ball2D(r=r, x=r, y=tbl.y_min, vy=tbl.v_max, color="blue")
        b2 = Ball2D(r=r, x=0, y=tbl.y_max, vy=-tbl.v_max, color="red")
        bc = BallCollision2D(balls=[b1, b2])
        max_r_sq = tbl.x_max**2 + tbl.y_max**2
        while (b1.x**2 + b1.y**2 < max_r_sq
               or b1.x**2 + b1.y**2 < max_r_sq):
            bc.ball_display()
            bc.ball_collision_update()
            time.sleep(t_update)
            bc.ball_update()
        if clear_at_end:
            bc.reset()


    def collision_5():
        """ Multi-ball collision one moving and three in traiagular
            arrangement
        """
        tu.reset()
        print("collision_5")
        r = 100
        maxby = tbl.y_max - 3*r
        b1 = Ball2D(r=r, x=0, y=tbl.y_min, vy=tbl.v_max, color="blue")
        b2 = Ball2D(r=r, x=-r, y=maxby, vy=0, color="red")
        b3 = Ball2D(r=r, x=+r, y=maxby, vy=0, color="orange")
        b4 = Ball2D(r=r, x=0, y=maxby-r*sqrt(3), vy=0, color="green")
        bc = BallCollision2D(balls=[b1, b2, b3, b4])
        max_r_sq = tbl.x_max**2 + tbl.y_max**2
        while (b2.x**2 + b2.y**2 < max_r_sq
               or b3.x**2 + b3.y**2 < max_r_sq):
            bc.ball_display()
            bc.ball_collision_update()
            #time.sleep(int(.01))
            time.sleep(t_update)
            bc.ball_update()
        if clear_at_end:
            bc.reset()


    def collision_5a():
        """ Multi-ball collision one moving and three in traiagle
        slightly separated balls
            arrangement
        """
        tu.reset()
        print("collision_5a")
        r = 100
        sep = r*.10
        maxby = tbl.y_max - 3*r
        b1 = Ball2D(r=r, x=0, y=tbl.y_min, vy=tbl.v_max, color="blue")
        b2 = Ball2D(r=r, x=-r-sep/2, y=maxby, vy=0, color="red")
        b3 = Ball2D(r=r, x=r+sep/2, y=maxby, vy=0, color="orange")
        b4 = Ball2D(r=r, x=0, y=maxby-sqrt(3*r**2+3*r*sep+3*sep**2/4),
                             vy=0, color="green")
        bc = BallCollision2D(balls=[b1, b2, b3, b4])
        max_r_sq = tbl.x_max**2 + tbl.y_max**2
        while (b2.x**2 + b2.y**2 < max_r_sq
               or b3.x**2 + b3.y**2 < max_r_sq):
            bc.ball_display()
            bc.ball_collision_update()
            time.sleep(t_update)
            bc.ball_update()
        if clear_at_end:
            bc.reset()


    def collision_6():
        """ Multi-ball collision one moving and three in line
        slightly separated balls
            arrangement
        """
        tu.reset()
        print("collision_6")
        r = 100
        sep = r*.0
        maxby = tbl.y_min + 7*r
        b1 = Ball2D(r=r, x=0, y=tbl.y_min, vy=tbl.v_max, color="blue")
        b2 = Ball2D(r=r, x=0, y=maxby, vy=0, color="red")
        b3 = Ball2D(r=r, x=0, y=maxby-2*(r+sep), vy=0, color="orange")
        b4 = Ball2D(r=r, x=0, y=maxby-4*(r+sep), vy=0, color="green")
        bc = BallCollision2D(balls=[b1, b2, b3, b4])
        while (b1.x**2 + b1.y**2 < max_r_sq
               and b2.x**2 + b2.y**2 < max_r_sq
               and b3.x**2 + b3.y**2 < max_r_sq
               and b4.x**2 + b4.y**2 < max_r_sq):
            bc.ball_display()
            bc.ball_collision_update()
            time.sleep(t_update)
            bc.ball_update()
        if clear_at_end:
            bc.reset()

    coll_list = [collision_1, collision_2, collision_3,
                 collision_4, collision_5, collision_5a,
                 collision_6
                 ]
    #coll_list = [collision_6]   # Just do one
    while True:
        for coll in coll_list:
            coll()
    tu.done()
