#square_simp.py  10Apr2022  crs, from square.py
"""
Simple visual example of object
Show inheritance
"""
from rectangle_simp import Rectangle

class Square(Rectangle):
    def __init__(self, side=100, **kwargs):
        self.side = side
        kwargs['width'] = kwargs['height'] = side
        super().__init__(**kwargs)


if __name__ == '__main__':
    from random import randint
    import turtle as tu
    
    tu.speed('fastest')     # speedup
    colors = ["red", "orange", "yellow",
              "green", "blue", "indigo",
              "violet"]
    nrec = 15
    size = 800
    x_beg = y_beg = -size/2
    x_end = y_end = size/2
    inc = int(size/nrec)
    x = x_beg
    y = y_beg
    for i in range(nrec):
        side = randint(inc,x_end-x)
        edge = i+1
        color = colors[i%len(colors)]
        fill = i % 2
        rec = Square(x=x, y=y, side=side,
                        color=color,fill=fill)
        x += inc
        y += inc
