# turtle_onclick_1.py    27Nov2020  crs, from geeksforgeeks

import turtle 
  
  
# screen object 
wn = turtle.Screen() 
  
# method to perform action 
def fxn(x, y): 
  turtle.goto(x, y) 
  #turtle.write(str(x)+","+str(y)) # print coordinates
  
# onclick action  
wn.onclick(fxn) 
wn.mainloop()
