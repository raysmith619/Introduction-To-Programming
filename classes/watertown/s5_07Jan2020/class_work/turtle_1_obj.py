#turtle_1_obj.py 17Nov2020 crs
"""
Turtle object oriented
"""

import turtle

rainbow = ["red", "orange", "yellow", "green", "blue",
           "indigo", "violet"]
def rt_corn(bot, col, angle, side):
    bot.color(col)
    bot.right(angle)
    bot.forward(side)
    
bots = []
for i in range(50):
    bots.append(turtle.Turtle())

for j in range(len(bots)):
    bot = bots[j]
    bot.forward(j*20)
    for i in range(len(rainbow)):
        col = rainbow[i]
        rt_corn(bot, col, 90*i*1.3, side=30*i)
