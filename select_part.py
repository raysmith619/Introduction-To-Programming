# select_part.py        

from select_error import SelectError
from select_loc import SelectLoc
from select_trace import SlTrace

def color_to_fill(color):
    """ Color integer into fill text
    """
    if color is None:
        return "None"
    
    return "#%06X" % color



class PartHighlight(object):
    """ Information about highlighted part
    """
    
    def __init__(self, part, xy=None):
        """ Record highlighting information
        :part: highlighted part
        :tag: graphics tag for deleting/redisplay
        :xy: x,y coordinates of mouse on canvas
        """
        self.part  = part
        self.xy = xy


class SelectPart(object):
    
    SZ_DISPLAY  = 1             # Size for display
    SZ_SELECT = 2               # Size for selection
    SZ_STANDOFF = 3             # Size for standoff
    
    edge_width_display = 5      # Default edge display line width in pixels
    edge_width_select = 3      # Default edge select line width in pixels
    edge_width_standoff = 5     # Default edge buffer for adjacent parts
    edge_width_enlarge = 2      # Enlarge number, added to width
    edge_fill = "blue"   # Default edge color
    edge_fill_highlight = "purple"   # Default edge highlight color
    corner_width_display = 8    # Default display size of corner in pixels
    corner_width_select = 8    # Default select size of corner in pixels
    corner_width_standoff = 10    # Default standoff size of corner in pixels
    corner_fill = "red" # Default corner color
    corner_fill_highlight = "pink"      # Default corner highlight color
    region_fill = "clear"   # Default edge color
    region_fill_highlight = "lightgray"   # Default edge highlight color

    id = 0          # Unique handle ID
            
            
    @staticmethod
    def is_point_equal(pt1, pt2):
        """ Check if points are equal
        """
        if pt1[0] == pt2[0] and pt1[1] == pt2[1]:
            return True
        
        return False
    

    @staticmethod
    def get_olaps(parts, sz_type=None, enlarge=False):
        """ Get overlapping rectangle, if any, of a list of parts
        """
        if len(parts) < 2:
            return None
        
        part1 = parts.pop()
        for part in parts:
            olap_rect = part1.get_overlap(part, sz_type=sz_type, enlarge=enlarge)
            if olap_rect is None:
                return None
            
            part1 = SelectPart(part.sel_area, part_type="edge", rect=olap_rect)
        return olap_rect

    @classmethod
    def get_edge_width(cls, sz_type=SZ_DISPLAY):
        """ Return class edge width
        :sz_type:  size type
        """
        width = cls.edge_width_display
        if sz_type == cls.SZ_SELECT:
            width = cls.edge_width_select
        elif sz_type == cls.SZ_STANDOFF:
            width = cls.edge_width_standoff           
        return width



    @classmethod
    def set_edge_width_cls(cls, display=None, select=None, standoff=None):
        """ Set edge width(s)
        """
        if display is not None:
            cls.edge_width_display = display
        if select is not None:
            cls.edge_width_select - select
        if standoff is not None:
            cls.edge_width_standoff = standoff
            return (cls.edge_width_display, cls.edge_width_select,
                    cls.edge_width_standoff)
    
    @classmethod
    def get_corner_rect_at_pt(cls, pt, sztype=None, enlarge=False):
        """ Get corner rectangle at given point
        """
        if sztype is None:
            sztype=cls.SZ_DISPLAY
        corner_width = cls.corner_width_display
        if sztype == SelectPart.SZ_DISPLAY:
            corner_width = cls.corner_width_display
        elif sztype == SelectPart.SZ_SELECT:
            corner_width = cls.corner_width_select
        elif sztype == SelectPart.SZ_STANDOFF:
            corner_width = cls.corner_width_standoff
            
        c1x = pt[0]
        if c1x >= corner_width/2:
            c1x -= corner_width/2
        c1y = pt[1]                 # inside upper left  corner
        if c1y >= corner_width/2:
            c1y -= corner_width/2
        if isinstance(c1x, list):
            print("c1x is a list")
        c3 = (c1x + corner_width, c1y + corner_width)
        c3x = c3[0]
        c3y = c3[1]
                                                    # Enlarge a bit
        if enlarge:
            el = 2                  # enlarge number of pixels
            c1x -= el
            c1y -= el
            c3x += el
            c3y += el
        
        """ Ensure uL to left and above lR """
        return SelectLoc.order_ul_lr(c1x,c1y,c3x,c3y)


    @classmethod
    def part_loc_key(cls, part_type, pt1, pt2=None):
        """ Return location of part as a key
        Used in determining if part is already present
        """
        if part_type == "corner":
            return pt1
        
        elif part_type == "edge":
            return (pt1,pt2)
        
        elif part_type == "region":
            return (pt1,pt2)
        
        raise SelectError("loc_key - unrecognized part_type: %s" % part_type)


    
    def __init__(self, sel_area, part_type,
                 point=None, rect=None, tag=None, xy=None,
                 color=None,
                 row=0, col=0):
        """ Selection Part setup
        :sel_area: - reference to region of operation and display
        :part_type: string describing type edge, corner, region
        :point, rect: description of location
        :row: optional row number, generally 1 - n
        :col: optional col number, generally 1 - n
        """
        if sel_area is None:
            raise SelectError("SelectPart missing sel_area")
        
        self.sel_area = sel_area
        SelectPart.id += 1
        self.id = SelectPart.id
        self.connecteds = []            # Start with none connected
        self.adjacents = []             # Start with none adjacent
        self.part_type = part_type
        self.highlighted = False
        self.highlight_tag = None
        self.display_tag = tag
        self.set_edge_width(SelectPart.edge_width_display,
                                     SelectPart.edge_width_select,
                                     SelectPart.edge_width_standoff)
        self.color = color
        self.row = row
        self.col = col
        if point is not None:
            self.loc = SelectLoc(point=point)
        elif rect is not None:
            self.loc = SelectLoc(rect=rect)
        else:
            raise SelectError("SelectPart: neither point nor rect type")


    def __str__(self):
        """ Provide reasonable view of part
        """
        return self.part_type + " id=%d" % self.id + " at %s" % self.loc 


    def get_nodes(self, indexes=None):
        """ Find nodes/points of part
        return pairs (index, node)
        """
        if self.is_corner():
            return [(0,self.loc.coord)]
        elif self.is_edge():
            nodes = []
            if indexes is None:
                nodes = [(0,self.loc.coord[0]), (1,self.loc.coord[1])]
            else:
                if not isinstance(indexes, list):
                    indexes = [indexes]     # Make a list of one
                for index in indexes:
                    nodes.append((index,self.loc.coord[index]))
            return nodes
        else:
            return []

    def set_color(self, color):
        """ Set color
        :returns: previous color
        No display done here
        """
        prev_color = self.get_color()
        self.color = color        
        return prev_color

    def set_node(self, index, node):
        """ Set node to new value
        """
        if self.is_corner():
            if index != 0:
                raise SelectError("set_node %s non-zero index %d"
                                  % (self, index))
            self.loc.coord = node
        elif self.is_edge():
            self.loc.coord[index] = node
        elif self.is_region():
            self.loc.coord[index] = node
        else:
            raise SelectError("set_node: % Unrecognized part type:%d" 
                              % (self, self.part_type))             



    def display_clear(self):
        """ Clear display of this part
        """
        if not self.is_highlighted() and self.display_tag is not None:   # leave alone if highlighted
            self.sel_area.canvas.delete(self.display_tag)
            self.display_tag = None
        if self.highlight_tag is not None:
            self.sel_area.canvas.delete(self.highlight_tag)
            self.highlight_tag = None
        if hasattr(self, 'move_tag') and self.move_tag is not None:
            self.sel_area.canvas.delete(self.move_tag)
            self.move_tag = None
        if hasattr(self, 'partno_tag') and self.partno_tag is not None:
            self.sel_area.canvas.delete(self.partno_tag)
            self.partno_tag = None
    

    def display_info(self):
        if hasattr(self, "partno"):
            partnostr = str(self.partno)
        else:
            partnostr = "--"
        fillstr = self.get_fill()
        
        SlTrace.lg("over %s row=%d col=%d partno=%s fill=%s"
                    % (self.part_type, self.row, self.col, partnostr, fillstr))
    
    def edge_dxy(self):
        """ Get "edge direction" as x-increment, y-increment pair
        """
        loc = self.loc
        if loc.type == SelectLoc.LOC_POINT:
            return 0,0                  # No change
        elif loc.type == SelectLoc.LOC_RECT:
            rect = loc.coord
            p1 = rect[0]
            p2 = rect[1]
            edx = p2[0] - p1[0]             # Find edge direction
            edy = p2[1] - p1[1]
        else:
            raise SelectError("edge_dxy: unrecognized loc type")
        return edx, edy

        
    def highlight_clear(self, tag=None):
        if self.is_highlighted():
            del self.sel_area.highlights[self.id]
            if self.highlight_tag is not None:
                self.sel_area.canvas.delete(self.highlight_tag)
                self.display_tag = None
            self.highlighted = False

        
    def highlight_set(self, tag=None):
        self.highlighted = True
        self.highlight_tag = tag
        self.sel_area.highlights[self.id] = PartHighlight(self)


    def is_highlighted(self):
        return self.highlighted

    def get_color(self):
        if hasattr(self, "color"):
            color = self.color 
        else:
            color = 0
        return color
    
    def get_fill(self):
        color = self.get_color()
        fill = color_to_fill(color)
        return fill

    def get_partno(self):
        if hasattr(self, "partno"):
            partno = self.partno 
        else:
            partno = 0
        return partno
    
    def get_connected_index(self, part):
        """ Get connected part index (end), to which we are connected
        0, 1 for edges, 0 for others
        """
        is_connected = False           # Set True if find a connection
        for eci, connected in enumerate(part.connecteds):
            if self.is_same(connected):
                is_connected = True
                break     # Got corner's end of edge
        if not is_connected:
            return None
        
        return eci
    
    
    def get_connected_loc_indexes(self, part):
        """ Get connected part's location index which we share
        Returns pair our index, other index
        """
        is_connected = False           # Set True if find a connection
        our_type = self.part_type
        our_loc = self.loc
        our_coord = our_loc.coord
        part_type = part.part_type
        part_loc = part.loc
        part_coord = part_loc.coord
        
        if isinstance(our_coord, list):
            our_coords = our_coord
        else:
            our_coords = [our_coord]
        
        if isinstance(part_coord, list):
            part_coords = part_coord
        else:
            part_coords = [part_coord]
                
        for oc in our_coords:
            for pci, pc in enumerate(part_coords):
                try:
                    if oc[0] == pc[0] and oc[1] == pc[1]:
                        pcio = 1 - pci      # only two 
                        return pci, pcio
                except:
                    raise SelectError("oc,pc compare failed")
                 
        return 0,0
    
    
    def get_unconnected_index(self, part):
        """ Get unconnected part index (far end), to which we are connected
        0, 1 for edges, 0 for others
        """
        is_not_connected = False           # Set True if find a connection
        for eci, connected in enumerate(part.connecteds):
            if not self.is_same(connected):
                is_not_connected = True
                break     # Got corner's far end of edge
        if not is_not_connected:
            return None
        
        return eci

    def get_points(self):
        """ return p1, p2 of edge
        """
        nodes = self.get_nodes()
        points = []
        for node in nodes:
            points.append(node[1])
        return points
    
    

    def get_rect(self, sz_type=None, enlarge=False):
        """ Return type of  rectangle for this part
        """
        from select_edge import SelectEdge
        SlTrace.lg("%s needs own get_rect" % self.part_type)
        rect = SelectEdge.get_rect(self, sz_type=sz_type, enlarge=enlarge)
        return rect

    def get_corner_width(self, sz_type=None):
        if sz_type is None:
            sz_type=SelectPart.SZ_DISPLAY
        width = SelectPart.corner_width_display
        if sz_type == SelectPart.SZ_SELECT:
            width = SelectPart.corner_width_select
        elif sz_type == SelectPart.SZ_STANDOFF:
            width = SelectPart.corner_width_standoff


    def get_overlap(self, part, sz_type=None, enlarge=False):
        """ return rectangle normalized (p1,p2) which part we and part overlap, None if no overlap
        Note: get_rect returns normalized rectangles
        :part: possibly overlapping part
        :sz_type:  size type Default:  SelectPart.SZ_SELECT
        :enlarge:  True  - part is enlarged(highlighted)
        :returns: overlap rectangle if any overlap, None if no overlap
        """
        if sz_type is None:
            sz_type = SelectPart.SZ_SELECT
        self_xyxy = self.get_rect(sz_type=sz_type)
        part_xyxy = part.get_rect(sz_type=sz_type, enlarge=enlarge)
        X1 = 0
        Y1 = 1           # Mnemonic
        X2 = 2
        Y2 = 3
        """ Find left most rectangle """
        left_x = self_xyxy[X1]
        left_xyxy = self_xyxy
        right_xyxy = part_xyxy
        if part_xyxy[X1] < left_x:
            left_x = part_xyxy[X1]
            left_xyxy = part_xyxy
            right_xyxy = self_xyxy
        if right_xyxy[X1] > left_xyxy[X2]:
            return None         # left rectangle totally left of right
        
        olap_x1 = right_xyxy[X1]      # left edge of right rectangle
        if right_xyxy[X2] > left_xyxy[X2]:
            olap_x2 = left_xyxy[X2]       # limited by left rectangle
        else:
            olap_x2 = right_xyxy[X2]      # limited by right rectangle  

        """ Find top most rectangle """
        upper_y = self_xyxy[Y1]
        upper_xyxy = self_xyxy
        lower_xyxy = part_xyxy
        if part_xyxy[Y1] < upper_y:
            upper_y = part_xyxy[Y1]
            upper_xyxy = part_xyxy
            lower_xyxy = self_xyxy
        if lower_xyxy[Y1] > upper_xyxy[Y2]:
            return None         # upper rectangle totally above of lower
        
        olap_y1 = lower_xyxy[Y1]      # upper edge of lower rectangle
        if lower_xyxy[Y2] > upper_xyxy[Y2]:
            olap_y2 = upper_xyxy[Y2]       # limited by upper rectangle
        else:
            olap_y2 = lower_xyxy[Y2]      # limited by lower rectangle  


        return [(olap_x1,olap_y1), (olap_x2, olap_y2)]
        
        
    def get_x(self):
        return self.get_xy()[0]

    
    def get_y(self):
        return self.get_xy()[1]
    
        
    def get_xy(self):
        return self.loc_to_xy()    


    def is_over(self, x, y, sz_type=None, enlarge=False):
        """ Return True if part is over (x,y) ie. point (x,y) is within
        our part
        :x,y: - x,y coordinates on canvas
        :enlarge: - enlarged rectangle (highlighted part)
        """
        if sz_type is None:
            sz_type=SelectPart.SZ_SELECT
        try:
            c1x,c1y,c3x,c3y = self.get_rect(sz_type=sz_type, enlarge=enlarge)
        except:
            raise SelectError("bad get_rect call")
        if x >= c1x and x <= c3x and y >= c1y and y <= c3y:
            SlTrace.lg("is_over: %s : c1x:%d, c1y:%d, c3x:%d, c3y:%d" % (self, c1x,c1y,c3x,c3y), "is_over")
            return True
        
        return False
    
    
    def loc_to_xy(self, loc=None):
        """ Convert handle object location to associated point
        Upper left corner
        """
        if loc is None:
            loc = self.loc
        loc_type = loc.type
        if loc_type == SelectPart.LOC_POINT:
            pt = loc.coord
            return (pt[0],pt[1])
        elif loc_type == SelectPart.LOC_RECT:
            rect = loc.coord
            p1 = rect[0]
            p1x = p1[0]
            p1y = p1[1]
            return (p1x, p1y)
        else:
            raise SelectError("loc_to_xy: unrecognized loc type %d(%s)" % (loc_type, loc))

    
    def loc_key(self):
        """ Return location of part as a key
        Should be overridden by all derived classes
        """
        raise SelectError("loc_key - unrecognized part_type: %s" % self.part_type)

                        
    def set_xy(self, xy=None):
        self.xy = xy 

    def is_corner(self):
        if self.part_type == "corner":
            return True
        return False

    def is_edge(self):
        if self.part_type == "edge":
            return True
        return False

    def is_region(self):
        if self.part_type == "region":
            return True
        return False
    
            
    def add_adjacent(self, handle):
        """ Add to list of adjacent, parts affected by changes
        to this part but not connected
        """
        if not self.is_adjacent(handle):
            self.adjacents.append(handle)
        return handle
    
            
    def add_connected(self, handle):
        """ Add to list of connected, parts affected by changes
        to this handle
        """
        if not self.is_connected(handle):
            self.connecteds.append(handle)
        return handle
    
    
    def is_adjacent(self, part):
        """ Test if part already adjacent to us
        """
        for con in self.adjacents:
            if part.id == con.id:
                return True
    
    
    def is_connected(self, handle):
        """ Test if handle already connected to us
        """
        for con in self.connecteds:
            if handle.id == con.id:
                return True

    def is_covering(self, part):
        """ Check if parts cover each other
        :returns:  True if same rectangle
        """
        if self.get_rect() == part.get_rect():
            return True
        
        return False
        
    
    def is_same(self, handle):
        """ Determine if handle is same as us
        """
        if self.id == handle.id:
            return True
        return False
        
    def set_edge_width(self, display=None, select=None, standoff=None):
        """ Set edge width(s)
        """
        if display is not None:
            self.edge_width_display = display
        if select is not None:
            self.edge_width_select - select
        if standoff is not None:
            self.edge_width_standoff = standoff
            return (self.edge_width_display, self.edge_width_select,
                    self.edge_width_standoff)
                     

    def unhighlight(self):
        """ Remove highlight from part, if any, restoring previous color.
        """
        self.highlight_clear()
            