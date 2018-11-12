# select_mover.py

from select_trace import SlTrace

class SelectMove(object):
    """ Movement information
    move types:
        MT_WHOLE - adjust whole part
        MT_INDEX - adjust part's index(end)
    """
    MT_WHOLE = 1
    MT_INDEX = 2
    move_id = 0              # Unique move id
    def __init__(self, part, delta_x=None, delta_y=None,
                 move_type=MT_WHOLE, indexes=None):
        """ Setup move instructions
        minus the offset which will be common
        """
        SelectMove.move_id += 1
        self.move_id = SelectMove.move_id
        self.part = part
        self.move_type = move_type
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.indexes = indexes


    def __str__(self):
        """ Provide reasonable view of move
        """
        return str(self.part) + " id=%d" % self.move_type 


class SelectMover(object):
    """ Controls moving of associated parts
    """
    
    def __init__(self, sel_area, delta_x=0, delta_y=0):
        self.sel_area = sel_area
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.moves = []         # List of PartMoves
        self.moves_by_id = {}   # Dictionary by id to allow quick checking


    def add_moves(self, parts, move_type=SelectMove.MT_WHOLE,
                  delta_x=None, delta_y=None, indexes=None):
        """ Add part moves to list (moves) to be subsequently executed by
        move_list
        Ignores repeated adding of same part
        :parts: part or list of parts
        :move_type: type of move Default:MT_WHOLE - move whole part
        :delta_x: - x increment for all parts to move
        :delta_y: - y increment for all parts to move
        :indexes: node indexes, default: all
        """
        if not isinstance(parts, list):
            parts = [parts]     # Make list of one
        
        if indexes is None:
            move_type = SelectMove.MT_WHOLE
        else:
            move_type = SelectMove.MT_INDEX
            if not isinstance(indexes, list):
                indexes= [indexes]      # Make list of one
                
        for part in parts:
            if not self.is_moved(part):
                move = SelectMove(part, move_type=move_type,
                                  delta_x=delta_x, delta_y=delta_y,
                                  indexes=indexes)
                self.add_move(move)


    def add_move(self, move):
        """ Add move and all subsequent moves forced by this move
        :move: part move to be added
        """
        if self.is_moved(move.part):
            return                      # Already moved

        move.mover = self               # refer to mover        
        self.moves.append(move)
        part = move.part
        self.moves_by_id[part.id] = move
        if move.move_type == SelectMove.MT_WHOLE:
            self.add_adjusts(part)          # Adjust all connected parts

        
    def add_corner_adjusts(self, corner, edges=None):
        """ Add in edge adjustments to edges attached to corner
        For each of the connecteds:
            Adjust the adjacent end
            if the movement is perpendicular to the connected
                adjust the connected's connecteds  by that perpendicular ammount
        """
        if edges is None:
            edges = corner.connecteds
        for edge in edges:            # Our end corners
            if edge.is_region():
                continue                # Ignore connected regions
            self.add_edge_adjust(corner, edge)    # Adjust those connected to our connected


    def add_adjusts(self, parts):
        """ Add in adjustments to parts attached to these
        For each of the connecteds:
            if connected not already addressed:
                adjust the connected
                add_adjusts for each of its connecteds
        :parts: one or list of parts to be adjusted
        """
        if not isinstance(parts, list):
            parts = [parts]             # list of one
        for part in parts:            # Our end corners
            for connected in part.connecteds:
                if connected.is_region():
                    continue            # regions are based on other components
                if self.is_moved(connected):
                    continue            # already addressed
                self.add_adjust(part, connected)     # adjust this connected part

    
    def add_adjust(self, base_part, part):
        """ Add move to adjust given part
        :base_part: Part causing adjustment
        :part: Part to be adjusted base on delta_x, delta_y and rules for adjusting
                this part type
        """
        if base_part.is_region():
            return                      # Region never causes adjustments
        if part.is_region():
            return                      # Region is never adjusted
        
        if part.is_corner():
            self.add_moves(part)        # Corner is always moved
            return
        
        self.add_edge_adjust(base_part, part)
        
        

    def add_edge_adjust(self, corner, corner_edge):
        """ Add adjustment to connected's end adjacent to part
        """
        corner_edge_dx, corner_edge_dy = corner_edge.edge_dxy()
        if ((self.delta_x != 0 and corner_edge_dy != 0)
            or (self.delta_y != 0 and corner_edge_dx != 0)):
            self.add_moves(corner_edge)     # Move whole edge
            self.add_moves(corner_edge.connecteds)          # Most already done
        else:
            ci, coi = corner.get_connected_loc_indexes(corner_edge)    # Adjust just connected end
            self.add_moves(corner_edge, indexes=ci)


    def is_moved(self, part):
        """ Determine if part has already been placed in current move list
        """
        if part.id in self.moves_by_id:
            return True
        
        return False
    
    
        
    def move_list(self, delta_x=None, delta_y=None):
        """ Adjust parts to complete connected move
            Adjust affected regions after parts moved
        """
        if delta_x is not None:
            self.delta_x = delta_x
        if delta_y is not None:
            self.delta_y = delta_y
            
        for move in self.moves:
            self.sel_area.record_move(move)
            part = move.part
            self.display_clear(part)
            move_type = move.move_type
            if move.delta_x is not None:
                delta_x = move.delta_x
            else:
                delta_x = self.delta_x
            if move.delta_y is not None:
                delta_y = move.delta_y
            else:
                delta_y = self.delta_y
            if move_type == SelectMove.MT_INDEX:
                self.adjust_part(part, delta_x, delta_y, indexes=move.indexes)
            elif move_type == SelectMove.MT_WHOLE:
                self.adjust_part(part, delta_x, delta_y)
            self.display_set(part)

        """ Adjust affected regions:
            Assume they are only the regions connected to the moved parts
        """
        region_d = {}
        for move in self.moves:
            connecteds = move.part.connecteds
            for part in connecteds:
                if part.is_region():
                    region_d[part.id] = part  # Adjust only once
        for region_id in region_d:
            region = region_d[region_id]
            region.display()
            
            
    def adjust_part(self, part, delta_x, delta_y, indexes=None):
        """ Adjust/Move part
        :part: - part to adjust/move
        :delta_x: - x change
        :delta_y: - y change
        :indexes: - index to adjust, None == all indexes
        """
        part.loc.move_nodes(delta_x, delta_y, nodes=indexes)


    def display_set(self, part=None):
        self.sel_area.display_set(part=part)


    def display_clear(self, handle):
        """ Clear display of this handle
        """
        self.sel_area.display_clear(handle)


