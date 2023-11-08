#turtle_draw_1.py    26Nov2020  crs
from turtle import *

    
def mydrag(x,y):
    ondrag(None)        # Disable to avoid possible event
    goto(x,y)
    ondrag(mydrag)

ondrag(mydrag)
done()                  # Necessary for events
