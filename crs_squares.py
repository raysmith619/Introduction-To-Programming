"""
Created on October 30, 2018

@author: Charles Raymond Smith
"""
from cmath import rect
import os
import sys
import time
from tkinter import *    
import argparse
from PIL import Image, ImageDraw, ImageFont
from select_area import SelectArea
from select_part import SelectPart
from select_window import SelectWindow
from select_color import SelectColor
from select_trace import SlTrace
from arrange_control import ArrangeControl
from select_region import SelectRegion
from select_squares import SelectSquares
from select_arrange import SelectArrange
from docutils.nodes import row

def pgm_exit():
    SlTrace.lg("Properties File: %s"% SlTrace.getPropPath())
    SlTrace.lg("Log File: %s"% SlTrace.getLogPath())
    sys.exit(0)


nx = 5              # Number of x divisions
ny = nx             # Number of y divisions
show_id = False     # Display component id numbers
width = 600         # Window width
height = width      # Window height


base_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
SlTrace.setLogName(base_name)
SlTrace.lg("%s %s\n" % (os.path.basename(sys.argv[0]), " ".join(sys.argv[1:])))
###SlTrace.setTraceFlag("get_next_val", 1)
""" Flags for setup """
app = None                  # Application window ref
frame = None
###canvas = None
        
mw = Tk()
app = SelectWindow(mw,
                title="crs_squares Testing",
                pgmExit=pgm_exit,
                arrange_selection=False
                )        
btmove = 1.         #  Seconds between moves
ew_display = 3
ew_select = 5
ew_standoff = 5

width = app.get_current_val("window_width", width)
width = int(width)
height = app.get_current_val("window_height", height)
height = int(height)
nx = app.get_current_val("figure_columns", nx)
ny = app.get_current_val("figure_rows", ny)

parser = argparse.ArgumentParser()

parser.add_argument('--btmove', type=float, dest='btmove', default=btmove)
parser.add_argument('--ew_display', type=int, dest='ew_display', default=ew_display)
parser.add_argument('--ew_select', type=int, dest='ew_select', default=ew_select)
parser.add_argument('--ew_standoff', type=int, dest='ew_standoff', default=ew_standoff)
parser.add_argument('--nx=', type=int, dest='nx', default=nx)
parser.add_argument('--ny=', type=int, dest='ny', default=ny)
parser.add_argument('--show_id', type=bool, dest='show_id', default=show_id)
parser.add_argument('--width=', type=int, dest='width', default=width)
parser.add_argument('--height=', type=int, dest='height', default=height)
args = parser.parse_args()             # or die "Illegal options"
SlTrace.lg("args: %s\n" % args)

btmove = args.btmove
nx = args.nx
ny = args.ny
nsq = nx * ny
show_id = args.show_id
width = args.width
height = args.height
ew_display= args.ew_display
ew_select = args.ew_select
ew_standoff = args.ew_standoff

SelectPart.set_edge_width_cls(ew_display,
                          ew_select,
                          ew_standoff)

run_running = False
figure_new = True           # True - time to setup new figure
                            # for possible arrangement
n_arrange = 1               #number of major cycle for rearrange
sqs = None

sp = None
players = None

        
    
class SelectPlayer:
    def __init__(self, name=None, letter=None, color=None):
        self.name = name
        if letter is None:
            letter = name[0].upper()
        self.letter = letter
        if color is None:
            color = "black"
        self.color = color
        

