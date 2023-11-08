# turtle_square_fill.py    26Oct2020 from
#  https://www.youtube.com/watch?v=pxKu2pQ7ILo
# Make a square
# + fill the square
import turtle

ray = turtle.Turtle()
ray.color("blue", "pink")
ray.begin_fill()
ray.forward(100)
ray.left(90)
ray.forward(100)
ray.left(90)
ray.forward(100)
ray.left(90)
ray.forward(100)
ray.end_fill()

