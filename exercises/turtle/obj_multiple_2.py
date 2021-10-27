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
    t.color(colors[i%nt])
    t.right(i*30)
    t.forward(i*25+50)
    ts.append(t)

print("Cycling through objects")
angle = 45
length = i*25
for t in ts:
    t.width(5)
    t.right(angle)
    t.forward(i*25+50)

for t in ts:
    t.width(8)
    t.right(angle)
    t.forward(i*25+50)

