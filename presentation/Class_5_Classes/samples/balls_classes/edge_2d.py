#edge2d.py  30Jul2022  crs, Author
"""
Two dimentional edge, using turtle
"""
import turtle as tu

class Edge2D:
    """ Two edge ball
    """
    tu.tracer(0)
    tu.hideturtle()
    width_prev = 1
    color_prev = "blue"
    def __init__(self, x1=0,y1=0, x2=0, y2=0,
                 width = None,
                 color=None):
        """ Initialize ball
        :x1: position begin x default: 0
        :y1: position begin y default: 0
        :x2: position end x default: 0
        :y2: position end y default: 0
        :width: edge line width default: previous_width [1]
        :color: color default: previous color ["blue"]
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width
        if width is None:
            width = Edge2D.width_prev  # Use previous
        self.width = width
        Edge2D.width_prev = width  # Remember as previous
        
        if color is None:
            color = Edge2D.color_prev
        self.color = color
        Edge2D.color_prev = color  # Remember as previous
        
    def __str__(self):
        """ String representation, mostly for
            debugging / diagnostic use
        """
        st = f"Edge2D: x1:{self.x1} y1:{self.y1}"
        st += f" x2:{self.x2} y2:{self.y2}"
        st += f" w:{self.width}"
        st += f" {self.color}"
        return st

    def display(self):
        """Display edge
        """
        tu.penup()
        tu.goto(x=self.x1, y=self.y1)
        tu.pendown()
        tu.color(self.color)
        tu.width(self.width)
        tu.goto(x=self.x2, y=self.y2)
        tu.update()

if __name__ == "__main__":
    x = 350
    top = x
    bottom = -x
    left = -x
    right = x
    edges = []      # Place edges in list
    etop = Edge2D(x1=left, y1=top, x2=right, y2=top,
                width=10, color="green")
    edges.append(etop)
    eright = Edge2D(x1=right, y1=top, x2=right, y2=bottom)
    edges.append(eright)
    ebottom = Edge2D(x1=right, y1=bottom, x2=left, y2=bottom)
    edges.append(ebottom)
    eleft = Edge2D(x1=left, y1=bottom, x2=left, y2=top)
    edges.append(eleft)
    for edge in edges:
        print(edge)
        edge.display()
        
    tu.done()
    


