#onkey_4_dir.py   12Dec2020  crs
"""
Simple turtle onkey example
+ Up,Down, Left, Right arrows
"""
side = 100
from turtle import *
def move(heading, dist):
    """ Move in heading direction
    :heading: heading in degrees
    :dist: distance to move
    """
    setheading(heading)
    forward(dist)
    
def up_key_pressed():
    print("up key pressed")
    move(90,side)
    
def down_key_pressed():
    print("down_key_pressed")
    move(270,side)
    
def left_key_pressed():
    print("left key pressed")
    move(180,side)
    
def right_key_pressed():
    print("right_key_pressed")
    move(0,side)


onkey(up_key_pressed, 'Up')
onkey(down_key_pressed, 'Down')
onkey(left_key_pressed, 'Left')
onkey(right_key_pressed, 'Right')

listen()

