# turtle_1.py    26Oct2020 from
#  https://www.youtube.com/watch?v=pxKu2pQ7ILo
import turtle

keith = turtle.Turtle()

keith.color("red", "cyan")
leng = 100
keith.begin_fill()
for i in range(3):
    keith.forward(leng)
    keith.left(90)
keith.forward(leng)
keith.end_fill()






turtle.done()
