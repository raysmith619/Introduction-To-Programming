#color_list.py
"""
Set of colors
"""
from turtle import *

cm = colormode()
side = 600
nstep = 6
xstep = side/(nstep*nstep*nstep)
speed("fastest")
penup()
goto(-side, side)
pensize(xstep)
tracer(0)       # Speedup  by putting off drawing
                # until the call to update
for ri in range(nstep):
    rc = ri/nstep*cm
    for gi in range(nstep):
        gc = gi/nstep*cm
        for bi in range(nstep):
            bc = bi/nstep*cm
            color((rc,gc,bc))
            setheading(0)
            forward(xstep)
            setheading(270)
            pendown()
            forward(side)
            penup()
            backward(side)
            print(f"rgb:{rc:.3} {gc:.3} {bc:.3}")
