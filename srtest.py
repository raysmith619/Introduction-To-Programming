"""
Created on September 18, 2018

@author: raysm
"""
from cmath import rect
import os
import sys
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
from select_arrange import SelectArrange
from docutils.nodes import row

def pgm_exit():
    SlTrace.lg("Properties File: %s"% SlTrace.getPropPath())
    SlTrace.lg("Log File: %s"% SlTrace.getLogPath())
    sys.exit(0)

color_prog = "random"   # random, ascend, descend
color_drop_red = False
color_drop_green = False
color_drop_blue = False

nx = 5              # Number of x divisions
ny = nx             # Number of y divisions
show_id = False     # Display component id numbers
show_moved = True   # Display component id numbers
width = 600         # Window width
height = width      # Window height


base_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
SlTrace.setLogName(base_name)
SlTrace.lg("%s %s\n" % (os.path.basename(sys.argv[0]), " ".join(sys.argv[1:])))
###SlTrace.setTraceFlag("get_next_val", 1)
SlTrace.setTraceFlag("arrange_step", 1)
""" Flags for setup """
app = None                  # Application window ref
frame = None
###canvas = None
        
mw = Tk()
app = SelectWindow(mw,
                title="SelectWindow Testing",
                pgmExit=pgm_exit,
                )        
sar = None                                  # select arrangement control
arc = app.arrange_control()                 # Start up control, currently required

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

parser.add_argument('--color_prog', dest='color_prog', default=color_prog)
parser.add_argument('--color_drop_red', type=bool, dest='color_drop_red', default=color_drop_red)
parser.add_argument('--ew_display', type=int, dest='ew_display', default=ew_display)
parser.add_argument('--ew_select', type=int, dest='ew_select', default=ew_select)
parser.add_argument('--ew_standoff', type=int, dest='ew_standoff', default=ew_standoff)
parser.add_argument('--color_drop_green', type=bool, dest='color_drop_green', default=color_drop_green)
parser.add_argument('--color_drop_blue', type=bool, dest='color_drop_blue', default=color_drop_blue)
parser.add_argument('--nx=', type=int, dest='nx', default=nx)
parser.add_argument('--ny=', type=int, dest='ny', default=ny)
parser.add_argument('--show_id', type=bool, dest='show_id', default=show_id)
parser.add_argument('--show_moved', type=bool, dest='show_moved', default=show_moved)
parser.add_argument('--width=', type=int, dest='width', default=width)
parser.add_argument('--height=', type=int, dest='height', default=height)
args = parser.parse_args()             # or die "Illegal options"
SlTrace.lg("args: %s\n" % args)

color_prog = args.color_prog
color_drop_red = args.color_drop_red
color_drop_green = args.color_drop_green
color_drop_blue = args.color_drop_blue
nx = args.nx
ny = args.ny
nsq = nx * ny
show_id = args.show_id
show_moved = args.show_moved
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

def one_run():
    """ One run loop with a call back
    """
    global n_arrange
    if run_running:
        step_button()
    if run_running:
        n_arrange = app.get_current_val("arrange_number", 3)
        if n_arrange > 0:
            time_step = app.get_current_val("arrange_time", 10)
        else:
            time_step = app.get_current_val("time_step", 100)
        mw.after(time_step, one_run)        # Call us after time_step        

def run_button():
    global run_running
    SlTrace.lg("srtest Run Button")
    run_running = True
    one_run()


