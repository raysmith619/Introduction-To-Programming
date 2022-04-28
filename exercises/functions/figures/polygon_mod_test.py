#polygon_mod_test.py   21Jan2022  crs, from polygon_mod.py
"""
Test program fore polygon_mod.py
"""

from polygon_mod import polygon

print("polygon_mod test")

colors = ["red", "orange", "yellow",
          "green", "blue", "indigo",
          "violet"]

nfig = 12
xbeg  = -600
xend = 600
xrange = xend-xbeg
ybeg = -600
yend = 600
yrange = yend-ybeg
side = .80*min(xrange,yrange)/nfig
wid = 4
xoff = 40   # offsets for second polygon
yoff = 20   
for i in range(nfig):
    nside = i + 3           # Start with triangle
    x = xbeg + i*side
    y = ybeg + side/2 +(i+1)*side
    polygon(nside=nside, x=x, y=y,
            side=side*(1-((i-1)/nfig)), # Shrink polygons
            clr=colors[i%len(colors)], wid=wid)
    
                                # Second with defaults
                                # except for offset position
                                # and line width
    polygon(x=x+2*xoff, y=y+yoff, wid=wid+2)
    polygon(x=x+4*xoff, y=y+2*yoff)
    polygon(x=x+6*xoff, y=y+4*yoff)
    
