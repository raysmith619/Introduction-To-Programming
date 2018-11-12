"""
Created on Aug 23, 2018

@author: raysm
"""
import math
from cmath import rect
from select_trace import SlTrace
    
from select_error import SelectError
from select_part import SelectPart, PartHighlight
from select_corner import SelectCorner
from select_edge import SelectEdge
from select_region import SelectRegion
from select_mover import SelectMover, SelectMove, SelectMoveDisplay
from PIL.ImageChops import offset
"""
General domain issue
"""
        
        
                    
                     
class SelectArea(object):
    """
    Selected region of image
    Candidate for selection.
    """
    

    def __init__(self, canvas, image, rects=None,
                 show_moved=False, show_id=False):
        """
        Rectangular selected/ing region,
        :canvas: Canvas containing the region
        :image: displayed in frame
        :rects: single, or list of Rectangles (upper left x,y), (lower right x,y)
                each being a region
                Default is no rectangles
        """
        self.parts = []          # Parts of scene, corners, edges, regions
        self.parts_by_id = {}    # By part id
        """ hash/dictionary of parts by type, location
            type: edge, corner, region
            loc: (pt), (x,y)
                 (pt1 (upper right), pt2 (lower right)
        """
        self.parts_by_loc = {}      # By type, location: 
                                
        self.show_id = show_id
        self.show_moved = show_moved
        self.record_md = SelectMoveDisplay(self, show_moved=show_moved)
        self.canvas = canvas
        self.is_enclosed = False
        self.inside = False
        self.is_down = False
        self.highlights = {}            # Highlighted handles object REFERENCE
        self.selects = {}               # Select objects(handle)  REFERENCE
        self.motion_xy = None
        self.regions = []               # list of regions
        
        if rects is not None:
            if not isinstance(rects, list):
                rects = [rects]         # list of one
            for rect in rects:
                self.add_rect(rect)
            
            
        self.canvas.bind ("<ButtonPress-1>", self.down)
        self.canvas.bind ("<ButtonRelease-1>", self.up)
        self.canvas.bind ( "<Enter>", self.enter)
        self.canvas.bind ("<Leave>", self.leave)


    def add_rect(self, rect, color=None, row=None, col=None):
        """ Add rectangle to object as another region
        """                
        rec_ps = [None] * 4
        ulX, ulY = rect[0][0], rect[0][1]
        lrX, lrY = rect[1][0], rect[1][1]
        sr = SelectRegion(self, rect=[(ulX,ulY),(lrX,lrY)],
                        color=color, row=row, col=col)
        self.regions.append(sr)         # Add region
        self.add_part(sr)       
        rec_ps[0] = (ulX, ulY)
        rec_ps[1] = (lrX, ulY) 
        rec_ps[2] = (lrX, lrY)
        rec_ps[3] = (ulX, lrY)
        for pi1 in range(0, 3+1):
            pi2 = pi1 + 1
            if pi2 >= len(rec_ps):
                pi2 = 0          # Ends at first
            pt1 = rec_ps[pi1]
            pt2 = rec_ps[pi2]
            self.add_edge(sr, pt1, pt2)

    def add_edge(self, region, pt1, pt2):
        """ Add edge handles to region
        Also adds corner handles
        """
        edge = self.get_edge_with(pt1, pt2)
        if edge is None:
            edge = SelectEdge(self, rect=[pt1,pt2])
            self.add_part(edge)
        self.add_corners(region, [pt1, pt2], edge=edge)     # So we get corners
        region.add_connected(edge)
        edge.add_connected(region)      # Connect region to edge
        
    def add_corners(self, region, points, edge=None):
        """ Add corners to region
        :region: region to which to add corners
        :points: one or more corner locations
        If corner == first corner, set region enclosed
        but DON't add corner
        """
        if not isinstance(points, list):
            points = [points]     # Treat as an array of one
        for point in points:
            if self.is_first_corner(point):
                self.is_enclosed = True
            if self.has_corner(point):
                corner = self.get_corner_part(point[0], point[1])
            else:
                corner = SelectCorner(self, point=point)
            self.add_part(corner)       # Add new corners
            corner.add_connected(region)
                    
            region.add_connected(corner)
            if edge is not None:
                corner.add_connected(edge)      # Connect edge to corner
                edge.add_connected(corner)      # Connect corner to edge
                    
    def has_corner(self, point):
        """ Check if corner already present in region
        """
        for corner in self.parts:
            if not corner.is_corner():
                continue
            loc = corner.loc
            pt = loc.coord
            if pt[0] == point[0] and pt[1] == point[1]:
                return True     # Corner already present
        return False            # No such corner present
    
    
    def is_first_corner(self, point):
        """ Determine if this is the first point (equal to)
        """
        corner1 = None          # Set if found
        for part in self.parts:
            if part.is_corner():
                corner1 = part 
                break
        if corner1 is None:
            return False        # No corners to be had
        
        cpt = corner1.loc.coord
        if cpt[0] == point[0] and cpt[1] == point[1]:
            return True
        
        return False


    def get_color(self, row, col):
        """ Get color on square(region) at row, col
        :row: row in nx,ny
        :col: column in nx,ny
        :returns: current color None if none
        """
        square = self.get_square(row,col)
        if square is None:
            return None

        color = square.get_color()
        return color


    def color_set(self, color, row, col):
        """ Set color on square(region) at row, col
        :color: color to set square
        :row: row in nx,ny
        :col: column in nx,ny
        :returns: previous color None if none
        """
        square = self.get_square(row,col)
        if square is None:
            return None

        prev_color = square.set_color(color)
        square.display()
        return prev_color
        

    def current_edge(self, pt1, pt2):
        """ Return edge with these specifications, None if none found
        """
        return self.current_part("edge" )


    def current_part(self, part_type, pt1, pt2=None):
        """ Return part with this type, location, None if none found
        """
        loc_key = SelectPart.part_loc_key(part_type, pt1, pt2=None)
        if loc_key in self.parts_by_loc:
            return self.parts_by_loc[loc_key]   # current entry
        
        return None     # No entry at this location

    def display(self):
        for part in self.parts:
            self.display_set(part)


    def display_set(self, part=None):
        if part.is_corner():
            self.display_corner(part)
        elif part.is_edge():
            self.display_edge(part)
        elif part.is_region():
            part.display()
                    
            
    def display_corner(self, corner):
        """ Display corner on inside upper left corner
        """
        self.display_clear(corner)
        if self.is_highlighted(corner):
            """ Highlight given corner
            :hand: Corner handle
            :Returns: object tag for deletion
            """
            c1x,c1y,c3x,c3y = corner.get_rect(enlarge=True)
            corner.display_tag = self.canvas.create_rectangle(
                                c1x, c1y, c3x, c3y,
                                fill=SelectPart.corner_fill_highlight)
        else:
            loc = corner.loc 
            SlTrace.lg("corner: %s" % str(loc), "display")
            c1x,c1y,c3x,c3y = corner.get_rect()
            corner.display_tag = self.canvas.create_rectangle(
                        c1x, c1y, c3x, c3y, fill=SelectPart.corner_fill)
    
    
    def display_text(self, position, **kwargs):
        """ Add text to display, returning tag
        """
        tag = self.canvas.create_text(position, **kwargs)
        return tag
    
    
    def get_parts_at(self, x, y, sz_type=SelectPart.SZ_SELECT):
        """ Check if any part is at canvas location provided
        If found list of parts
        :Returns: SelectPart[]
        """
        parts = []
        for part in self.parts:
            if part.is_over(x,y, sz_type=sz_type):
                parts.append(part)
        if len(parts) > 1:
            SlTrace.lg("get_parts at (%d, %d) sz_type=%d" % (x,y, sz_type))
            for part in parts:
                c1x,c1y,c3x,c3y = part.get_rect(sz_type=sz_type)
                SlTrace.lg("    %s : c1x:%d, c1y:%d, c3x:%d, c3y:%d"
                       % (part, c1x,c1y,c3x,c3y))
            SlTrace.lg()
            olap_rect = SelectPart.get_olaps(parts, sz_type=SelectPart.SZ_SELECT)
            if olap_rect is not None:
                SlTrace.lg("Overlapping %d,%d, %d,%d"
                   % (olap_rect[0][0], olap_rect[0][1], olap_rect[1][0], olap_rect[1][1]))
                SlTrace.lg()
        return parts


    

    def get_corner_part(self, x, y):
        """ Returns corner SelectPart if at corner handle
        else None
        """
        for corner in self.parts:
            if not corner.is_corner():
                continue
            p1c1x,p1c1y,p1c3x,p1c3y = corner.get_rect(sz_type=SelectPart.SZ_SELECT)
            if p1c1x <= x and x <= p1c3x and p1c1y <= y and y <= p1c3y:
                return corner
            
        return None
    

    def get_edge_part(self, x, y):
        """ Returns edge object if at corner handle
        else None
        """
        for edge in self.parts:
            if not edge.is_edge():
                continue
            p1c1x,p1c1y,p1c3x,p1c3y = edge.get_rect()
            if p1c1x <= x and x <= p1c3x and p1c1y <= y and y <= p1c3y:
                return edge
            
        return None
    
    
    def get_edge_with(self, pt1, pt2):
        """ Get edge part with corners at pt1, pt2, if one
            :pt1:  end point uL or lR
            :pt2:  end point
            :Returns: edge or None
        """
        for part in self.parts:
            if not part.is_edge():
                continue
            points = part.get_points()
            if (SelectPart.is_point_equal(points[0], pt1)
                and SelectPart.is_point_equal(points[1], pt2)):
                return part
            if (SelectPart.is_point_equal(points[1], pt1)
                and SelectPart.is_point_equal(points[0], pt2)):
                return part

        return None
                    

    def get_region_part(self, x, y):
        """ Returns region object if at region handle
        else None
        """
        for region in self.parts:
            if not region.is_region():
                continue
            p1c1x,p1c1y,p1c3x,p1c3y = region.get_rect()
            if p1c1x <= x and x <= p1c3x and p1c1y <= y and y <= p1c3y:
                return region
            
        return None
        


    
    def get_square(self, row, col):
        """ return part for region at row, col
        :returns: part at row,col else None
        """
        
        """ Create dictionary only if we have to
        Maybe numpy would be better but we need to store parts, not numbers
        """
        if not hasattr(self, "parts_by_row_col") or self.parts_by_row_col is None:
            parts_by_row_col = {}
            for part in self.parts:
                if part.row != 0 and part.col != 0:
                    key = (part.row, part.col)
                    parts_by_row_col[key] = part
            self.parts_by_row_col = parts_by_row_col
        key = (row,col)
        
        if key not in self.parts_by_row_col:
            return None
        
        part = self.parts_by_row_col[key]
        
        return part
    
    
    def display_clear(self, handle):
        """ Clear display of this handle
        """
        if handle.display_tag is not None:
            self.canvas.delete(handle.display_tag)
            handle.display_tag = None
        if handle.highlight_tag is not None:
            self.canvas.delete(handle.highlight_tag)
            handle.highlight_tag = None

    
    def display_edge(self, edge):
        """ Display edge as a rectangle
        We leave room for the corners at each end
        Highlight if appropriate
        """
        
        loc = edge.loc
        rect = loc.coord
        SlTrace.lg("edge: %s" % str(loc), "display")
        if self.is_highlighted(edge):
            c1x,c1y,c3x,c3y = edge.get_rect(enlarge=True)
            edge.highlighted_tag = self.canvas.create_rectangle(
                                c1x, c1y, c3x, c3y,
                                fill=SelectPart.edge_fill_highlight)
        else:
            self.display_clear(edge)
            c1x, c1y, c3x, c3y = edge.get_rect()
            edge.display_tag = self.canvas.create_rectangle(
                                c1x, c1y, c3x, c3y,
                                fill=SelectPart.edge_fill)
        if self.show_id:
            dir_x, dir_y = edge.edge_dxy()
            chr_w = 5
            chr_h = chr_w*2
            if dir_x != 0:      # sideways
                offset_x = -len(str(edge.id))*chr_w/2 + chr_w
                offset_y = chr_h
            if dir_y != 0:      # up/down
                offset_x = len(str(edge.id))*chr_w
                offset_y = 0    
        
            cx = (c1x+c3x)/2 + offset_x
            cy = (c1y+c3y)/2 + offset_y
            edge.name_tag = self.display_text((cx, cy), text=str(edge.id))


    def down (self, event):
        self.is_down = True
        if self.inside:
            SlTrace.lg("Click in canvas event:%s" % event, "motion")
            cnv = event.widget
            x,y = cnv.canvasx(event.x), cnv.canvasy(event.y)
            SlTrace.lg("x=%d y=%d" % (x,y))
        if self.has_highlighted():
            for highlight in self.highlights.values():
                part = highlight.part
                self.select_set(part)
                if part.display_tag is None:
                    pt=str(part.part_type)
                    pdtag = str(part.display_tag)
                    SlTrace.lg("select %s tag=%s"
                           % (pt, pdtag,), "highlight")
                else:
                    SlTrace.lg("select %s tag=%s (%s)"
                           % (part.part_type, part.display_tag,
                              part), "highlight")
                    

    
    
    def motion (self, event):
        ###cnv.itemconfigure (tk.CURRENT, fill ="blue")
        cnv = event.widget
        x,y = float(cnv.canvasx(event.x)), float(cnv.canvasy(event.y))
        ###got = event.widget.coords (tk.CURRENT, x, y)
    
    def leave (self, event):
        SlTrace.lg("leave", "leave")
        self.inside = False
        if hasattr(self, 'motion_bind_id') and self.motion_bind_id is not None:
            self.canvas.unbind ("<Motion>", self.motion_bind_id)
            self.motion_bind_id = None
    
    def enter (self, event):
        SlTrace.lg("enter", "enter")
        self.inside = True
        self.motion_bind_id = self.canvas.bind("<Motion>", self.on_motion)


    def on_motion(self, event):
        cnv = event.widget
        x,y = cnv.canvasx(event.x), cnv.canvasy(event.y)
        prev_xy = self.motion_xy
        self.motion_xy = (x,y)
        if prev_xy is None:
            prev_xy = self.motion_xy
        if self.is_down:
            if self.has_selected():
                parts = self.get_selected_parts()
                self.record_move_setup()
                for part in parts:
                    xinc = x - prev_xy[0]
                    yinc = y - prev_xy[1]
                    SlTrace.lg("motion on(%s) at xy=(%d,%d) by xinc=%d yinc=%d"
                           % (part.part_type, x,y, xinc, yinc), "motion")
                    self.move_part(part, xinc, yinc)
                    self.highlight_set(part)
                self.record_move_display()
        parts = self.get_parts_at(x,y, sz_type=SelectPart.SZ_SELECT)        # NOTE: this is reference
        if len(parts) > 0:
            ncheck = 3
            if len(parts) > ncheck:
                SlTrace.lg("on parts(%d) > %d " % (len(parts), ncheck), "motion")
                for pa in parts:
                    SlTrace.lg("part: %s" % pa, "motion")
                SlTrace.lg("", "motion")
            self.highlight_clear()              # First clear all highlighted parts
            for part in parts:
                if not part.is_region():
                    SlTrace.lg("motion over %s" % part, "is_over")
                if SlTrace.trace("part_info"):
                    part.display_info()
                self.highlight_set(part, xy=(x,y))
        else:
            if self.has_highlighted():    
                self.highlight_clear()
            
            
    def highlight_set(self, part, xy=None):
        """ highlight specified part
        Save handle in highlight to allow easy access
        Clear previous highlight, if one
        
        """
        if part.is_corner():
            self.highlight_corner(part, xy=xy)
        elif  part.is_edge():
            self.highlight_edge(part, xy=xy)
        elif  part.is_region():
            ###self.highlight_region(part, xy=xy)
            part.highlight()
        else:
            return

    
    
    def get_highlighted(self):
        if not self.has_highlighted():
            return None
        
        highlighted = self.highlighted
        return highlighted


    
    
    def get_highlighted_part(self):
        highlighted = self.get_highlighted()
        if highlighted is None:
            return None
        
        return highlighted.part


    def has_highlighted(self):
        """ Determine if any highlighted parts
        """
        if bool(self.highlights):
            return True
        return False


    def is_highlighted(self, part):
        """ Check if part is highlighted
        """
        return part.is_highlighted()


    def is_highlighted_others(self, part):
        """ Check if non-overlapping parts are highlighted
        """
        if not self.has_highlighted():
            return False                # Nobody highlighted
        
        for highlight in self.highlights.values():
            if highlight.part.part_type != part.part_type:
                return True             # Another type is highlighted
            
            if not highlight.part.is_covering(part):
                return True
            
        return False


    def highlight_clear(self, parts=None, others=False):
        """ Clear highlighted parts
            Remove part form  highlights
            :parts:  parts to consider
            :others:   False - clear these parts
                        True - clear other parts
        """
        if not self.has_highlighted():
            return
        
        if parts is None:
            if not others:
                SlTrace.lg("highlight_clear ALL", "highlight")
            parts = []
            for highlight in self.highlights.values():
                parts.append(highlight.part)
        if not isinstance(parts, list):
            parts = [parts]
        
        if others:
            other_parts = []
            for highlight in self.highlights.values():
                found = False
                for part in parts: 
                    if highlight.part.is_same(part):
                        found = True
                        break
                if not found:
                    other_parts.append(part)
            parts = other_parts
                
        for part in parts:
            if part.id in self.highlights:
                highlight_tag = part.highlight_tag
                if highlight_tag is not None:
                    self.canvas.delete(highlight_tag)     # Remove highlight figure
                    part.highlight_tag = None
                part.highlighted = False
                if part.display_tag is None:
                    self.display_set(part)                # reestablish original display
                del self.highlights[part.id]
                SlTrace.lg("highlight_clear %d: %s" % (part.id, part), "highlight")

        
    
    def highlight_corner(self, corner, xy):
        """ Highlight given corner
        :handle: Corner handle
        :Returns: object tag for deletion
        """
        c1x,c1y,c3x,c3y = corner.get_rect(enlarge=True)
        tag = self.canvas.create_rectangle(
                            c1x, c1y, c3x, c3y,
                            fill=SelectPart.corner_fill_highlight)
        corner.highlight_tag = tag
        self.highlights[corner.id] = PartHighlight(corner, xy=xy)

    
    def highlight_edge(self, edge, xy):
        """ Highlight given edge
        :hand: Corner handle
        :Returns: object tag for deletion
        """
        c1x,c1y,c3x,c3y = edge.get_rect(enlarge=True)
        tag = self.canvas.create_rectangle(
                            c1x, c1y, c3x, c3y,
                            fill=SelectPart.edge_fill_highlight)
        edge.highlight_tag = tag
        self.highlights[edge.id] = PartHighlight(edge, xy=xy)

    
    def highlight_region(self, region, xy):
        """ Highlight region
        :region: Corner handle
        :Returns: object tag for deletion
        """
        c1x,c1y,c3x,c3y = region.get_rect(enlarge=True)
        tag = self.canvas.create_rectangle(
                            c1x, c1y, c3x, c3y,
                            fill=SelectPart.region_fill_highlight)
        region.highlight_tag = tag
        self.highlights[region.id] = PartHighlight(region, xy=xy)
        
        
    def select_set(self, part_id):
        """ Select handle
        """
        self.selects[part_id] = part_id
        
        
    def select_remove(self, selects):
        """ Remove one or more of selections
        :select: one or list of  selections to remove
                Default: all
        """
        if not isinstance(selects,list):
            selects = [selects]
        for id in list(self.selects):
            self.selects.pop(id)
    
    def get_selecteds(self):
        """ Return list of selected info or [] if none
        """
        return self.selects.values()
    
    
    def get_selected_parts(self):
        """ Returns all selected parts
        [] if non selected
        """
        parts = self.get_selecteds()
        return parts
    
    
    def has_selected(self):
        if bool(self.selects):
            return True
        return False
        

    def move_part(self, part, xinc, yinc):
        """ Move selected handle, adjusting connected parts
        """
        self.display_clear(part)      # Clear display before moveing
        if part.is_region():
            self.move_region(part, xinc, yinc)
        elif part.is_edge():
            self.move_edge(part, xinc, yinc)
        
        elif part.is_corner():
            self.move_corner(part, xinc, yinc)
        
        self.display_set(part)


    def move_edge(self, edge, xinc,  yinc, adjusts=None):
        
        
        """ Move selected edge, adjusting connected parts
        Direction of movement is constrained to perpendicular to edge
        Connected parts are:
            the corners at each edge end
            the end-points of the edges, not including this edge,
                connected to the end-corners
        :edge:  selected edge
        :xinc:  x destination delta
        :yinc:  y destination delta
        :adjusts: adjusted connections
                    Default: all connections
        :highlight: True - highlight after move
        """
        self.display_clear(edge)      # Clear display before moveing
        delta_x = xinc
        delta_y = yinc
        edge_dx, edge_dy = edge.edge_dxy()
        if edge_dx == 0:
            delta_y = 0     # No movement parallel to edge
        if edge_dy == 0:
            delta_x = 0     # No movement parallel to edge
        coord = edge.loc.coord
        p1, p2 = coord[0], coord[1]
        SlTrace.lg("move_edge: %s by delta_x=%d,delta_y=%d"
               % (edge, delta_x, delta_y), "move_part")
        """ Collect moves group:
            Collect all parts which need to be moved in whole or part.
            Each part is present once.  If an edge end is moved only the other edge's
            ends need to be adjusted
                 
        """
        mover = SelectMover(self, delta_x=delta_x, delta_y=delta_y)
        mover.add_moves(parts=edge)
        ###mover.add_moves(parts=edge.connecteds)
        ###mover.add_adjusts(edge.connecteds)      # Adjust those connected to corners and so on
        mover.move_list(delta_x, delta_y)

        
    def move_corner(self, corner, xinc,  yinc):
        """ Move selected corner, adjusting connected edges
        :corner: selected corner
        :xinc: x destination increment
        :yinc: y destination increment
        """
        delta_x = xinc
        delta_y = yinc
        SlTrace.lg("move: %s  by delta_x=%d,delta_y=%d"
               % (corner, delta_x, delta_y), "move_part")
        """ Split movements in to two directions to restrict propagation
        of affected parts
        """
        if delta_x != 0:
            mover = SelectMover(self, delta_x=delta_x)
            mover.add_moves(parts=corner)
            ###mover.add_moves(parts=edge.connecteds)
            ###mover.add_adjusts(edge.connecteds)      # Adjust those connected to corners and so on
            mover.move_list(delta_x, 0)
        if delta_y != 0:
            mover = SelectMover(self, delta_y=delta_y)
            mover.add_moves(parts=corner)
            ###mover.add_moves(parts=edge.connecteds)
            ###mover.add_adjusts(edge.connecteds)      # Adjust those connected to corners and so on
            mover.move_list(0, delta_y)


    def move_region(self, region, xinc,  yinc, adjusts=None):
        """ Move region
        Currently all parts
        Implement via move all corners
        """
        for part in region.connecteds:
            if part.is_corner():
                self.move_corner(part, xinc, yinc)
            
                 
    def adjust_corner_edge(self, corner, edge, delta_x, delta_y):
        """ Adjust edge's endpoint connected to this corner by the delta x,y
        """
        indexes = edge.get_connected_loc_indexes(corner)
        if indexes is None:
            raise(SelectError("adjust_corner_edge: corner(%s) not connected to edge(edge)"
                              % (corner, edge)))
        coord = edge.loc.coord
        coord.move_nodes(delta_x, delta_y, indexes[0])
        self.display_set(edge)

    def add_part(self, part):
        """ Add new part to list
        """
        if part.id in self.parts_by_id:
            return
        
        SlTrace.lg("add_part: %s" % part, "add_part")
        self.parts.append(part)
        self.parts_by_id[part.id] = part
        loc_key = part.loc_key()
        if loc_key in self.parts_by_loc:
            SlTrace.lg("add_part %s already present")
            return
        
        self.parts_by_loc[loc_key] = part
        
                            
    def up (self, event):
        self.is_down = False
        ###event.widget.itemconfigure (tk.CURRENT, fill =self.defaultcolor)
        cnv = event.widget
        x,y = cnv.canvasx(event.x), cnv.canvasy(event.y)
        ###got = event.widget.coords (tk.CURRENT, x, y)
        SlTrace.lg("up at x=%d y=%d" % (x,y), "motion")
        if self.has_selected():
            ids = list(self.selects)
            for sel_id in ids:
                self.select_remove(sel_id)
        
        
    def record_move(self, move):
        """ Record move for display or subsequent action
        :move: SelectMove to be recorded
        """
        self.record_md.record_move(move)
        
            
    def record_move_setup(self):
        """ Setup for move record display
        """
        self.record_md.record_move_setup()
        
        
    def record_move_display(self):
        self.record_md.record_move_display()
        
        
        
    
