# This program animates the turtle to walk across the screen.
import turtle
window = turtle.Screen()
window.setup(320,320)   # Set Window size.
window.tracer(0)        # Turn-off animation.

TTL = turtle.Turtle()
TTL.speed(0)
TTL.shape("turtle")     # Select turtle's shape.
TTL.penup()
TTL.goto(-300, 0)       # Set turtle's starting position.

while True:
    window.update()     # In each while loop, refresh the window with the new drawing.
    TTL.forward(0.01)
window.exitonclick()
