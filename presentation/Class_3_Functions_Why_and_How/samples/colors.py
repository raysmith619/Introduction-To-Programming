#colors.py  05Mar2022  crs
""" Just some experimentation with
colors
"""
import turtle as tu
side = 600
x_beg = -side/2
y_beg = -side/2
n_wide = 10
n_high = 7
x_seg = side/n_wide
y_seg = side/n_high
width = max(x_seg, y_seg)
tu.width(width)
tu.speed("fastest")
tu.colormode(255)
while True:
    # Take pairs of red,blue,green
    for m in [(1,1,0), (0,1,1), (1,0,1)]:
        r,g,b = m
        for i in range(n_wide):
            y1 = y_beg
            for j in range(n_high):
                y1 += y_seg
                tu.penup()
                x1 = x_beg+i*x_seg
                tu.goto(x1,y1)
                tu.pendown()
                rc = bc = gc = 0
                if r:
                    rc = int(i/n_wide*255)
                if g:
                    if r:
                        gc = int(j/n_high*255)
                    else:
                        gc = int(i/n_wide*255)
                if b:
                    bc = int(j/n_high*255)
                tu.color((rc,bc,gc))    # Don't forget tupple
                x2 = x1+x_seg
                y2 = y1
                tu.goto(x2,y2)
