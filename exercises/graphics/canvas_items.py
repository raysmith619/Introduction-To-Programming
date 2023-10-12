#canvas_items.py    23Oct2022  crs, From resource_lib_proj/
import tkinter as tk
mw = tk.Tk()
cv_width = 300
cv_height = cv_width*2
x_min = cv_width*.1
x_max = cv_width*.9
x_mid = (x_min+x_max)/2
y_min = cv_height*.1
y_max = cv_height*.9
y_mid = (y_min+y_max)/2

canvas = tk.Canvas(mw, width=cv_width, height=cv_height)
canvas.pack()

canvas.create_rectangle(x_min, y_min, x_max, y_max,
                        fill="green")

line = canvas.create_line(x_min,y_min,
                          x_max,y_max, fill="red",
                          width=10)    
line2 = canvas.create_line(x_min,y_max,
                           x_max, y_min, fill="blue")
oval = canvas.create_oval(x_mid,y_min, x_max, y_max,
                          fill="orange")
x_q = (x_min+x_mid)/2
y_q = (y_min+y_mid)/2
sq = canvas.create_rectangle(x_q, y_q,
                             x_mid, y_mid,
                             fill="yellow")
canvas.create_text(x_mid,y_mid, text="Hello World",
                   font="Tahoma 30")
tk.mainloop()
