#rectangle_simp.py   09Apr2022  crs, from rectangle.py
"""
Simple visual example of objects shortened for demonstration
Uses turtle for visual appeal
"""
import turtle as tu

class Rectangle:
    def __init__(self, x=0, y=0,
                 width=100, height=200,
                 edge=3, color="blue",
                 fill=False,
                 displayed=True):
        """ Create rectangle
            Units in pixels
        :width: width default: 100
        :height: height default: 200
        :edge: surrounding edge default: 3
        :color: color default: "blue"
        :fill: fill with color default: False
                False - only edge is colored
        :displayed: display now default: True
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.edge = edge
        self.color = color
        self.fill = fill
        self.displayed = displayed
        if self.display:
            self.display()

    def display(self):
        """ Display rectangle """
        tu.penup()
        tu.goto(x=self.x, y=self.y)
        tu.pendown()
        tu.pensize(self.edge)
        if self.fill:
            tu.color(self.color,self.color)
        else:
            tu.color(self.color)
        if self.fill:
            tu.begin_fill()
        tu.forward(self.width)
        tu.left(90)
        tu.forward(self.height)
        tu.left(90)
        tu.forward(self.width)
        tu.left(90)
        tu.forward(self.height)
        tu.left(90)     # Leave in original direction
        if self.fill:
            tu.end_fill()

if __name__ == '__main__':
    from random import randint
    
    tu.speed('fastest')     # speedup
    colors = ["red", "orange", "yellow",
              "green", "blue", "indigo",
              "violet"]
    nrec = 15
    size = 800
    x_beg = y_beg = -size/2
    x_end = y_end = size/2
    inc = int(size/nrec)
    x = x_beg
    y = y_beg
    for i in range(nrec):
        width = randint(inc,x_end-x)
        height = randint(inc,y_end-y)
        edge = i+1
        color = colors[i%len(colors)]
        fill = i % 2
        rec = Rectangle(x=x, y=y, width=width, height=height,
                        color=color,fill=fill)
        x += inc
        y += inc
