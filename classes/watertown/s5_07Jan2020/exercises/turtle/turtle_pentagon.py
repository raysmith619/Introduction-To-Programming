# turtle_pentagon.py    26Oct2020 from
#  https://www.youtube.com/watch?v=pxKu2pQ7ILo
# Make a pentagon

import turtle

ray = turtle.Turtle()
ray.color("green", "red")
ray.begin_fill()
side = 200          # Length of side
nside = 5           # Number of sides

                    # Arithmetic to figure inside
                    # angle given number of sides
ntriangle = nside-2 # Divide up polygon into triangles
total_inside_angle = ntriangle*180  # Each triangle has 180
inside_angle = total_inside_angle/nside # Spread angle
outside_angle = 180 - inside_angle
angle = outside_angle   # We turn by the outside angle
for i in range(nside):
    ray.forward(side)
    ray.left(angle)
ray.end_fill()

