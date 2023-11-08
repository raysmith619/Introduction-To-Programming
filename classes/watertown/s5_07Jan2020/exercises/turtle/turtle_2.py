# turtle_2.py    26Oct2020 from
#  https://www.youtube.com/watch?v=pxKu2pQ7ILo
import turtle

t = turtle.Turtle()
t.color("red", "yellow")
t.speed(10)
ang = 170
t.begin_fill()
l = 200
for i in range(50):
    t.forward(l)
    t.left(ang)
t.end_fill()

turtle.done()
