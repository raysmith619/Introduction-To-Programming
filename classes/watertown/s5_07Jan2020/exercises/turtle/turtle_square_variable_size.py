# turtle_square_variable_size.py    26Oct2020 from
#  https://www.youtube.com/watch?v=pxKu2pQ7ILo
# Make a square
# + fill the square
# + Make the size a variable
import turtle

ray = turtle.Turtle()
ray.color("blue", "red")
ray.begin_fill()
side = 200       # Length of square side
ray.forward(side)
ray.left(90)
ray.forward(side)
ray.left(90)
ray.forward(side)
ray.left(90)
ray.forward(side)
ray.end_fill()