def set_figure_button():
    global frame, sr, figure_new, sar
    global width, height, nx, ny
    global n_rearrange_cycles, rearrange_cycle
    SlTrace.lg("srtest Set Button", "button")
    ###    if canvas is not None:
    ###        SlTrace.lg("delete canvas")
    ###        canvas.delete()
    ###        canvas = None
    if frame is not None:
        SlTrace.lg("destroy frame", "destroy frame")
        frame.destroy()
        frame = None
    
    app.update_form()
    n_rearrange_cycles = app.get_current_val("arrange_number", 1)
    rearrange_cycle = 1    
    width = app.get_current_val("window_width", width)
    width = int(width)
    height = app.get_current_val("window_height", height)
    height = int(height)
    nx = app.get_current_val("figure_columns", nx)
    if nx == 0:
        new_nx = 1
        SlTrace.lg("nx:%d is too low - set to %d" % (nx, new_nx), "adjust_size")
        nx = new_nx
    ny = app.get_current_val("figure_rows", ny)
    if ny == 0:
        new_ny = 1
        SlTrace.lg("ny:%d is too low - set to %d" % (ny, new_ny), "adjust_size")
        ny = new_ny
        
        
        
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
    def rn(val):
        return int(round(val))
                   
    for i in range(int(nx)):
        col = i+1
        x1 = xmin + i*xlen
        x2 = x1 + xlen
        for j in range(int(ny)):
            row = j+1
            y1 = ymin + j*ylen
            y2 = y1 + ylen
            rect = ((rn(x1), rn(y1)), (rn(x2), rn(y2)))
            rects.append(rect)
            rects_rows.append(row)
            rects_cols.append(col)
    
    im = Image.new("RGB", (width, height))
    frame = Frame(mw, width=width, height=height, bg="", colormap="new")
    frame.pack()
    canvas = Canvas(frame, width=width, height=height)
    canvas.pack()   
    sr = SelectArea(canvas, im)
    color_spec = app.get_current_val("color_spec", default= "freq")
    color_prog = app.get_current_val("color_prog", default="ascend")
    color_min = None        # Use internal defaults
    color_max = None
    ###if color_spec == "freq":
    ###    color_min = app.get_component_val("color_value", "min", default=400)
    ###    color_max = app.get_component_val("color_value", "max", default=700)
        
    reg_cc = SelectColor(ncolor=len(rects),
                         spec=color_spec,
                         prog=color_prog,
                         cmin=color_min,
                         cmax=color_max)

    SlTrace.lg("ncolor=%d" % len(rects), "get_color")
    SelectRegion.reset()
    for i, rect in enumerate(rects):
        row = rects_rows[i]
        col = rects_cols[i]
        col_rect = reg_cc.get_color()
        sr.add_rect(rect, color=col_rect, row=row, col=col)

    sr.display()        
    app.set_call("run", run_button)
    app.set_call("set", set_figure_button)
    app.set_call("pause", pause_button)
    app.set_call("step", step_button)
    app.set_call("step_down", step_down_button)
    if SlTrace.trace("step_button"):
        SlTrace.lg("color_spec: %s color_prog: %s color_min: %d color_max: %d")
    sar = SelectArrange(arc, sr, n_major_cycle = n_arrange, mw=mw)        # Setup for color rearrangement
    figure_new = False
    
    
def pause_button():
    global run_running
    SlTrace.lg("srtest Pause Button")
    run_running = False

def vs(val):
    if type(val) == str:
        return val
    
    return str(val)


def next_app_vals(step_dir = 1):
    """ Update app values to next value - should move to ctl 
    """
    nx = app.get_current_val("figure_columns", 1)
    ny = app.get_current_val("figure_rows", 1)
    nsq = nx * ny
    if nsq <= 0:
        nsq = 2
    for ctl_name in ["window_width", "window_height",
                 "figure_columns", "figure_rows",
                    "figure_size",
                 "color_prog", "color_spec",
                 "arrange_arranged", "arrange_extent",
                    "arrange_propagate", "arrange_restore",
                    "arrange_modify", "arrange_time",
                    "arrange_number",           
                 "time_step"]:
        if ctl_name == "figure_columns" or ctl_name == "figure_rows":
            nx = app.get_current_val("figure_columns", 1)
            ny = app.get_current_val("figure_rows", 1)
            nsq = nx * ny
            if nsq <= 0:
                nsq = 2
        app.get_component_next_val(ctl_name, inc_dir=step_dir)


def figure_step(step_dir=1):
        next_app_vals()
        set_figure_button()



def arrange_step(step_dir=1):
    """ Do one arrange step, first calling figure_step if appropriate
    :step_dir: 1 step up, -1 step back
    """
    global sar, figure_new
    global n_rearrange_cycles, rearrange_cycle
    if figure_new:
        sar = SelectArrange(arc, sr, n_major_cycle = n_arrange, mw=mw)
        figure_new = False
    if not sar.step(step_dir=1):
        rearrange_cycle += 1
        SlTrace.lg("arrange_step rearrange_cycle=%d of %d"
                    % (rearrange_cycle, n_rearrange_cycles), "arrange_step")
        if rearrange_cycle > n_rearrange_cycles:
            SlTrace.lg("end arrange_step rearrange_cycle=%d of %d"
                        % (rearrange_cycle, n_rearrange_cycles), "arrange_step")
            figure_step(step_dir=step_dir)
        next_app_vals(step_dir)
        sar.reset()             # Start a new cycle on existing figure

        
def step_button(step_dir = 1):
    SlTrace.lg("srtest Step Button", "step_button")
    arc.log_ctl_vals(trace="log_ctl_vals")
    arrange_step(step_dir=step_dir)


def step_down_button():
    SlTrace.lg("srtest Step Down Button", "set_button")
    step_button(step_dir=-1)
    
    
set_figure_button()                    # Start with an implied "set"


sr.display()
mainloop()