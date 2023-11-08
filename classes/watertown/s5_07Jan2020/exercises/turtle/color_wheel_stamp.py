#color_wheel_stamp.py 15Dec2020  crs  From stackOverflow
"""
Color Wheel, using stamp
"""
from turtle import Turtle, Screen

colors = ['#880000', '#884400', '#888800', '#008800',
          '#008888', '#000088', '#440088', '#880088']

def draw_color_wheel(colors, radius, center=(0, 0)):
    slice_angle = 360 / len(colors)

    yertle = Turtle(visible=False)
    yertle.penup()

    yertle.begin_poly()
    yertle.sety(radius)
    yertle.circle(-radius, extent=slice_angle)
    yertle.home()
    yertle.end_poly()

    screen.register_shape('slice', yertle.get_poly())
    yertle.shape('slice')
    yertle.setposition(center)

    for color in colors:
        yertle.color(color)
        yertle.stamp()
        yertle.left(slice_angle)

screen = Screen()

draw_color_wheel(colors, 250, center=(25, 50))

screen.exitonclick()
