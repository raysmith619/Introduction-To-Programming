# obj_multiple_2.py    03Oct2021  crs, example
# Several turtles
import turtle

ts = []
colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]
nt = len(colors)
for i in range(nt):
    t = turtle.Turtle()
    t.color(colors[i])
    t.right(i*30)
    t.forward(i*25+50)
    ts.append(t)

print("Cycling through objects")
width = 5
angle = 45
linlen = 200
for t in ts:
    t.width(width)
    t.right(angle)
    t.forward(linlen)

width = 8
angle = 60
for t in ts:
    t.width(8)
    t.right(angle)
    t.forward(linlen)

