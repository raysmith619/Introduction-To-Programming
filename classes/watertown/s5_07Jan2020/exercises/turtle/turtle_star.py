# turtle_star.py    26Oct2020 from
#  https://www.youtube.com/watch?v=pxKu2pQ7ILo
# Complete Python Turtle Graphics Overview!
#  (From Beginner to Advanced)
import turtle
import math
import random

def star(tg, size):
    if size <= 10:
        return
    tg.begin_fill() 
    for i in range(5):
       tg.forward(size)
       star(tg, size/3)
       tg.left(216)
    tg.end_fill()


leng = 360
t = turtle.Turtle()
t.getscreen().bgcolor("light blue")
t.speed(100)
t.penup()
t.goto((-200, 100))
t.pendown()
star(t, leng)
turtle.done()
