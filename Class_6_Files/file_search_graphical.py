#file_search_graphical.py 28Feb2022  crs
# Simple search
# uses graphical_text module
import os
import turtle as tu

from graphical_text import GraphicalText

file_prev = __file__
pattern_prev = "text"

grt = GraphicalText()

while True:
    fpn = os.path.basename(file_prev)
    inp = input(f"Enter File Name[{fpn}]:")
    if inp == "":
        inp = file_prev
    file_name = inp
    grt.display_text(f"File: {file_name}", colr="black")
    try:
        with open(file_name) as finp:
            file_prev = file_name   # Remember if opened
            inp = input(f"Search For[{pattern_prev}]:")
            if inp == "":
                inp = pattern_prev
            pattern = inp
            pattern_prev = pattern            
            grt.display_text(f"pattern: {pattern}", colr="green")
            line_no = 0         # Keep track of line
            is_first = True
            for line in finp:
                line_no += 1    # Bump each line
                if pattern in line:
                    #print(f"{line_no:4}: {line}")
                    if is_first:
                        grt.display_text("")
                        is_first = False
                    grt.display_text(f"{line_no:4}: {line}",
                                 colr="blue")
    except OSError:
        err_msg = f"Can't open File:{file_name}"
        print(err_msg)
        grt.display_text(err_msg, colr="red")
        continue
    
