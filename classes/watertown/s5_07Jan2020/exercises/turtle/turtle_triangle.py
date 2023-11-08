# turtle_triangle.py    26Oct2020 from
#  https://www.youtube.com/watch?v=pxKu2pQ7ILo
# Make a triangle
import turtle

ray = turtle.Turtle()
ray.color("blue", "red")
ray.begin_fill()
side = 200       # Length of side
angle = 120      # 180 - 120 = 60
ray.forward(side)
ray.left(angle)
ray.forward(side)
ray.left(angle)
ray.forward(side)
ray.end_fill()

