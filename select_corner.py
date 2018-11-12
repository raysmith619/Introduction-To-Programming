# select_corner.py        

from select_error import SelectError
from select_loc import SelectLoc
from select_part import SelectPart

class SelectCorner(SelectPart):
    corner_width_display = 8    # Default display size of corner in pixels
    corner_width_select = 8    # Default select size of corner in pixels
    corner_width_standoff = 10    # Default standoff size of corner in pixels
    corner_fill = "red" # Default corner color
    corner_fill_highlight = "pink"      # Default corner highlight color

    
    def __init__(self, sel_area, point=None):
        SelectPart.__init__(self, sel_area, "corner", point=point)
        self.loc = SelectLoc(point=point)


    def get_nodes(self, indexes=None):
        """ Find nodes/points of part
        return pairs (index, node)
        """
        return [(0,self.loc.coord)]


    def set_node(self, index, node):
        """ Set node to new value
        """
        if index != 0:
            raise SelectError("set_node %s non-zero index %d"
                              % (self, index))
        self.loc.coord = node


    def edge_dxy(self):
        """ Get "edge direction" as x-increment, y-increment pair
        """
        return 0,0                  # No change
        
                     

    
    def get_rect(self, sz_type=None, enlarge=False):
        """ Get rectangle containing edge handle
        Use connected corners
        Coordinates returned are ordered ulx, uly, lrx,lry so ulx<=lrx, uly<=lry
        We leave room for the corners at each end
        :edge - selected edge
        :enlarge - True - enlarge rectangle
        """
        if sz_type is None:
            sz_type=SelectPart.SZ_DISPLAY
        wlen = self.get_edge_width(sz_type)
        
        c1x = self.loc.coord[0]
        c1y = self.loc.coord[1]
        c3x = c1x
        c3y = c1y
        if c1x >= wlen/2:     # Yes - widen the orthogonal dimension
            c1x -= wlen/2
        c3x += wlen
        if c1y >= wlen:     # Yes - widen the orthogonal dimension
            c1y -= wlen/2
        c3y += wlen
        if enlarge:
            wenlarge = SelectPart.edge_width_enlarge
            c1x -= wenlarge
            c3x += wenlarge
                
        return c1x,c1y,c3x,c3y


    
    def loc_key(self):
        """ Return location of part as a key
        """
        key = self.loc.coord
        return (key)
