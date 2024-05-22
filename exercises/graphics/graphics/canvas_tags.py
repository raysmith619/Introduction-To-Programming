#canvas_tags.py    24Oct2022  crs
import tkinter as tk
import math
import time

mw = tk.Tk()

# Establish sizes
cv_width = 300          # canvas size
cv_height = cv_width*2

# Star-like object
# Demonstrating grouping by tag
#
class Star:
    tag_prefix = "Star_"
    tag_no = 0
    def __init__(self, canvas, x=0, y=0, r=100,
                 n=10,
                 color="blue", width=2,
                 tag=None):
        """ Setup initial star
        :canvas: canvas widget
        :x: center x-coordinate
        :y: center y-coordinate
        :r: radius radius default: 100
        :n: number of spokes default: 10
        :color: color default: "blue"
        :width: spoke line width default: 2
        :tag: star componens' tag default: generated
        """
        self.star_legs = []
        self.canvas = canvas
        self.x = x
        self.y = y
        self.r = r
        self.n = n
        self.color = color
        self.width = width
        if tag is None:
            Star.tag_no += 1
            tag = f"{Star.tag_prefix}{Star.tag_no}"
        self.tag = tag
        x1 = x
        y1 = y
        for i in range(n):
            theta = i * 2*math.pi / n
            x2 = x + math.cos(theta) * r
            y2 = y + math.sin(theta) * r
            line = canvas.create_line(x1,y1, x2,y2,
                                      fill=self.color,
                                      width=self.width,
                                      tag=self.tag)
            self.star_legs.append(line)

    def move_to(self, x=None, y=None):
        """ Move star to new place
        :x: new x-coordinate default: keep old x
        :y: new y-coordinate default: keep old y
        """
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        x_chg = x - self.x
        y_chg = y - self.y
        self.canvas.move(self.tag, x_chg, y_chg)
        self.x = x  # Update location
        self.y = y
        
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
             
# Add Title Text    
canvas.create_text(x_mid, y_min/2,
                   text="Star made of lines"
                       "\nwhich are moved together",
                font=20, fill="black")

# Create Star
star_r = min(x_range,y_range)/2 * .3
star1 = Star(canvas, x=x_mid,y=y_mid,
             r=star_r)
vx = x_range/3     # velocity (pixel/sec)
vy = 4*vx
delta_time = .01
while True:
    if vx > 0 and star1.x > x_max-star1.r:
        vx = -vx
    if vx < 0 and star1.x < x_min+star1.r:
        vx = -vx
    if vy > 0 and star1.y > y_max-star1.r:
        vy = -vy
    if vy < 0 and star1.y < y_min+star1.r:
        vy = -vy
    delta_x = delta_time*vx
    delta_y = delta_time*vy
    new_x = star1.x+delta_x
    new_y = star1.y+delta_y
    star1.move_to(x=new_x, y=new_y)
    mw.update()
    time.sleep(delta_time)

tk.mainloop()
