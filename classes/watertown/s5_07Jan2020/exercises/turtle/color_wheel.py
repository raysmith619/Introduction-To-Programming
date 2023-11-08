#color_wheel.py 15Dec2020  crs  From stackOverflow

import turtle

colors = ['#880000','#884400','#888800','#008800',
          '#008888','#000088','#440088','#880088']

def draw_color_wheel(colors, radius, center=(0, 0)):
    slice_angle = 360 / len(colors)
    heading, position = 90, (center[0] + radius, center[1])
    for color in colors:
        turtle.color(color, color)
        turtle.penup()
        turtle.goto(position)
        turtle.setheading(heading)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius, extent=slice_angle)
        heading, position = turtle.heading(), turtle.position()
        turtle.penup()
        turtle.goto(center)
        turtle.end_fill()

draw_color_wheel(colors, 150, center=(25, 50))
turtle.hideturtle()
print('done - press any key to exit')
turtle.onkeypress(exit)
turtle.listen()
turtle.done()
