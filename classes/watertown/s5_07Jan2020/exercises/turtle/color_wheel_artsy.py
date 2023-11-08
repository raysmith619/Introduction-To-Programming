#color_wheel_artsy.py   15Dec2020  crs from github
#https://python-with-science.readthedocs.io/en/latest/colour_wheel/colour_wheel.html
# Explore HSL colour
from turtle import *
import colorsys

def sector(r, angle, c):
    "Sector filled with colour c"
    fillcolor(c)
    begin_fill()
    forward(r)
    left(90)
    circle(r, angle)
    right(90)
    backward(r)
    end_fill()

def wheel(r, sat=1.0, light=0.5, N=24):
    "A colour wheel of radius r with N sectors"
    for i in range(N):
        c = colorsys.hls_to_rgb(i/N, light, sat)
        sector(r, 360/N, c)

# Program
hideturtle()
penup()
tracer(0)

K = 50
for k in range(K):
    r = 300*(1-k/K)
    wheel(r, light=(K-k-1)/K, sat=1.0, N=120)
    update()
