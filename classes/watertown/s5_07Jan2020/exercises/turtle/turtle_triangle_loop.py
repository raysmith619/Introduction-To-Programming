# turtle_triangle_loop.py    26Oct2020 from
#  https://www.youtube.com/watch?v=pxKu2pQ7ILo
# Make a triangle
# Use loop to generalize

import turtle

ray = turtle.Turtle()
ray.color("blue", "red")
ray.begin_fill()
side = 200       # Length of side
angle = 120      # 180 - 120 = 60
for i in range(3):
    ray.forward(side)
    ray.left(angle)
ray.end_fill()

