#onkey_up_down.py   12Dec2020  crs
"""
Simple turtle onkey example
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


onkey(up_key_pressed, 'Up')
onkey(down_key_pressed, 'Down')

listen()