class SelBound(object):
    """
    Select boundary - part of Region
    """
    
    def __init__(self, region, rect, part_type='edge'):
        """
        Rectangular region, part of a selection region which can be used to modify
        the position/size of the region
        :region: region of which this  boundary is part
        :rect: Rectangle (upper left x,y), (lower right x,y)
        :part_type: Type region - determines range of movement, and effect
                    'corner' - free x,y adjusting adjacent legs
                    'edge' - movement perpendicular to edge, adjusting
                            placement of this edge and size of adjacent
                            edges
                    'region' - free x,y, adjusting position of whole
                            region, keeping dimensions fixed
        """
     
     
          
        
if __name__ == "__main__":
    import os
    import sys
    from tkinter import *    
    import argparse
    from PIL import Image, ImageDraw, ImageFont
    
    
    nx = 2          # Number of x divisions
    ny = 2          # Number of y divisions
    show_id = False  # Display component id numbers
    show_moved = True  # Display component id numbers
    width = 600     # Window width
    height = width  # Window height

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--nx=', type=int, dest='nx', default=nx)
    parser.add_argument('--ny=', type=int, dest='ny', default=ny)
    parser.add_argument('--show_id', type=bool, dest='show_id', default=show_id)
    parser.add_argument('--show_moved', type=bool, dest='show_moved', default=show_moved)
    parser.add_argument('--width=', type=int, dest='width', default=width)
    parser.add_argument('--height=', type=int, dest='height', default=height)
    args = parser.parse_args()             # or die "Illegal options"
    
    nx = args.nx
    ny = args.ny
    show_id = args.show_id
    show_moved = args.show_moved
    width = args.width
    height = args.height
    
    SlTrace.lg("%s %s\n" % (os.path.basename(sys.argv[0]), " ".join(sys.argv[1:])))
    SlTrace.lg("args: %s\n" % args)
    
    
    
    
    
    rect1 = ((width*.1, height*.1), (width*.5, height*.5))
    rect2 = ((width*.5, height*.5), (width*.9, height*.9))
    rects =  []
    ###rects.append(rect1)
    ###rects.append(rect2)
    xmin = .1*width
    xmax = .9*width
    xlen = (xmax-xmin)/nx
    ymin = .1*height
    ymax = .9*height
    ylen = (ymax-ymin)/ny
    for j in range(ny):
        y1 = ymin + j*ylen
        y2 = y1 + ylen
        for i in range(nx):
            x1 = xmin + i*xlen
            x2 = x1 + xlen
            rect = ((x1, y1), (x2, y2))
            rects.append(rect)
            
    im = Image.new("RGB", (width, height))
    frame = Frame(width=width, height=height, bg="", colormap="new")
    frame.pack()
    canvas = Canvas(frame, width=width, height=height)
    canvas.pack()   
    sr = SelectArea(canvas, im, rects=rects,
                      show_moved=show_moved, show_id=show_id)
    sr.display()
    mainloop()