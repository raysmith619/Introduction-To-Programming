#rectangle.py   09Apr2022  crs, simple object
"""
Simple visual example of objects
Uses turtle for visual appeal
"""
import turtle as tu

class Rectangle:
    """ Defaults, updated with latest values
    """
    x = 0
    y = 0
    width = 100
    height = 200
    edge = 3
    color = "blue"
    fill = False
    displayed = True
    
    def __init__(self, x=None, y=None,
                 width=None, height=None,
                 edge=None, color=None,
                 fill=None,
                 displayed=None):
        """ Create rectangle
            Using previous values as defaults
            Units in pixels
        :width: width default: previous [100]
        :height: height default: previous [200]
        :edge: surrounding edge default: previous [3]
        :color: color default: previous ["blue"]
        :fill: fill with color default: previous [False]
                False - only edge is colored
        :displayed: display now default: previous
        """
        if x is None:
            x = Rectangle.x
        self.x = x
        Rectangle.x = x
        
        if y is None:
            y = Rectangle.y
        self.y = y
        Rectangle.y = y
        
        if width is None:
            width = Rectangle.width
        self.width = width
        Rectangle.width = width
        
        if height is None:
            height = Rectangle.height
        self.edge = edge
        Rectangle.height = height
        
        if edge is None:
            edge = Rectangle.edge
        self.edge = edge
        Rectangle.edge = edge
        
        if color is None:
            color = Rectangle.color
        self.color = color
        Rectangle.color = color
        
        if fill is None:
            fill = Rectangle.fill
        self.fill = fill
        Rectangle.fill = fill
        
        if displayed is None:
            displayed = Rectangle.displayed
        self.displayed = displayed
        Rectangle.displayed = displayed

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
