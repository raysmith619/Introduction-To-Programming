# obj_multiple_2.py    03Oct2021  crs, example
# Several turtles
import turtle

ts = []     # List of Turtle objects
colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]
nt = len(colors)
print("Build a list of turtle objects")
for i in range(nt):
    ts.append(turtle.Turtle())
    
print("Cycling through objects")
for i in range(nt):
    t = ts[i]
    t.color(colors[i])
    t.right(i*30)
    t.forward(i*25+50)

print("Adding a bit to each object")
width = 5
angle = 45
linlen = 200
for t in ts:
    t.width(width)
    t.right(angle)
    t.forward(linlen)

print("Adding a bit to each object")
width = 8
angle = 60
for t in ts:
    t.width(8)
    t.right(angle)
    t.forward(linlen)

