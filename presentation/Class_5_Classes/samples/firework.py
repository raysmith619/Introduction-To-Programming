# firework.py  04Mar2022  crs, from fireworks.py
"""
Firework class - individual firework
"""
from random import randint
import turtle as tu

class Firework:
    """ Individual firework function
    """
    def __init__(self, fireworks, x, y,
                 size=100, color="blue"):
        """ Setup firework
        :fireworks: group control 
        :x: x coordinate of center
        :y: y coordinate of center
        :size: size (diameter) default: 100
        """
        self.fireworks = fireworks
        self.x = x    # initial location
        self.y = y
        self.size = size
        self.size_inc = size*.01
        self.color = color
        self.count = 0      # count of calls
        
    def display(self):
        """ Display firework
        :fw: firework object
        """
        self.star_burst()
        return
    
        tu.penup()
        tu.goto(self.x,self.y)
        tu.pendown()
        tu.dot(self.size, self.color)

    def star_burst(self):
        """ Starburst display a current x, y
        """
        npt = 20
        radius = self.size/2
        radius_min = int(radius*.5)
        radius_max = int(radius)
        angle = 360/npt
        width = 4
        width_min = int(width*.5)
        width_max = int(width*2)
        tu.penup()
        tu.goto(self.x,self.y)
        tu.pendown()
        tu.color(self.color)
        if self.count%10000 == 0:
            width = randint(width_min, width_max)
            radius = randint(radius_min,radius_max)
        self.count += 1
        for i in range(npt):
            tu.width(width)
            tu.forward(radius)
            tu.backward(radius)
            tu.right(angle)
        
    def update(self):
        """ Update this firework
        :fw: firework object (updated in place)
        """
        size = self.size
        radius = self.size/2
        x = self.x
        y = self.y
        x_min = self.fireworks.x_min
        x_max = self.fireworks.x_max
        y_min = self.fireworks.y_min
        y_max = self.fireworks.y_max
        # Grow firework until it hits a display edge
        if (x-radius <= x_min or x+radius >= x_max
            or y-radius <= y_min or y+radius >= y_max):
            # Then create in-place replacement firework
            fw_new = self.fireworks.new_firework()
            for k, v in fw_new.__dict__.items():
                setattr(self, k, v)
            size = self.size
            size_inc = self.size_inc

        size += self.size_inc
        self.size = size

    
    
