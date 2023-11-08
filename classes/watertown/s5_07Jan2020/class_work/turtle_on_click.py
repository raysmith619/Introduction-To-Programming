#turtle_on_click.py 19Nov2020 crs
from turtle import *

class MyTurtle(Turtle):
    def glow(self,x,y):
        self.fillcolor("red")
    def unglow(self,x,y):
        self.fillcolor("orange")
    def mv(self, x, y):
        #self.penup()
        print(f"mv({x},{y})")
        self.goto(x,y)
        #self.pendown()
        
t = MyTurtle()
t.color("blue")
#t.shape("circle")
#t.shapesize(10,15, 20)
#t.onclick(t.glow)     # clicking on turtle turns fillcolor red,
#t.onrelease(t.unglow) # releasing turns it to transparent.
t.ondrag(t.mv)
t.forward(30)
t.left(90)
t.forward(30)
done()
