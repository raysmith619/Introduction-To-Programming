"""
Created on Aug 23, 2018

@author: raysm
"""
import math
from cmath import rect
from docutils.nodes import Part
from platform import node

    
from select_error import SelectError
from select_part import SelectPart
from select_corner import SelectCorner
from select_edge import SelectEdge
from select_region import SelectRegion
from select_mover import SelectMover, SelectMove, SelectMoveDisplay
from PIL.ImageChops import offset
"""
General domain issue
"""

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
        
        
                    
                     
class SelectReg(object):
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


    def add_rect(self, rect):
        """ Add rectangle to object as another region
        """                
        rec_ps = [None] * 4
        ulX, ulY = rect[0][0], rect[0][1]
        lrX, lrY = rect[1][0], rect[1][1]
        sr = SelectRegion(rect=[(ulX,ulY),(lrX,lrY)])   # Just one region now
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
            edge = SelectEdge(rect=[pt1,pt2])
            self.add_part(edge)
        self.add_corners(region, [pt1, pt2], edge=edge)     # So we get corners
        region.add_connected(edge)

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
                corner = SelectCorner(point=point)
            self.add_part(corner)       # Add new corners
                
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


    def display(self):
        for part in self.parts:
            self.display_set(part)


    def display_set(self, part=None):
        if part.is_corner():
            self.display_corner(part)
        elif part.is_edge():
            self.display_edge(part)
                    
            
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
            print("corner: %s" % str(loc))
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
            print("get_parts at (%d, %d) sz_type=%d" % (x,y, sz_type))
            for part in parts:
                c1x,c1y,c3x,c3y = part.get_rect(sz_type=sz_type)
                print("    %s : c1x:%d, c1y:%d, c3x:%d, c3y:%d"
                       % (part, c1x,c1y,c3x,c3y))
            print()
            olap_rect = SelectPart.get_olaps(parts, sz_type=SelectPart.SZ_SELECT)
            if olap_rect is not None:
                print("Overlapping %d,%d, %d,%d"
                   % (olap_rect[0][0], olap_rect[0][1], olap_rect[1][0], olap_rect[1][1]))
                print()
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
        print("edge: %s" % str(loc))
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
            print("Click in canvas event:%s" % event)
            cnv = event.widget
            x,y = cnv.canvasx(event.x), cnv.canvasy(event.y)
            print("x=%d y=%d" % (x,y))
        if self.has_highlighted():
            for highlight in self.highlights.values():
                part = highlight.part
                self.select_set(part)
                print("select %s tag=%d (%s)"
                       % (part.part_type, part.display_tag,
                          part))

    
    
    def motion (self, event):
        ###cnv.itemconfigure (tk.CURRENT, fill ="blue")
        cnv = event.widget
        x,y = float(cnv.canvasx(event.x)), float(cnv.canvasy(event.y))
        ###got = event.widget.coords (tk.CURRENT, x, y)
    
    def leave (self, event):
        print("leave")
        self.inside = False
        if hasattr(self, 'motion_bind_id'):
            self.canvas.unbind ("<Motion>", self.motion_bind_id)

    
    def enter (self, event):
        print("enter")
        self.inside = True
        self.motion_bind_id = self.canvas.bind("<Motion>", self.on_motion)


    def on_motion(self, event):
        cnv = event.widget
        x,y = cnv.canvasx(event.x), cnv.canvasy(event.y)
        prev_xy = self.motion_xy
        self.motion_xy = (x,y)
        if prev_xy is None:
            prev_xy = self.motion_xy
        
        if self.has_selected():
            parts = self.get_selected_parts()
            self.record_move_setup()
            for part in parts:
                xinc = x - prev_xy[0]
                yinc = y - prev_xy[1]
                print("motion on(%s) at xy=(%d,%d) by xinc=%d yinc=%d"
                       % (part.part_type, x,y, xinc, yinc))
                self.move_part(part, xinc, yinc)
                self.highlight_set(part)
            self.record_move_display()
        parts = self.get_parts_at(x,y, sz_type=SelectPart.SZ_SELECT)        # NOTE: this is reference
        if len(parts) > 0:
            ncheck = 3
            if len(parts) > ncheck:
                print("on parts(%d) > %d " % (len(parts), ncheck))
                for pa in parts:
                    print("part: %s" % pa)
                print()
            self.highlight_clear()              # First clear all highlighted parts
            for part in parts:
                if not part.is_region():
                    print("motion over %s" % part)
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
            self.highlight_region(part, xy=xy)
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
                print("highlight_clear ALL")
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
                print("highlight_clear %d: %s" % (part.id, part))

        
    
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
        
        
    def select_set(self, part):
        """ Select handle
        """
        self.selects[part.id] = part
        
        
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
        print("move_edge: %s by delta_x=%d,delta_y=%d"
               % (edge, delta_x, delta_y))
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
        print("move_edge: %s  by delta_x=%d,delta_y=%d"
               % (corner, delta_x, delta_y))
        mover = SelectMover(self, delta_x=delta_x, delta_y=delta_y)
        mover.add_moves(parts=corner)
        ###mover.add_moves(parts=edge.connecteds)
        ###mover.add_adjusts(edge.connecteds)      # Adjust those connected to corners and so on
        mover.move_list(delta_x, delta_y)


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
        
        print("add_part: %s" % part)
        self.parts.append(part)
        self.parts_by_id[part.id] = part
        
        
                            
    def up (self, event):
        self.is_down = False
        ###event.widget.itemconfigure (tk.CURRENT, fill =self.defaultcolor)
        cnv = event.widget
        x,y = cnv.canvasx(event.x), cnv.canvasy(event.y)
        ###got = event.widget.coords (tk.CURRENT, x, y)
        print("up at x=%d y=%d" % (x,y))
        if self.has_selected():
            ids = list(self.selects)
            for id in ids:
                self.select_remove(self.parts[id])
        
        
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
    
    print("%s %s\n" % (os.path.basename(sys.argv[0]), " ".join(sys.argv[1:])))
    print("args: %s\n" % args)
    
    
    
    
    
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
    for i in range(nx):
        x1 = xmin + i*xlen
        x2 = x1 + xlen
        for j in range(ny):
            y1 = ymin + j*ylen
            y2 = y1 + ylen
            rect = ((x1, y1), (x2, y2))
            rects.append(rect)
            
    im = Image.new("RGB", (width, height))
    frame = Frame(width=width, height=height, bg="", colormap="new")
    frame.pack()
    canvas = Canvas(frame, width=width, height=height)
    canvas.pack()   
    sr = SelectReg(canvas, im, rects=rects,
                      show_moved=show_moved, show_id=show_id)
    sr.display()
    mainloop()