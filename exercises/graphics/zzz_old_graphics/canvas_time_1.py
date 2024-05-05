#canvas_time_1.py    24Oct2022  crs
import tkinter as tk
import math
import time
import random

mw = tk.Tk()

# Establish sizes
cv_width = 300          # canvas size
cv_height = cv_width*3
        
# Coordinates within drawing area
x_min = cv_width*.05
x_max = cv_width*.95
x_range = (x_max-x_min)
x_mid = (x_min+x_max)/2
y_min = cv_height*.1
y_max = cv_height*.95
y_mid = (y_min+y_max)/2
y_range = abs(y_max-y_min)

# Add drawing area
canvas = tk.Canvas(mw, width=cv_width, height=cv_height)
canvas.pack()
             
# Add title text    
canvas.create_text(x_mid, y_min/2,
                text="Event timiing - with after()",
                font=20, fill="black")

# Lights layout
time_green = 3000         # time for green milliseconds
time_red = 2000         # time for red milliseconds
time_yellow = int(time_red/3)   # time for yellow
light_size = y_range*.33
light_spacer = light_size*.05
yt = y_min
ytb = yt + light_size
ym = ytb + light_spacer
ymb = ym + light_size
yb = ymb + light_spacer
ybb = yb + light_size
# Add lights
g = canvas.create_oval(x_min,yt, x_max,ytb)
y = canvas.create_oval(x_min,ym,x_max,ymb)
r = canvas.create_oval(x_min,yb,x_max,ybb)

def red_light():
    """ Configure lights for red light """
    canvas.itemconfigure(r, fill="red")
    canvas.itemconfigure(y, fill="gray")
    canvas.itemconfigure(g, fill="gray")
    canvas.after(time_red, green_light)

def yellow_light():
    canvas.itemconfigure(r, fill="gray")
    canvas.itemconfigure(y, fill="yellow")
    canvas.itemconfigure(g, fill="gray")
    canvas.after(time_yellow, red_light)

def green_light():
    canvas.itemconfigure(r, fill="gray")
    canvas.itemconfigure(y, fill="gray")
    canvas.itemconfigure(g, fill="green")
    canvas.after(time_red, yellow_light)

# Start the loop
green_light()
        
mw.mainloop()
