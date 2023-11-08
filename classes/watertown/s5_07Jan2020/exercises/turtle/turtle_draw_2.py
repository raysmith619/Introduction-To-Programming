#turtle_draw_2.py    26Nov2020  crs
from turtle import *

""" Support positioning
"""
def myclick(x,y):
    #penup()
    onclick(None)       # Avoid events while here
    goto(x,y)
    onclick(myclick)
    #pendown()
    
def mydrag(x,y):
    ondrag(None)        # Disable to avoid possible event
    goto(x,y)
    ondrag(mydrag)

onclick(myclick)
#ondrag(mydrag)
done()                  # Necessary for events