class SelectMoveDisplay():
    """ Move annotation support
    Adds move annotations to their associated parts in the display
    """
    
    def __init__(self, sel_area, show_moved=False):
        """ Setup move display
        """
        self.sel_area = sel_area
        self.show_moved = show_moved
        self.record_move_list = []      # Recorded move list
        
        
    def record_move(self, move):
        """ Record move for display or subsequent action
        :move: SelectMove to be recorded
        """
        self.record_move_list.append(move)



    def record_move_display(self):
        """ Add move recording
        """
        if not SlTrace.trace("moveplan"):
            return
        for move in self.record_move_list:
            move_n = move.move_id - self.record_move_list[0].move_id + 1
            part = move.part
            if hasattr(part, 'move_tag') and part.move_tag is not None:
                self.sel_area.canvas.delete(part.move_tag)
                part.move_tag = None
            dir_x, dir_y = part.edge_dxy()
            chr_w = 8
            chr_h = chr_w*2
            disp_str = str(move_n)
            if part.is_edge():
                if dir_x != 0:      # sideways
                    if move.move_type == SelectMove.MT_INDEX:
                        if move.indexes[0] == 0:
                            disp_str = "> " + disp_str
                        else:
                            disp_str = disp_str + " <"                    
                    offset_x = -len(disp_str)*chr_w/4
                    offset_y = chr_h
                if dir_y != 0:      # up/down
                    if move.move_type == SelectMove.MT_INDEX:
                        if move.indexes[0] == 0:
                            disp_str = "v " + disp_str
                        else:
                            disp_str = disp_str + " ^"                    
                    offset_x = chr_w*2
                    offset_y = 0    
            else:
                offset_x = 1.2*chr_w
                offset_y = .7*chr_h
            c1x, c1y, c3x, c3y = part.get_rect()
            cx = (c1x+c3x)/2 + offset_x
            cy = (c1y+c3y)/2 + offset_y
            part.move_tag = self.sel_area.display_text((cx, cy), text=disp_str)
            SlTrace.lg("move: %d  %s (%d,%d) %s  dir_x=%d  dir_y=%d"
                       % (move_n, part.part_type, cx,cy, disp_str, dir_x, dir_y))
            
            
    def record_move_setup(self):
        if len(self.record_move_list) > 0:        
            if self.show_moved:
                for move in self.record_move_list:
                    if hasattr(move, 'tag') and move.tag is not None:
                        self.sel_area.canvas.delete(move.tag)     # delete move tag
                        move.tag = None
            self.record_move_list = []
