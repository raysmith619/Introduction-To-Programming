#graphical_text.py 28Feb2022  crs
# simple text support using turtle
# 
import turtle as tu


class GraphicalText:
    """ Class to support writing text to graphical
    screen
    """
    def __init__(self, screen_width=800, screen_height=None,
                 disp_left=None, disp_top=None,
                 disp_right=None, disp_bottom=None,
                 disp_boarder=None,
                 font_size_to_ch = 2,   # font size to ch height
                 dt_size = 14,          # display text size
                 text_color = "black"):
        """ Setup text screen
        :screen_width: turtle screen width default:800
        :screen_height: turtle screen height default:800
        :disp_left: display left default: -screen_width//2
        :disp_right: display right default: screen_width//2
        """
        self.screen_width = screen_width
        if screen_height is None:
            screen_height = screen_width
        self.screen_height = screen_height
        if disp_boarder is None:
            disp_boarder = min(screen_width,screen_height)//10
        self.disp_boarder = disp_boarder
        if disp_left is None:
            disp_left = -screen_width//2+disp_boarder
        self.disp_left = disp_left
        if disp_right is None:
            disp_right = screen_width//2-disp_boarder
        self.disp_right = disp_right
        if disp_top is None:
            disp_top = screen_height//2-disp_boarder
        self.disp_top = disp_top
        if disp_bottom is None:
            disp_bottom = -screen_width//2+disp_boarder
        self.disp_bottom = disp_bottom
        tu.screensize(screen_width,screen_height)         
        self.dt_x = disp_left
        self.dt_y = disp_top
        
        self.font_size_to_ch = font_size_to_ch
        self.dt_size = dt_size
        self.text_color = text_color
        
    def clear_text(self):
        """ Clear text screen and reset
        """
        tu.reset()
        self.dt_x = self.disp_left
        self.dt_y = self.disp_top
        tu.penup()
        tu.goto(self.dt_x, self.dt_y)
        tu.pendown()
        
    def display_text(self, text, size=None, colr=None,
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
        if size is None:
            size = self.dt_size
        self.size = size
        if colr is None:
            colr = self.text_color
        self.text_color = colr
        if new_line is not None:
             if x is not None or y is not None:
                raise Exeception("Must not have new_line and x,y")
        else:
            if x is not None or y is not None:
                new_line = False
            else:
                new_line = True
        if new_line:
            x = self.dt_x = self.disp_left
            self.dt_y -= size*self.font_size_to_ch
            y = self.dt_y
            #print(f"new_line: y:{y} dt_y:{self.dt_y}")
        else:
            if x is None:
                x = dt_x
            self.dt_x = x
            if y is None:
                y = self.dt_y
            self.dt_y = y
        #print(f"display_text: text:{text} x:{x}, y:{y}")
        tu.penup()
        if y < self.disp_bottom + self.disp_boarder:
            continue_msg = "Press ENTER to continue"
            inp = input(continue_msg)
            self.clear_text()    # Only option            
        
        tu.goto(x,y)
        tu.pendown()
        
        tu.color(colr)
        font = ("Arial", size, "normal")
        #print(f"colr:{colr} text:{text} font:{font}")
        #print(f"xcor():{tu.xcor()} ycor():{tu.ycor()}")
        tu.write(text, align="left", font=font)

if __name__ == "__main__":

    grt = GraphicalText()

    test_list = [
        {"text" : "First Test",
         "x": grt.disp_left, "y": grt.disp_top},
        {"text" : "Second Test", "colr" : "red"},
        {"text" : "Second Test", "colr" : "blue", 'size' : 20},
        {"text" : "Third Test", "colr" : "green", 'size' : 25},
        {"text" : "Fourth Test", "colr" : "purple", 'size' : 25},
        {"text" : "With x:300, y:300", "x" :300, "y":300}
        ]

    for test in test_list:
        grt.display_text(**test)
    grt.clear_text()        # clear text
    for test in test_list:
        grt.display_text(**test)
    
    while True:
        inp = input("x:")
        if inp != "":
            x = int(inp)
        else:
            x = None
        inp = input("y:")
        if inp != "":
            y = int(inp)
        else:
            y = None
        if x is None and y is None:
            new_line = True
        else:
            new_line = None
        inp = input("text:")
        text = inp
        grt.display_text(text, x=x,  y=y, new_line=new_line)
