#ball_2d_table.py  26Aug2021  crs, from ball_2d.py
#                  12Aug2021  crs, Author
"""
Two dimentional billiard table
"""
class Ball2dTable:
    def __init__(self, color="green", fill=None,
                 length=9,
                 width=None,
                 rotation=None):
        """ Define/Setup Tables's attributes
        :color: table's color default: green
        :fill: table fill color
                default: same as color
        :length: length in feet
                default: 9
        :width: width in feet
                default: length/2
        :rotation: length orientation in degrees
                default: No rotation
         """
        self.color = color
        if fill is None:
            fill = color
        self.fill = fill
        self.length = length
        if width is None:
            width = length/2
        self.width = width
        self.rotation = rotation
        
    def __str__(self):
        """ String representation of ball???
        """
        table_str = f"Ball2dTable:{self.color}"
        table_str += f" length:{self.length} x {self.width} ft"
        return table_str
        
# Self Test
if __name__ == "__main__":
    t1 = Ball2dTable()
    t2 = Ball2dTable(color="blue", length=7)
    t3 = Ball2dTable(color="red", length=2, width=2)
    print(f"{i:4}\n\tt1: {t1}\n\tt2: {t2}\n\tt3: {t3}")
        
