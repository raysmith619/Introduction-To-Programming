# select_edge.py        
from select_trace import SlTrace
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

    
    def __init__(self, sel_area, rect=None, draggable=True, invisible=False):
        SelectPart.__init__(self, sel_area, "edge", rect=rect,
                            draggable=draggable, invisible=invisible)
        self.loc = SelectLoc(rect=rect)



    
    def display(self):
        """ Display edge as a rectangle
        We leave room for the corners at each end
        Highlight if appropriate
        """
        if self.invisible and not self.highlighted:
            return
        
        loc = self.loc
        SlTrace.lg("edge: %s" % str(loc), "display")
        if self.highlighted:
            if self.turned_on:
                if self.on_highlighting:
                    c1x,c1y,c3x,c3y = self.get_rect(enlarge=True)
                    self.highlight_tag = self.sel_area.canvas.create_rectangle(
                                        c1x, c1y, c3x, c3y,
                                        fill=SelectPart.edge_fill_highlight)
            else:
                if self.off_highlighting:
                    c1x,c1y,c3x,c3y = self.get_rect(enlarge=True)
                    self.highlight_tag = self.sel_area.canvas.create_rectangle(
                                        c1x, c1y, c3x, c3y,
                                        fill=SelectPart.edge_fill_highlight)
        else:
            self.display_clear()
            c1x, c1y, c3x, c3y = self.get_rect()
            self.display_tag = self.sel_area.canvas.create_rectangle(
                                c1x, c1y, c3x, c3y,
                                fill=self.color)
        if SlTrace.trace("show_id"):
            dir_x, dir_y = self.edge_dxy()
            chr_w = 5
            chr_h = chr_w*2
            if dir_x != 0:      # sideways
                offset_x = -len(str(self.id))*chr_w/2 + chr_w
                offset_y = chr_h
            if dir_y != 0:      # up/down
                offset_x = len(str(self.id))*chr_w
                offset_y = 0    
        
            cx = (c1x+c3x)/2 + offset_x
            cy = (c1y+c3y)/2 + offset_y
            self.name_tag = self.display_text((cx, cy), text=str(self.id))


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
        corner1 = self.get_corner(c1x, c1y)
        corner1_x, corner1_y, corner_size = corner1.get_center_size()
        dir_x, dir_y = self.edge_dxy()
        wlen = self.get_edge_width(sz_type)/2
        wlen_off = self.get_edge_width_cls(sz_type)/2
        if dir_y != 0:          # Check if in y direction
            if c1x >= wlen:     # Yes - widen the orthogonal dimension
                c1x -= wlen
            c3x += wlen
            c1y += wlen_off         # Yes - shorten ends to avoid corner
            c3y -= wlen_off
        if dir_x != 0:          # Check if in x direction
            if c1y >= wlen:     # Yes - widen the orthogonal dimension
                c1y -= wlen
            c3y += wlen
            c1x += wlen_off         # Yes - shorten ends to avoid corner
            c3x -= wlen_off
        if enlarge:
            wenlarge = SelectPart.edge_width_enlarge
            if dir_y != 0:
                c1x -= wenlarge
                c3x += wenlarge
            if dir_x != 0:
                c1y -= wenlarge 
                c3y += wenlarge
                
        return c1x,c1y,c3x,c3y


    def get_corner(self,cx, cy):
        """ Get corner close to c1x,c1y
        :cx: end of rectangle
        :cy:  end of rectangle
        """
        corners = self.get_corners()

    
    def get_parts(self, type=None):
        return self.get_connecteds()
    
            
    def highlight(self):
        """ Highlight and display
        """
        self.highlight_set(display=True)    #Just to remind ourselves that we do the display


    
    def loc_key(self):
        """ Return location of part as a key
        """
        key = tuple(self.loc.coord)
        return (key)
