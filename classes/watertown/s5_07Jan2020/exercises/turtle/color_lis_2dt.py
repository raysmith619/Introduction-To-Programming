#color_list_2d.py
"""
Set of colors
"""
from turtle import *

cm = colormode()
side = 400
nstep = 25
xstep = side/nstep
speed("fastest")
penup()
goto(-side, side)
cur_pos = position()
tracer(0)       # Speedup  by putting off drawing
                # until the call to update
pensize(xstep)
for ri in range(nstep):
    penup()
    setpos(cur_pos[0]+xstep, cur_pos[1])
    cur_pos = pos()
    rc = ri/nstep*cm
    setheading(270)
    pendown()
    for gi in range(nstep):
        gc = gi/nstep*cm
        for bi in range(nstep):
            bc = bi/nstep*cm
            color((rc,gc,bc))
            forward(xstep/nstep)
            #print(f"rgb:{rc:.3} {gc:.3} {bc:.3}")
    
