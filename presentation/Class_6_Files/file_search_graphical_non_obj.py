#file_search_graphical_non_obj.py 28Feb2022  crs
# Simple search
# providing graphical output
import os
import turtle as tu

file_prev = __file__
pattern_prev = "text"
disp_boarder = 50
disp_left = -400
disp_top = 400
disp_bottom = -400+disp_boarder
text_left = disp_left
text_top = disp_top

x = disp_left
y = disp_top
font_size_to_ch = 2   # font size to ch height
dt_size_prev = 14
dt_colr_prev = "black"
dt_x = x
dt_y = y

def clear_text():
    """ Clear text screen and reset
    """
    global dt_x, dt_y, dt_size_prev, dt_colr_prev
    
    tu.reset()
    dt_x = x = disp_left
    dt_y = y = disp_top
    tu.penup()
    tu.goto(x,y)
    tu.pendown()
    
def display_text(text, size=None, colr=None,
                 x = None, y = None,
                 new_line = None):
    """ Display text on screen
    :text: text to display
    :size: font size default: previous, 14
    :colr: text color, default: previous, "black"
    :x: starting x default: previous x end
    :y: starting y default: previous y end
    :new_line: first update x,y to new line
                only new_line OR x,y allowed
    """
    global dt_x, dt_y, dt_size_prev, dt_colr_prev

    if tu.ycor() < disp_bottom + disp_boarder:
        continue_msg = "Press ENTER to continue"
        inp = input(continue_msg)
        clear_text()    # Only option            
    
    if size is None:
        size = dt_size_prev
    dt_size_prev = size
    if colr is None:
        colr = dt_colr_prev
    dt_colr_prev = colr
    if new_line is not None:
         if x is not None or y is not None:
            raise Exeception("Must not have new_line and x,y")
    else:
        new_line = True
    if new_line:
        x = dt_x = disp_left
        dt_y -= size*font_size_to_ch
        y = dt_y
    else:
        if x is None:
            x = dt_x
        dt_x = x
        if y is None:
            y = dt_y
        dt_y = y
    #print(f"display_text: text:{text} x:{x}, y:{y}")
    tu.penup()
    tu.goto(x,y)
    tu.pendown()
    tu.color(colr)
    font = ("Arial", size, "normal")
    #print(f"colr:{colr} text:{text} font:{font}")
    #print(f"xcor():{tu.xcor()} ycor():{tu.ycor()}")
    tu.write(text, align="left", font=font)
    
while True:
    fpn = os.path.basename(file_prev)
    inp = input(f"Enter File Name[{fpn}]:")
    if inp == "":
        inp = file_prev
    file_name = inp
    display_text(f"File: {file_name}", colr="black")
    try:
        with open(file_name) as finp:
            file_prev = file_name   # Remember if opened
            inp = input(f"Search For[{pattern_prev}]:")
            if inp == "":
                inp = pattern_prev
            pattern = inp
            pattern_prev = pattern            
            display_text(f"pattern: {pattern}", colr="green")
            line_no = 0         # Keep track of line
            is_first = True
            for line in finp:
                line_no += 1    # Bump each line
                if pattern in line:
                    #print(f"{line_no:4}: {line}")
                    if is_first:
                        display_text("")
                        is_first = False
                    display_text(f"{line_no:4}: {line}",
                                 colr="blue")
    except OSError:
        err_msg = f"Can't open File:{file_name}"
        print(err_msg)
        display_text(err_msg, colr="red")
        continue
    
