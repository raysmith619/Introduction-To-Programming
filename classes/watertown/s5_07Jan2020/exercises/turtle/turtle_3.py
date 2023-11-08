# turtle_3.py    26Oct2020 from
#  https://www.youtube.com/watch?v=pxKu2pQ7ILo
import turtle
import math
import random

t = turtle.Turtle()
t.color("red", "yellow")
t.speed(10)
ang = 170
t.begin_fill()
l = 200
for i in range(2000):
    t.forward(l/20)
    t.left(math.sin(i/10)*25)
    t.left(l/10)
t.end_fill()

turtle.done()
