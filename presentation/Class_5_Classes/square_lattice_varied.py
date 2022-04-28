# square_lattice_varied.py  21Feb2022  crs, Author
""" Exercise SquareLattice
"""
from random import randint, uniform
import turtle as tu

from square_lattice import SquareLattice, LSquare

nfig_min = 5
nfig_max = 100
nfig_count = 0
nfig_mult = 5    # change count 
sq_size_min = 5
sq_size_max = 200
update_loop_time = 1
colors = ["red", "orange", "yellow",
      "green", "blue", "indigo", "violet",
      "gray", "black", "pink"]

turtle = tu.Turtle()
screen = tu.Screen()

def do_lattice():
    """ Update display
    nfig changes each time but sq_size
    repeats for nfig_mult times
    """
    global nfig_count, sq_size
    
    nfig = randint(nfig_min, nfig_max)
    if nfig_count % nfig_mult == 0:
        sq_size = uniform(sq_size_min, sq_size_max)
    nfig_count += 1
    lt = SquareLattice(turtle=turtle, screen=screen,
                       sq_size=sq_size)
    nsquare = lt.nsquare
    for i in range(nfig):
        ix = randint(0,nsquare)
        iy = randint(0,nsquare)
        colr = colors[randint(0,len(colors)-1)]
        sq = LSquare(lt, ix=ix, iy=iy, color=colr)
        lt.add_square(sq)
    print(f"nfig:{nfig} sq_size:{sq_size:3.4}")
    lt.display()

def display_update():
    """ Update display and set recall to continue
    """
    do_lattice()
    screen.ontimer(display_update, int(update_loop_time*1000))

display_update()    # Start display loop

screen.mainloop()
