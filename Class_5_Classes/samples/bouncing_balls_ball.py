# pool_ball.py  17Feb2022  crs, Author
"""
Demonstration of class/object usage
in depicting pool balls on a table
PoolBall class
"""
import turtle

class PoolBall:
    number = 0    # Previous/default values
    radius = 100
    pos_x = 0
    pos_y = 0
    vel_x = 0
    vel_y = 0
    
    def __init__(self,
                 tu,
                 radius=None,
                 color=None,
                 number=None,
                 pos_x=None,
                 pos_y=None,
                 vel_x=None,
                 vel_y=None):
        """ Create ball
        :tu: turtle instance
        :radius: ball radius default: previous
        :color: ball color default: previous
        :number: ball number default: generated
        :pos_x: x position default: previous
        :pos_y: y position default: previous
        :vel_x: x velocity default: previous
        :vel_y: y velocity default: previous
        """
        self.tu = tu
        if number is None:
            PoolBall.number += 1
            number = PoolBall.number
        self.number = number
        if number > PoolBall.number:
            PoolBall.number = number
        if radius is None:
            radius = PoolBall.radius
        PoolBall.radius = radius
        self.radius = radius
        if color is None:
            color = PoolBall.color
        PoolBall.color = color
        self.color = color
        if pos_x is None:
            pos_x = PoolBall.pos_x
        self.pos_x = pos_x
        if pos_y is None:
            pos_y = PoolBall.pos_y
        self.pos_y = pos_y
        if vel_x is None:
            vel_x = PoolBall.vel_x
        self.vel_x = vel_x
        if vel_y is None:
            vel_y = PoolBall.vel_y
        self.vel_y = vel_y
