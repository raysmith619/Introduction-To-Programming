# turtle_screen_ondrag.py    27Nov2020  crs, from geeksforgeeks
# looking for turtle screen
#
#
# importing package 
import turtle 
  
# method to call on drag 
def fxn(x, y): 
  
    # stop backtracking 
    turtle.ondrag(None)  
  
    # move the turtle's angle and direction  
    # towards x and y 
    turtle.setheading(turtle.towards(x, y)) 
  
    # go to x, y 
    turtle.goto(x, y) 
  
    # call again 
    turtle.ondrag(fxn) 
  
# set turtle speed 
turtle.speed(10) 
  
# make turtle screen object 
sc = turtle.Screen() 
  
# set screen size 
sc.setup(400, 300) 
  
# call fxn on drag 
turtle.ondrag(fxn) 
  
# take screen in mainloop 
sc.mainloop()  