#canvas_lines.py    23Oct2022  crs, From resource_lib_proj/
import tkinter as tk
from random import uniform

mw = tk.Tk()

# Establish sizes
cv_width = 300          # canvas size
cv_height = cv_width*2

# Coordinates within drawing area
x_min = cv_width*.1
x_max = cv_width*.9
x_range = (x_max-x_min)
x_mid = (x_min+x_max)/2
y_min = cv_height*.1
y_max = cv_height*.9
y_mid = (y_min+y_max)/2
y_range = abs(y_max-y_min)

# Add drawing area
canvas = tk.Canvas(mw, width=cv_width, height=cv_height)
canvas.pack()

# parabola: f(x) = x**2
# Scale to fit (x,y: min to max)
# x increases to right
# y increases down
npts = 100
xys = []    # List of x,y coords
fn_x_max = npts-1
fn_y_max = fn_x_max**2
for i in range(npts):
    fn_x = i
    fn_y = fn_x**2
    x = x_min + x_range*fn_x/fn_x_max
    y = y_min + y_range*fn_y/fn_y_max
    xys.extend([x,y])
    
# line sequence    
line = canvas.create_line(*xys, fill="red",
                          width=5)
# Add Title Text    
canvas.create_text(x_mid, y_min/2, text="Parabola",
                font=20, fill="blue")


tk.mainloop()
