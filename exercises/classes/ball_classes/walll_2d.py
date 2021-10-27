#wall_2d.py     08Oct2021  crs, from ball_2d.py
#               12Aug2021  crs, Author
"""
Two dimentional wall
"""
class Wall2d:
    def __init__(self, color="green",
                 width=1,
                 beg_x=0, beg_y=0,
                 end_x=300, end_y=0):
        """ Define/Setup Wall's attributes
        :color: wall's color default: black
        :width: width(thickness) in default units
                default: 1
        :beg_x: x (horizontal right) in default units
                default: 0
        :beg_y: y (vertical down) in default units
                default: 0
        :end_x: x (horizontal right) default
                    units, default time inc
                default: 300
        :end_y: y (vertical down)
                default: 0
        """
        self.color = color
        self.width = width
        self.beg_x = beg_x
        self.beg_y = beg_y
        self.end_x = end_x
        self.end_y = end_y
        
    def __str__(self):
        """ String representation of wall
        """
        w_str = f"Wall2d:{self.color}"
        w_str += f" w:{self.width}"
        w_str += f" beg_xy:{self.beg_x},{self.beg_y}"
        w_str += f" end_xy:{self.end_x},{self.end_y}"
        return w_str
        
        
# Self Test
if __name__ == "__main__":
    w1 = Wall2d()
    print(f"w1:{w1}")
    w2 = Wall2d(beg_x=20, end_x=200)
    print(f"w2:{w2}")
        
