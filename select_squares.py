"""
Created on Oct 30, 2018

@author: raysmith
Creation and Manipulation of the grid (dots and squares)
of the old squares game
"""
from select_trace import SlTrace
from select_area import SelectArea

class SelectSquares(object):
    """
    classdocs
    """


    def __init__(self, canvas, nrows=10,
                  ncols=None,
                  width=None, height=None, tbmove=.1,
                  highlight_limit=1):
        """
        :canvas: - canvas within we are placed
        :nrows: number of rows of squares default: 10
        :ncols: number of columns of squares default: rows
        :width: window width
        :height: window height
        :tbmove: minimum time(seconds) between move detection
        :highlight_limit: limit highlighting (seconds)
                default: 1 (None - no limit)
        """
        if ncols is None:
            ncols = nrows
        self.canvas = canvas
        self.nrows = nrows
        if width is None:
            width = canvas.winfo_width()
        if height is None:
            height = canvas.winfo_height()
        self.drawn_lines = []           # lines drawn
            
        min_xlen = 10
        min_ylen = min_xlen
        self.tbmove = tbmove
        self.highlight_limit = highlight_limit
        
        rects =  []
        rects_rows = []         # So we can pass row, col
        rects_cols = []
        
        def rn(val):
            return int(round(val))
        xmin = .1*float(width)
        xmax = .9*float(width)
        xlen = (xmax-xmin)/float(ncols)
        min_xlen = float(min_xlen)
        if xlen < min_xlen:
            SlTrace.lg("xlen(%.0f) set to %.0f" % (xlen, min_xlen))
            xlen = min_xlen
        ymin = .1*float(height)
        ymax = .9*float(height)
        ylen = (ymax-ymin)/float(nrows)
        min_ylen = float(min_ylen)
        if ylen < min_ylen:
            SlTrace.lg("ylen(%.0f) set to %.0f" % (ylen, min_ylen))
            ylen = min_ylen
        for i in range(int(ncols)):
            col = i+1
            x1 = xmin + i*xlen
            x2 = x1 + xlen
            for j in range(int(nrows)):
                row = j+1
                y1 = ymin + j*ylen
                y2 = y1 + ylen
                rect = ((rn(x1), rn(y1)), (rn(x2), rn(y2)))
                rects.append(rect)
                rects_rows.append(row)
                rects_cols.append(col)
        
        self.area = SelectArea(canvas, tbmove=self.tbmove,
                               highlight_limit=self.highlight_limit)
        ###SelectRegion.reset()
        for i, rect in enumerate(rects):
            row = rects_rows[i]
            col = rects_cols[i]
            self.area.add_rect(rect, row=row, col=col,
                            draggable_edge=False,
                            draggable_corner=False,
                            draggable_region=False,   
                            invisible_region=True,
                            invisible_edge=True)
        for part in self.area.get_parts():
            if part.is_corner():
                part.set(display_shape="circle",
                           display_size=10,
                           color="blue")
            elif part.is_edge():
                part.set(edge_width_select=50,
                           edge_width_display=5,
                           on_highlighting=False,
                           color="lightgreen")

        self.area.add_down_call(self.down_click)        # Connect our processing
        self.area.add_stroke_call(self.stroke_call)      # Treat stroke as down_click
        self.complete_square_call = None                # Setup for complete square call
        self.new_edge_call = None                       # Setup for new edge call
        self.area.add_turned_on_part_call(self.new_edge)
        
    
    def add_complete_square_call(self, call_back):
        """ Add function to be called upon completed square
        :call_back: call back (edge, region) - None - remove call back
        """
        self.complete_square_call = call_back

    
    def add_new_edge_call(self, call_back):
        """ Add function to be called upon newly added edge
        :call_back: call back (edge) - None - remove call back
        """
        self.new_edge_call = call_back
        
    def complete_square(self, edge, regions):
        """ Report completed square
        :edge: - edge that completed the region
        :regions: - completed region(s)
        """
        SlTrace.lg("Completed region edge=%s" % (edge), "complete_square")
        if self.complete_square_call is not None:
            self.complete_square_call(edge, regions)


    def is_square_complete(self, edge, squares=None):
        """ Determine if this edge completes a square(s)
        :edge: - potential completing edge
        :squares: list, to which any completed squares(regions) are added
                Default: no regions are added
        :returns: True iff one or more squares are completed
        """
        return self.area.is_square_complete(edge, squares=squares)
        
        
    def new_edge(self, edge):
        """ Report new edge added
        :edge: - edge that completed the region
        """
        SlTrace.lg("SelectSquares.new_edge: edge=%s" % (edge), "new_edge")
        if self.new_edge_call is not None:
            self.new_edge_call(edge)

        
    def down_click(self, part, event=None):
        """ Process down click over highlighted part
        All highlighted parts elicit a call
        :part: highlighted part
        :event: event if available
        :Returns: True if processing is complete
        """
        if part.is_edge() and not part.is_turned_on():
            SlTrace.lg("turning on %s" % part, "turning_on")
            self.drawn_lines.append(part)
            part.turn_on()
            regions = part.get_adjacents()      # Look if we completed any squares
            for square in regions:
                if square.is_complete():
                    self.complete_square(part, square)
                    
            return True             # Indicate processing is done
    
        return False


    def stroke_call(self, part=None, x=None, y=None):
        """ Call back from sel_area.add_stroke_call
        """
        self.down_click(part)
        
            
    def display(self):
            self.area.display()
    
