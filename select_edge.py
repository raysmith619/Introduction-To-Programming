# select_edge.py        

from select_error import SelectError
from select_loc import SelectLoc
from select_part import SelectPart

class SelectEdge(SelectPart):
    width_display = 5      # Default edge display line width in pixels
    width_select = 3      # Default edge select line width in pixels
    width_standoff = 5     # Default edge buffer for adjacent parts
    width_enlarge = 2      # Enlarge number, added to width
    fill = "blue"   # Default edge color
    fill_highlight = "purple"   # Default edge highlight color

    
    def __init__(self, sel_area, rect=None):
        SelectPart.__init__(self, sel_area, "edge", rect=rect)
        self.loc = SelectLoc(rect=rect)


    def get_nodes(self, indexes=None):
        """ Find nodes/points of part
        return pairs (index, node)
        """
        nodes = []
        if indexes is None:
            nodes = [(0,self.loc.coord[0]), (1,self.loc.coord[1])]
        else:
            if not isinstance(indexes, list):
                indexes = [indexes]     # Make a list of one
            for index in indexes:
                nodes.append((index,self.loc.coord[index]))
        return nodes


    def set_node(self, index, node):
        """ Set node to new value
        """
        self.loc.coord[index] = node


    def edge_dxy(self):
        """ Get "edge direction" as x-increment, y-increment pair
        """
        loc = self.loc
        rect = loc.coord
        p1 = rect[0]
        p2 = rect[1]
        edx = p2[0] - p1[0]             # Find edge direction
        edy = p2[1] - p1[1]
        return edx, edy
                     

    
    def get_rect(self, sz_type=None, enlarge=False):
        """ Get rectangle containing edge
        Use connected corners
        Coordinates returned are ordered ulx, uly, lrx,lry so ulx<=lrx, uly<=lry
        We leave room for the corners at each end
        :edge - selected edge
        :enlarge - True - enlarge rectangle
        """
        if sz_type is None:
            sz_type=SelectPart.SZ_DISPLAY
        c1x = self.loc.coord[0][0]
        c1y = self.loc.coord[0][1]
        c3x = self.loc.coord[1][0]
        c3y = self.loc.coord[1][1]
        c1x,c1y,c3x,c3y = SelectLoc.order_ul_lr(c1x,c1y,c3x,c3y)
        """ Leave room at each end for corner """
        dir_x, dir_y = self.edge_dxy()
        wlen = self.get_edge_width(sz_type)/2
        if dir_y != 0:          # Check if in y direction
            if c1x >= wlen:     # Yes - widen the orthogonal dimension
                c1x -= wlen
            c3x += wlen
            c1y += wlen         # Yes - shorten ends to avoid corner
            c3y -= wlen
        if dir_x != 0:          # Check if in x direction
            if c1y >= wlen:     # Yes - widen the orthogonal dimension
                c1y -= wlen
            c3y += wlen
            c1x += wlen         # Yes - shorten ends to avoid corner
            c3x -= wlen
        if enlarge:
            wenlarge = SelectPart.edge_width_enlarge
            if dir_y != 0:
                c1x -= wenlarge
                c3x += wenlarge
            if dir_x != 0:
                c1y -= wenlarge 
                c3y += wenlarge
                
        return c1x,c1y,c3x,c3y


    
    def loc_key(self):
        """ Return location of part as a key
        """
        key = tuple(self.loc.coord)
        return (key)
