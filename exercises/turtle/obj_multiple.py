# obj_multiple.py    03Oct2021  crs, example
# Several turtles
import turtle

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]
nt = len(colors)          
for i in range(nt):
    t = turtle.Turtle()
    t.color(colors[i])
    t.right(i*30)
    t.forward(i*25+50)

