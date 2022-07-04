#shapes.py  26Feb2022  crs
"""
Simple construction of shapes from components
"""
import turtle as tu     # shorten local name

x_prev = 0
y_prev = 0
colr_prev = "black"
wid_prev = 3
down_prev = True

def add_point(x=None, y=None,
         colr=None, wid=None, down=None):
    """ Add point
    :x: point x default: previous x
    :y: point y default: previous y
    :colr: line color default: previous color
    :wid: line width default: previous colr
    :down: pen down default: previous down
    """
    global x_prev, y_prev, colr_prev, wid_prev
    global down_prev

    if x is None:
        x = x_prev
    x_prev = x

    if y is None:
        y = y_prev
    y_prev = y

    if colr is None:
        colr = colr_prev
    colr_prev = colr

    if wid is None:
        wid = wid_prev
    wid_prev = wid

    if down is None:
        down = down_prev
    down_prev = down

    tu.width(wid)
    if down:
        tu.pendown()
    else:
        tu.penup()
        
    tu.color(colr)
    tu.goto(x,y)

"""
Do testing if running this file
"""
if __name__ == "__main__":
                        # Start text
    text_bot = -100     # lower left corner
    text_left = -350
    seg = 100  # line segment
    let_wid = 2*seg              # letter width
    let_high = 2*seg            # letter height
    space = .5*seg

    # R    
    let_bot = text_bot          # First letter
    let_left = text_left
    add_point(down=False, wid=15)
    add_point(x=let_left, y=let_bot, colr="red")
    add_point(down=True)
    add_point(       y=let_bot+let_high)    # up
    add_point(x=let_left+let_wid)           # right
    add_point(       y=let_bot+let_high/2)  # down
    add_point(x=let_left)                   # left
    add_point(x=let_left+.5*seg)            # right a bit
    add_point(x=let_left+let_wid, y=let_bot)# down to right

    # A
    let_left = let_left+let_wid+space       # next letter
                                            # same height
    add_point(down=False)
    add_point(x=let_left, colr="blue") # to next letter
    add_point(down=True)
    add_point(x=let_left+seg, y=let_bot+2*seg, down=True)
    add_point(x=let_left+2*seg, y=let_bot)
    # Get cross line
    x_cp = ((let_left+seg)+(let_left+2*seg))/2
    y_cp = (let_bot+(let_bot+let_high))/2
    add_point(x=x_cp, y=y_cp)
    x_cp = ((let_left)+(let_left+seg))/2
    add_point(x=x_cp)

    # Y
    let_left = let_left+let_wid+space
    add_point(down=False)
    add_point(x=let_left, y=let_bot+let_high,
              colr="green") # to next letter
    add_point(down=True)
    add_point(x=let_left+seg, y=let_bot+1*seg, down=True)
    add_point(x=let_left+2*seg, y=let_bot+let_high)
    add_point(x=let_left+seg, y=let_bot+1*seg, down=True)
    add_point(      y=let_bot)
    
