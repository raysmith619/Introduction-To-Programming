# turtle_onclick_a.py    27Nov2020  crs, from geeksforgeeks

from turtle import * 
  
rainbow = ["red", "orange", "yellow", "green",
           "blue", "indigo", "violet"]
color_index = len(rainbow)  # Starting color
# screen object 
wn = Screen()   # Required for event(e.g. click) 
  
# method to perform action 
def fxn(x, y):
  global color_index  # Required if changing outside var
  color_index = (color_index + 1)%len(rainbow)
  color(rainbow[color_index])
  goto(x, y) 
  
# onclick action  
wn.onclick(fxn) 
wn.mainloop()
