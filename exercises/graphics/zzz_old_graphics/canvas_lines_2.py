#canvas_lines_2.py    23Oct2022  crs, From resource_lib_proj/
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


# Connect random points
npts = 15
xys = []    # List of x1,y1, x2,y2, ...
for i in range(npts):
    x = uniform(x_min,x_max)
    y = uniform(y_min, y_max)
    xys.append(x)
    xys.append(y)

# *xys expands xys list to calling arguments    
line = canvas.create_line(*xys, fill="green",
                          width=2)    
# Mark points
for n in range(1,npts+1):
    i = n*2-2
    if n == 1:
        canvas.create_text(xys[i],xys[i+1],
                           text="Start",
                           font=20, fill="blue")
    elif n == npts:
        canvas.create_text(xys[i],xys[i+1],
                           text="End",
                           font=20, fill="blue")
    else:
        canvas.create_text(xys[i],xys[i+1],
                           text=n,
                           font=15, fill="blue")
# Add Title Text    
canvas.create_text(x_mid, y_min/2,
                   text="Line connecting random points"
                       "\nwhich are subsequently marked",
                font=20, fill="black")



tk.mainloop()
