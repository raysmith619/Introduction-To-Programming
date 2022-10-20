# square_lattice.py  20Feb2022  crs, Author
import turtle as tu
from random import randint
import time
import copy

class LSquare:
    """ One element (square) in a SquareLattice
    """
    def __init__(self, lattice,
                 ix, iy, on=True, color=None,
                 verbose=False):

        """ Setup a lattice square
        :lattice: the lattice of which we are apart
        :screen: turtle screen default: create instance
        :ix: - x square offset  (zero based from left side)
        :iy: - y square offset (zero based from bottom)
        :on: State True if on, else False default: on
            Usually list only contains on elements but
            during pattern processing the list may
            contain off (on==False) values
            default: True (ON)

        :color: - color of square default: lattice.color
        :verbose: True - print values default: False
        """
        self.lattice = lattice
        self.ix = ix
        self.iy = iy
        self.on = on
        self.color = color
        if verbose is None:
            verbose = lattice.verbose
        self.verbose = verbose

    def display(self):
        """ Display lattice square
        """
        ix = self.ix
        iy = self.iy
        on = self.on
        lt = self.lattice       # Shorten access
        nsq_x = lt.nsquare
        nsq_y = lt.nsquare
        sq_size = lt.sq_size
        sq_edge = lt.sq_edge
        x_edge_min = lt.x_edge_min
        y_edge_min = lt.y_edge_min
        if not on:
            return      # Not on

        if ix > nsq_x or ix < 0:
            return      # out of bounds

        if iy > nsq_y or iy < 0:
            return      # out of bounds

        colr = self.color
        if colr is None:
            colr = lt.color
        tu = lt.turtle
        tu.color(colr)
        x = x_edge_min+sq_edge+ix*(sq_size+sq_edge)
        y = y_edge_min+sq_edge+iy*(sq_size+sq_edge)
        if self.verbose:
            print(f"ix:{ix} x:{x} iy:{iy} y:{y}")
        tu.penup()
        tu.goto(x,y)
        tu.pendown()
        tu.begin_fill()
        tu.goto(x+sq_size, y)
        tu.goto(x+sq_size, y+sq_size)
        tu.goto(x, y+sq_size)
        tu.goto(x, y)
        tu.end_fill()
        tu.penup()

        
class SquareLattice:
    """
    Latice of squares which can be used as a basis
    of graphic designs
    """
    def __init__(self, turtle=None, screen=None,
                window_width=800,
                window_height=None,
                nsquare=None, sq_size=None,
                sq_edge=1,
                color="black",
                verbose=False,
                ):
        """ Setup latice
        Sizes are in pixels
        :turtle: turtle instance default: create
        :screen: turtle screen instance default: create
        :window_width: window width default:800
        :window_height: window height default: window_width
        :nsquare: number of squares wide
                    default: window_width/sq_size else 100
        :sq_size: latuce square size
                default: window_width/nsquare
        :sq_edge: space between squares default: 1
        """
        if turtle is None:
            turtle = tu.Turtle()
        self.turtle = turtle
        if screen is None:
            screen = tu.Screen()
        self.screen = screen
        turtle.speed("fastest")        # 0 - fastest drawing - no delay
        turtle.hideturtle()
        self.window_width = window_width
        if window_height is None:
            window_height = window_width
        self.window_width = window_width
        self.window_size = min(window_width, window_height)
        self.x_edge_min = -window_width/2
        self.x_edge_max = window_width/2
        self.y_edge_min = -window_height/2
        self.y_edge_max = window_height/2
        if nsquare is not None and sq_size is not None:
            raise Exception("Can't specify both"
                            f"nsquare ({nsquare}"
                            f" and sq_size ({sq_size})")
        if nsquare is None:
            if sq_size is None:
                nsquare = 100
            else:
                nsquare = int(window_width/sq_size)
        if sq_size is None:
            sq_size = window_width/nsquare
        self.nsquare = nsquare
        self.sq_size = sq_size
        self.color = color
        self.sq_edge = sq_edge
        self.verbose = verbose
        if verbose:
            print(f"window_width:{window_width} window_height:{window_height}")
            print(f"x_edge_min:{self.x_edge_min}"
                  f" y_edge_min:{self.y_edge_min}")
            print(f"y_edge_max:{self.y_edge_max}"
                  f" y_edge_max:{self.y_edge_max}")
            print(f"nsquare:{nsquare} sq_size:{sq_size}")
        screen.setup(window_width, window_height)   # Window size.
        screen.tracer(0)                    # Turn-off animation.
        update_loop_time = .01              # Our update loop time
        self.display_list = {}

    def mainloop(self):
        """ Local pointer to turtle.mainloop
        """
        self.screen.mainloop()

    def display(self):
        """ Display lattice
        """
        self.turtle.clear()
        for ixy in self.display_list:
            sq = self.display_list[ixy]
            sq.display()
            
        
    def add_square(self,sq):
        """ Add square to lattice
        :sq: square to be added
        """
        ix = sq.ix
        iy = sq.iy
        self.display_list[(ix,iy)] = copy.copy(sq)

"""
Selftest for SquareLattice
"""
if __name__ == "__main__":
    nfig = 200
    colors = ["red", "orange", "yellow",
          "green", "blue", "indigo", "violet",
          "gray", "black", "pink"]

    lt = SquareLattice()
    nsquare = lt.nsquare
    for i in range(nfig):
        ix = randint(0,nsquare)
        iy = randint(0,nsquare)
        colr = colors[randint(0,len(colors)-1)]
        
        sq = LSquare(lt, ix=ix, iy=iy, color=colr)
        lt.add_square(sq)
    lt.display()

    lt.mainloop()      # Do event processing

    
    
