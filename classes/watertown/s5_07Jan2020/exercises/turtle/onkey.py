#onkey.py   12Dec2020  crs
"""
Simple turtle onkey example
"""
from turtle import *
def up_key_pressed():
    print("up key pressed")

def down_key_pressed():
    print("down_key_pressed")


onkey(up_key_pressed, 'Up')
onkey(down_key_pressed, 'Down')

listen()