class SelectPlay:
    def __init__(self, board=None,
                 btmove=btmove, players=None, move_first=None):
        self.board = board
        self.btmove = btmove
        self.players = players
        self.player_index = 0
        self.msg = None
        if move_first is None:
            self.player_index = 0
        else:
            self.player_index = move_first-1
        self.move_no = 0
        self.first_time = True       # flag showing first time
        self.moves = []
        board.add_new_edge_call(self.new_edge)


    def annotate_squares(self, squares, player=None):
        """ Annotate squares in board with players info
        :squares: list of squares to annotate
        :player: player whos info is used
                Default: use current player
        """
        if player is None:
            player = self.get_player()
        for square in squares:
            square.add_centered_text(player.letter, color=player.color)


    def announce_player(self):
        """ Announce current player
        """
        player = self.get_player()
        text = "It's %s's turn." % player.name
        SlTrace.lg(text)
        self.do_message(text=text, color=player.color)


    def do_message(self, text, color=None, font_size=40, time_sec=None):
        """ Put message up. If time is present bring it down after time seconds    
        :time: time for message
                default: leave message there till next message
        """
        if self.msg is not None:
            self.msg.destroy()
            self.msg = None
        self.msg = Message(mw, text=text)
        self.msg.config(fg=color, bg='white',
                        font=('times', font_size, 'italic'))
        self.msg.pack()
        if time_sec is not None and False:
            SlTrace.lg("Leaving message up for %.1f seconds" % time_sec)
            time.sleep(time_sec)
            self.msg.destroy()
            self.msg = None    
            
            
    def do_first_time(self):
        self.announce_player()


    def is_square_complete(self, edge, squares=None):
        """ Determine if this edge completes a square(s)
        :edge: - potential completing edge
        :squares: list, to which any completed squares(regions) are added
                Default: no regions are added
        :returns: True iff one or more squares are completed
        """
        return self.board.is_square_complete(edge, squares=squares)


    def new_edge(self, edge):
        SlTrace.lg("New edge %s" % edge, "new_edge")
        if self.first_time:
            self.first_time = False
        else:
            self.move_no += 1
        regions = []
        if self.is_square_complete(edge, regions):
            self.completed_square(edge, regions)
        else:
            self.get_next_player()      # Advance to next player
        self.announce_player()

    def get_next_player(self):
        """ Get next player to move
        """
        self.player_index += 1
        if self.player_index >= len(self.players):
            self.player_index = 0
        return self.get_player()

    
    def get_player(self):
        """ Get current player to move
        """
        player = self.players[self.player_index]
        return player
        
    
    def completed_square(self, edge, squares):
        player = self.get_player()
        player_name = player.name
        player_letter = player.letter
        if len(squares) == 1:
            text = ("%s completed a square with letter %s"
                     % (player_name, player_letter))
        else:
            text = ("%s completed %d squares with letter %s"
                    % (player_name, len(squares), player_letter))
        SlTrace.lg(text)
        self.annotate_squares(squares, player=player)    
        self.do_message(text, font_size=20, time_sec=2)
        text = ("%s gets another turn." % player_name)
        SlTrace.lg(text)
        self.do_message(text, font_size=20, time_sec=1)



def set_squares_button():
    global frame, sqs
    global width, height, nx, ny
    global n_rearrange_cycles, rearrange_cycle
    global players, sp
    
    SlTrace.lg("Squares Set Button", "button")
    ###    if canvas is not None:
    ###        SlTrace.lg("delete canvas")
    ###        canvas.delete()
    ###        canvas = None
    if frame is not None:
        SlTrace.lg("destroy frame", "destroy frame")
        frame.destroy()
        frame = None
    
    app.update_form()
        
        
        
    rects =  []
    rects_rows = []         # So we can pass row, col
    rects_cols = []
    min_xlen = app.get_component_val("figure_size", "min", 10)
    min_xlen = float(min_xlen)
    min_xlen = str(min_xlen)
    min_ylen = min_xlen
    
    ###rects.append(rect1)
    ###rects.append(rect2)
    xmin = .1*float(width)
    xmax = .9*float(width)
    xlen = (xmax-xmin)/float(nx)
    min_xlen = float(min_xlen)
    if xlen < min_xlen:
        SlTrace.lg("xlen(%.0f) set to %.0f" % (xlen, min_xlen))
        xlen = min_xlen
    ymin = .1*float(height)
    ymax = .9*float(height)
    ylen = (ymax-ymin)/float(ny)
    min_ylen = float(min_ylen)
    if ylen < min_ylen:
        SlTrace.lg("ylen(%.0f) set to %.0f" % (ylen, min_ylen))
        ylen = min_ylen
    frame = Frame(mw, width=width, height=height, bg="", colormap="new")
    frame.pack()
    canvas = Canvas(frame, width=width, height=height)
    canvas.pack()
            
    players = []
    players.append(SelectPlayer("Alex", letter="Ax", color="pink"))
    players.append(SelectPlayer("Declan", color="blue"))
    ###players.append(SelectPlayer("Avery", letter="Av", color="pink"))
    if sp is not None and sp.msg is not None:
        sp.msg.destroy()
        sp.msg = None
    sqs = SelectSquares(canvas, nrows=ny, ncols=nx, width=width, height=height)
    sp = SelectPlay(board=sqs, players=players, move_first=1)
       
    sqs.display()        
    sp.do_first_time()

def vs(val):
    if type(val) == str:
        return val
    
    return str(val)

def new_edge(edge):
    """ Top level processing of new edge (line
    :edge: added edge
    """
    SlTrace.lg("We have added an edge (%s)" % (edge), "new_edge")
    sp.new_edge(edge)

def new_game():
    """ Start new game
    """
    SlTrace.lg("Starting New Game")
    set_squares_button()



def change_players():
    """ View/Change players
    """
    SlTrace.lg("Control Players - not yet installed")
    
    
app.add_menu_command("NewGame", new_game)
app.add_menu_command("Players", change_players)
set_squares_button()

mainloop()