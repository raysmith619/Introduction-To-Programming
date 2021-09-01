#shortest_demo2.py
#From turtle module documentation
import random
from turtle import *
colors = ['red', 'orange',
          ###'yellow',
          'green', 'blue', 'indigo',
          'violet']
star_xchg = star_ychg = 200
for j in range(10):
    color(colors[j%len(colors)])
    penup()
    setpos(random.randint(0,star_xchg*j),
           random.randint(0,star_ychg*j))
    pendown()
    for i in range(10):
        forward(200)
        left(170)
