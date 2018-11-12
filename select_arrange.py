# select_arrange.py
"""
Control of color arrangement stepping through different schemes
"""
import random
from datetime import datetime
import time
import re
from tkinter import *    

from select_trace import SlTrace
from select_part import color_to_fill
from select_color import darken
from select_error import SelectError
    
class SavedColorRow:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col


class SelectArrange:
    
    def __init__(self, arrctl, figure, n_major_cycle, mw=None):
        """ Setup arrangement control
        :arrctl: arrange control (ArrangeControl)
        :figure: - display figure
        """
        self.arrctl = arrctl
        self.n_major_cycle = n_major_cycle
        self.figure = figure
        self.major_cycle = 0        # Number of times reset
        self.max_duration = None        
        if mw is None:
            mw = Tk()
        self.mw = mw
        """ Keep values that change figure structure
        before and outside reset
        """
        self.nx = self.arrctl.get_current_val("figure_columns", 3)
        if self.nx == 0:
            new_nx = 1
            SlTrace.lg("nx:%d is too low - set to %d" % (self.nx, new_nx), "adjust_size")
            self.nx = new_nx
        self.ny = self.arrctl.get_current_val("figure_rows", 3)
        if self.ny == 0:
            new_ny = 1
            SlTrace.lg("ny:%d is too low - set to %d" % (self.ny, new_ny), "adjust_size")
            self.ny = new_ny
        self.reset()
        
    def reset(self):
        """ Set/reset color arrangement to allow repeating cycles
        """
        self.major_cycle += 1
        self.propagate = self.arrctl.get_current_val("arrange_propagate", "grow")
        self.restore = self.arrctl.get_current_val("arrange_restore", "random")
        self.modify = self.arrctl.get_current_val("arrange_modify", "replace")
        self.number_cycle = self.arrctl.get_current_val("arrange_number", 1)
        self.arranged = self.arrctl.get_current_val("arrange_arranged", "square")
        nsq = self.nx * self.ny
        if self.arranged == "square":
            if nsq >= 81:
                self.arranged = "2x2"
            if nsq >= 144:
                self.arranged = "3x3"
            if nsq >= 225:
                self.arranged = "4x4"
            self.arrctl.set_current_val("arrange_arranged", self.arranged)
        elif self.arranged == "2x2":
            if nsq >= 144:
                self.arranged = "3x3"
            if nsq >= 225:
                self.arranged = "4x4"
            self.arrctl.set_current_val("arrange_arranged", self.arranged)

                
        SlTrace.lg("SelectArrange: nx=%d, ny=%d propagate=%s restore=%s modify=%s arranged=%s"
                   % (self.nx, self.ny, self.propagate, self.restore,
                      self.modify, self.arranged), "arrange_step")
        self.is_arranged_row_x_col = False
        if self.arranged == "square":
            self.row_extent = 1
            self.col_extent = 1
        elif self.arranged == "row":
            self.row_extent = 1
            self.col_extent = self.nx
        elif self.arranged == "column":
            self.row_extent = self.ny
            self.col_extent = 1
        elif "x" in self.arranged:
            m = re.match(r'^(\d+)x(\d+)$', self.arranged)
            if m is None:
                raise SelectError("Unrecognized arrangement %s" % self.arranged)
            self.is_arranged_row_x_col = True
            self.row_extent = int(m.group(1))
            self.col_extent = int(m.group(2))
        self.cycle = -1       # define to allow print without error
        self.sub_cycle = -1
        self.row_prev = self.row_next = self.row_cur = -1
        self.col_prev = self.col_next = self.col_cur = -1
        
        self.step_set()          # setup for stepping
        self.saved_square_groups = []           # square_groups saved for restoration/access
        self.highlighted_squares = None         # highlighted squares
                                                #  unhighlighted view
        
        
    def after_time(self, time_ms=None, call_rtn=None):
        if time_ms is None:
            time_ms = 100
        self.mw.after(time_ms, call_rtn)
            

    def color_change(self):
        """ Change colors based on scheme and row,col current and row,col next
        """
        if self.propagate == "ripple":
            pass
        elif self.propagate == "grow":
            pass
        elif self.propagate == "bubble":
            pass
        """ Implement grow """
        if SlTrace.trace("color_change"):
            nextfill = color_to_fill(self.color_begin)
            dest_square = self.get_square()
            SlTrace.lg("color_change: sqare_stepno:%d[%d] new=%s from=%s at row=%d col=%d"
                        % (self.sqare_stepno, self.sqare_stepno_end, nextfill, dest_square.get_fill(),
                            dest_square.row, dest_square.col ))
        to_color = self.color_begin     # default: replace
        self.modify_group()


    def modify_group(self):
        """ Modify current group's color etc based on self.modify,arranged
        Appropriately updates square_stepno by the number of squares arranged
        """
        group_squares = self.get_group_squares()    # Reduced to those within bounds
        if group_squares is None or len(group_squares) == 0:
            return
        
        to_color = self.get_next_color(group_squares)
        if self.modify == "switch":
            """ Because:
                1. squares probably change color, often propagating the same
                   color.
                2. often go in strings of the same or close to the same color
                3. we will use a color of a randomly selected square.
            """
            self.set_group_color(to_color, group_squares)
        elif self.modify == "darken":
            self.darken_group(group_squares)
        else:
            self.set_group_color(to_color, group_squares, save=False)
            
        self.square_stepno += len(group_squares)


    def darken_group(self, squares):
        """ Darken group of squares
        :squares: square(SaveColorRow) or list of squares to be darkened
        """
        if not isinstance(squares, list):
            squares = [squares]
        
        to_colors = []
        for sq in squares:
            to_color = darken(sq.color)
            to_colors.append(to_color)
        self.set_group_color(to_colors, squares, save=True)
        
        
    def set_group_color(self, to_colors, squares=None, save=True):
        """ Set group of squares to color(s)
            optionally, save square_group for restoration
        :to_colors: one or a list of colors one or list
                if number of to_colors is less than number of squares
                repeat to_colors
        :squares: one or a list of squares
        :save: save squares for restoration default: save
        TBD - complete
        """
        if to_colors is None:
            to_colors = self.color_begin
        if not isinstance(to_colors, list):
            to_colors = [to_colors]     # Make list of one
        if squares is None:
            squares = self.get_group_squares()
        if not isinstance(squares, list):
            squares = [squares]
        tci = 0
        for square in squares:
            self.set_square_color(to_colors[tci], square)
            tci += 1
            if tci >= len(to_colors):
                tci = 0         # Wrap around, reusing colors
        if save:
            self.save_square_group(squares)
        self.highlight_square_group(squares)


    def set_square_color(self, color, square):
        """ Set given square to color.  No recording for restoration is done here
        :color: color to set
        :square: square(SaveColorRow) color to set
        :returns: previous color
        """
        fig_square = self.get_square(row=square.row, col=square.col)
        fig_color = fig_square.get_color()
        prev_color = self.color_set(color, row=square.row, col=square.col)
        return prev_color
    
    
    def get_group_squares(self, row=None, col=None):
        """ Get group of squares starting with row,col
        Group depends on arranged, starting row, col, and
        boundaries (nx,ny)
        
        :row: beginning row number default: self.row_cur
        :col: beginning col number default: self.col_cur
        """
        
        if row is None:
            row = self.row_cur
        if col is None:
            col = self.col_cur
        nrow = self.ny                  # Reads better, allows modification
        ncol = self.nx
        """ calculate row_end, col_end given:
                1. type of arrangement(arranged)
                2. row_extent, col_extent
                3. figure size: rows(ny), cols(nx)
        """ 
           
        row_end = row + self.row_extent - 1
        if row_end > nrow:
            row_end = nrow
        if row > row_end:
            return []               # No room
        col_end = col + self.col_extent - 1
        if col_end > ncol:
            col_end = ncol
         
        squares = []
        for rn in range(row, row_end+1):
            for cn in range(col, col_end+1):
                fig_square = self.get_square(row=rn, col=cn)
                if fig_square is None:
                    SlTrace.lg("None at row=%d col=%d" % (rn, cn))
                    continue
                fig_color = fig_square.get_color()
                sq = SavedColorRow(fig_color, rn, cn)
                squares.append(sq)
        return squares
    
    
    def get_next_color(self, squares):
        """ Get best color for next group, based on some algorithm
        TBD - better algorithm - look for increased contrast
        """
        if squares is None:
            len_sc = len(self.saved_square_groups)
            if len_sc > 0:
                sc_index = random.randint(0, len_sc-1)
                squares = self.saved_square_groups[sc_index]
        sc = squares[0]
        to_color = sc.color
        return to_color


    def highlight_square_group(self, squares, keep=False):
        """ Highlight group of squares
        :squares: one square(savedColorRow) or list of squares
        :keep: True - keep previous highlighting, Default remove it
        """
        
        if not isinstance(squares, list):
            squares = [squares]     # list of one
        if not keep:
            self.unhighlight_square_group()
        self.highlighted_squares = squares
        for square in squares:
            fig_square = self.get_square(square)
            fig_square.highlight()
            
    def unhighlight_square_group(self, squares=None):
        """ Restore squares to previous view
        :squares: squares to unhighlight default: currently highlighted
        """
        if squares is None:
            squares = self.highlighted_squares
            self.highlighted_squares = None
        if squares is not None:
            for square in squares:
                fig_square = self.get_square(square)
                fig_square.unhighlight()
        
    def save_square_group(self, squares=None):
        """ Save group to be accessed/restored later
        :squares: one square(savedColorRow) or list of squares
                      comprising  of a group
                default: square at  row_cur, col_cur
        """
        
        if squares is None:
            squares = self.get_group_squares()
        self.saved_square_groups.append(squares)    
        
        
    def color_set(self, color=None, row=None, col=None):
        """ Set figure square
        :color: color to set, default= self.color_begin
        :row: row - default= self.row_cur
        :col: col - default= self.col_cur
        """
        
        if color is None:
            color = self.color_begin
        if row is None:
            row = self.row_cur
        if col is None:
            col = self.col_cur
        prev_color = self.figure.color_set(color=color, row=row, col=col)
        return prev_color

    def get_color(self, row=None, col=None):
        """ Get color of square
        :row: - default self.row_cur
        :col: - default self.col_cur
        """
        
        if row is None:
            row = self.row_cur
        if col is None:
            col = self.col_cur
        figure = self.figure
        color = figure.get_color(row=row, col=col)
        return color

    def get_fill(self, row=None, col=None):
        """ Get color of square 8x %06X fmt
        :row: - default self.row_cur
        :col: - default self.col_cur
        """
        if row is None:
            row = self.row_cur
        if col is None:
            col = self.col_cur
        part = self.get_square(row=row, col=col)
        if part is None:
            return "None"
        return part.get_fill()


    def get_square(self, square=None, row=None, col=None):
        """ Get figure square, either from square(SaveColorRow) or row,col
        """
        if square is not None:
            if row is not None or col is not None:
                raise SelectError("get_square: Mixing square and row/col parameters")
            row = square.row
            col = square.col
        else:
            if row is None:
                row = self.row_cur
            if col is None:
                col = self.col_cur
        return self.figure.get_square(row=row, col=col)
        
    def set_figure(self):
        """ Set up for figure arrangement run
        """
        pass
        
        
    def step(self, step_dir=1):
        """ Make one arrangement step, returning False if we are at end
        end of figure cycle
        :step_dir: direction of step 1(up) default
        """
        self.begin_time = datetime.now()
        if not self.step_next(step_dir=1):
            return False
        
        self.end_time = datetime.now()
        diff_time = self.end_time - self.begin_time
        self.time_duration = diff_time.total_seconds()
        if self.arrctl.sar_max_duration is None or self.time_duration > self.arrctl.sar_max_duration:
            if self.arrctl.sar_max_duration is not None:
                delta_dur = self.time_duration - self.arrctl.sar_max_duration
                SlTrace.lg("Arrange duration(sec): max=%s was=%s delta=%f"
                           % (self.time_duration, self.arrctl.sar_max_duration, delta_dur))
                if SlTrace.trace("arrange_time"):
                    SlTrace.lg("%d %s"
                                % (self.time_duration,
                                    self.arrctl.get_ctl_vals()))
            else:
                SlTrace.lg("First time diff", "arrange_time")
            self.arrctl.sar_max_duration = self.time_duration
        return True
            
            
    def step_next(self, step_dir=1):
        """ Adjust row, col square_stepno, colors for next step
        go through each cycle
        cycle 0 is setup
        cycle 1 through self.number_cycles are cycles through extent
        sub_cycle 1 is populate
        sub_cycle 2 is reset to initial layout
        :step_dir: direction through squares pos - up (default), neg - down
        :returns: True - still in cycle, False - cycle is complete
        """
        SlTrace.lg("step_next major_cycle=%d[%d] sub_cycle=%d[%d] %s"
                    % (self.major_cycle, self.n_major_cycle, self.sub_cycle, 2,
                       self.arranged)
                    
                + " square_stepno=%d[%d] row=%d[%d] col=%d[%d]"
                    %  (self.square_stepno, self.nx*self.ny,
                       self.row_cur, self.ny,
                       self.col_cur, self.nx),
                "arrange_step")
        if self.cycle == 0:
            self.row_begin = random.randint(1,self.ny)
            if self.row_begin + self.row_extent - 1 > self.ny:
                self.row_begin = self.ny - self.row_extent + 1
            self.row_cur = self.row_begin
            self.col_begin = random.randint(1,self.nx)          # Start so it fits
            if self.col_begin + self.col_extent - 1 > self.nx:
                self.col_begin = self.nx - self.col_extent + 1
            self.col_cur = self.col_begin
            self.row_next = self.row_cur        # Prepare for the next call
            self.col_next = self.col_cur
            self.color_begin = self.get_color()
            self.square_stepno_end = self.nx * self.ny # Only correct for extent == all
            self.sub_cycle = 0
            self.cycle = 1      # Setup next cycle
            self.new_cycle(self.cycle)
            SlTrace.lg("step_next: %s nx=%d ny=%d"
                        % (self.arranged, self.nx, self.ny), "arrange_step")
            return True     # No change from the beginning


        ###if self.cycle >  self.number_cycle:
        if self.cycle >  1:
            SlTrace.lg("end of cycles: %d > %d\n"
                        % (self.cycle, 1), "arrange_step")
            return False
        
        if self.sub_cycle == 0:
            self.new_cycle(self.cycle)
        elif self.sub_cycle > 2:
            self.cycle += 1
            self.sub_cycle = 0
            return True
        
                           
        if self.sub_cycle == 1:
            if self.square_stepno == 0:
                self.square_stepno = 1
            self.row_prev = self.row_cur    # remember previous
            self.col_prev = self.row_cur
            self.row_cur = self.row_next    # advance to next
            self.col_cur = self.col_next
            
            if not self.next_square_group(step_dir):     # update roe,col and color if appropriate
                self.sub_cycle = 2
                self.square_stepno = 0              # Flag for beginning of sub_cycle
                self.unhighlight_square_group()     # Remove last group marker
                return True
            
        elif self.sub_cycle == 2:       # color reset cycle
            if self.square_stepno == 0:
                self.square_stepno = 1
                self.saved_sqgrp_index = 0    # Setup
                if self.restore == "random":
                    random.shuffle(self.saved_square_groups)                # rearange randomly
                elif self.restore == "forward":
                    pass                # Do in order changed
                elif self.restore == "reverse":
                    self.saved_square_groups = list(
                            reversed(self.saved_square_groups))                # Do in reversed order
                SlTrace.lg("restore cycle restore=%s(%d)"
                           % (self.restore, len(self.saved_square_groups)), "arrange_step")

            if self.saved_sqgrp_index >= len(self.saved_square_groups):
                SlTrace.lg("end restore cycle", "arrange_step")
                self.sub_cycle += 1
                self.unhighlight_square_group()     # Remove last group marker
                return True
                
            scg = self.saved_square_groups[self.saved_sqgrp_index]
            self.saved_sqgrp_index += 1
            self.restore_color(scg)
        else:
            if self.sub_cycle > 2:
                self.cycle += 1
                self.sub_cycle = 0    
        return True


    def new_cycle(self, cycle):
        """ Setup fore new cycle
        :cycle: cycle number for info
        """
        self.sub_cycle = 1
        self.square_stepno = 0      # setup flag


    def restore_color(self, squares):
        """ Restore square(SavedColorRow) or list of squares
        :squares: one or list of SavedColorRow.
        """
        self.unhighlight_square_group() 
        if not isinstance(squares, list):
            squares = [squares]
        for square in squares:
            fig_square = self.get_square(row=square.row, col=square.col)
            if SlTrace.trace("color_change"):
                nextfill = color_to_fill(square.color)
                SlTrace.lg("restore_saved_colors: square_stepno:%d[%d] new=%s from=%s at row=%d col=%d"
                            % (self.square_stepno, self.square_stepno_end, nextfill, fig_square.get_fill(),
                                fig_square.row, fig_square.col ))
            self.figure.color_set(color=square.color, row=square.row, col=square.col)
        self.highlight_square_group(squares)
                
    def next_square_group(self, step_dir):
        """ Update row_next, col_next,  and color region for next arrangement step
        Note that currently all arranged are located by row,col of upper left
        square of the arranged
        """
        if self.square_stepno > self.square_stepno_end:
            self.unhighlight_square_group()     # Remove last group marker
            return False
        
        if "horiz" in self.propagate:
            self.step_horizontal(step_dir=step_dir)
        elif "diag" in self.propagate:
            self.step_horizontalstep_dir=step_dir()
            self.step_vertical(step_dir=step_dir)    
        else:       # vertical
            self.step_vertical(step_dir=step_dir)
                                            
        self.color_change()        
        return True                     # Still in cycle


    def step_horizontal(self, step_dir):
        """ adjust row, col for horizontal step
        """
        self.row_next += step_dir*self.row_extent
        if self.row_next > self.ny:
            self.row_next = 1            # Wrap around
            self.col_next += self.col_extent
            if self.col_next > self.nx:
                self.col_next = 1
        elif self.row_next < 0:           # Wrap around
            self.row_next = self.ny
            self.col_next -= step_dir*self.col_extent
            if self.col_next < 0:
                self.col_next = self.nx-self.col_extent+1


    def step_vertical(self, step_dir):
        """ adjust row, col for horizontal step
        """
        self.col_next += step_dir*self.col_extent
        if self.col_next > self.nx:
            self.col_next = 1            # Wrap around
            self.row_next += self.row_extent
            if self.row_next > self.ny:
                self.row_next = 1           # Wrap around
                self.col_next += step_dir*self.col_extent
                if self.col_next > self.ny:
                    self.col_next = 1
        if self.col_next > self.nx:
            self.col_next = 1            # Wrap around
            self.row_next += self.row_extent
            if self.row_next > self.ny:
                self.row_next = 1           # Wrap around
                self.col_next += step_dir*self.col_extent
                if self.col_next > self.ny:
                    self.col_next = 1
    
    def step_set(self, square_stepno=0):
        """ Setup for stepping
        :square_stepno: step number, 0 == startup
        """
        self.saved_color_row_col_groups = []  
        self.square_stepno = square_stepno
        self.cycle = 0
        
            