# select_loc.py

from select_error import SelectError
from select_trace import SlTrace

class SelectLoc(object):
    """ Selection Part Location - contains information about
    handle location and shape point if point, rect if rectangle
    else error
    """
    LOC_NONE = 0            # None or unknown
    LOC_POINT = 1           # A point or like point with x,y
    LOC_RECT = 2            # A rectangle with x1,y1 x2,y2

    """ Selection handle such as corner or edge
    Used to facilitate repositioning or resizing
    Contains display information such as is_highlighted
    Type (point OR rect)
    """
    @staticmethod
    def order_ul_lr(c1x,c1y,c3x,c3y):
        """ Order corners so c1x,c1y is upper left """
        if c1x > c3x:
            tmp = c1x
            c1x = c3x
            c3x = tmp
        if c1y > c3y:
            tmp = c1y
            c1y = c3y
            c3y = tmp
        return c1x, c1y, c3x,c3y



    
    def __init__(self, point=None, rect=None):
        if point is not None:
            self.type = SelectLoc.LOC_POINT
            self.coord = point
        elif rect is not None:
            self.type = SelectLoc.LOC_RECT
            """ Order location points to ensure ul, lR placement
            """
            c1x,c1y,c3x,c3y = SelectLoc.order_ul_lr(
                rect[0][0], rect[0][1], rect[1][0], rect[1][1])
            self.coord = [(c1x,c1y), (c3x,c3y)]
        else:
            raise SelectError("SelectPart requires point or rect")


    def move_nodes(self, delta_x, delta_y, nodes):
        """ Adjust location node(s) by delta_x, delta_y position
        :delta_x: adjustment in x direction
        :delta_y: adjustment in y direction
        :nodes: node indexes(s) of the node coordinate(s) to adjust
                default: all nodes
                if not list - one node
        """
        if nodes is None:
            if self.type == SelectLoc.LOC_POINT:
                nodes = [0]
            elif self.type == SelectLoc.LOC_RECT:
                nodes = [0,1]
            else:
                raise SelectError("move_nodes unrecognized type: %s" % self.type)
        if not isinstance(nodes, list):
            nodes = [nodes]     # list of one
        
        for node in nodes:
            self.move_node(delta_x, delta_y, node)

    
    def move_node(self, delta_x, delta_y, node):
        """ Adjust single node(coordinate)
        """
        SlTrace.lg("adjust_node: %d[%d] by delta_x=%d,delta_y=%d"
               % (self.type, node, delta_x, delta_y), "adjust")
        if self.type == SelectLoc.LOC_POINT:
            if node != 0:
                return          # Only one coordinate - ignore others
            self.coord = (self.coord[0]+delta_x, self.coord[1]+delta_y)
        elif self.type == SelectLoc.LOC_RECT:
            new_rect = [(self.coord[0][0], self.coord[0][1]),
                        (self.coord[1][0], self.coord[1][1])]
            new_rect[node] = (new_rect[node][0]+delta_x, new_rect[node][1]+delta_y)
            self.coord = new_rect  
        else:
            raise SelectError("move_node unrecognized node type %d" % self.type)
        

    def __str__(self):
        """ Provide reasonable view of location
        """
        desc = ""
        if self.type == SelectLoc.LOC_POINT:
            desc += " point: xy=(%d,%d)" % (self.coord[0], self.coord[1])
        elif self.type == SelectLoc.LOC_RECT:
            desc += (" rect: p1=(%d,%d) p2=(%d,%d)"
             % (self.coord[0][0], self.coord[0][1],
                 self.coord[1][0], self.coord[1][1]))
        else:
            desc += " UNKNOWN"
            
        return desc
