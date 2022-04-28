# Turtle Animation using Screen Events - Arrow Keys.
# From: https://softwareprogramming4kids.com/turtle-animation/
import turtle
screen = turtle.Screen()
screen.setup(320,320)   # Set screen size.
screen.tracer(0) # Stop animation until frame is completed.
screen.title('TURTLE ANIMATION USING ARROW KEYS')
trtl = turtle.Turtle()
trtl.hideturtle() # We do not want to see the turtle image on the screen.
trtl.color("blue")

# Initialize variables.
x, y, x_step, y_step = 0, 0, 10, 10  # Initialize global variables.

def next_frame():
    trtl.clear()   # Clear the screen before each next frame.
    # x-step and y_step are the pexels the image moves at each key press.
    trtl.penup()
    trtl.goto(x, y)
    trtl.pendown()
    trtl.dot(100)  # Draw a black dot of radius = 20
    screen.ontimer(next_frame, 10) # Call next_frame 10 msec later
    screen.update()

###### DEFINE KEY PRESS EVENT HANDLER FUNCTIONS ######
def move_left():
    global x
    print('left arrow key pressed')
    x = x - x_step

def move_right():
    global x
    print('right arrow key pressed')
    x = x + x_step

def move_down():
    global  y
    print('down arrow key pressed')
    y = y - y_step

def move_up():
    global y
    print('up arrow key pressed')
    y = y + y_step

###### BIND EVENTS TO THE FOUR ARROW KEYS  ######
screen.onkey(move_left, 'Left')  # Left arrow key bind to handler 'move_left'.
screen.onkey(move_right, 'Right')
screen.onkey(move_down, 'Down')
screen.onkey(move_up, 'Up')

######  CALL next-frame() FUNCTION ######
next_frame()
screen.listen()  # Check if key is pressed
screen.mainloop()
