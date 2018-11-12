# arrange_control.py 25Sep2018

from tkinter import *
import random
from select_error import SelectError
from select_trace import SlTrace
from builtins import str
from select_dd_choice import SelectDDChoice
from _ast import Str
"""
Arrangement control window layout
            ___  min____ max___ inc___ end (loop) reverse
window
    width
    height

figure
    rows
    columns

time
    steps
    run


[run] [pause] [step] by___
[RESET] [STOP]
"""

class ControlEntry:
    
    def __init__(self, name, ctl_widget=None,
                 value = None,
                 unknown_type=False,
                 default_value=None,
                 value_type=int,
                 width=4):
        """ Setup control Entry for later access
        """
        self.name = name
        self.unknown_type = unknown_type
        self.value_type = value_type
        self.ctl_widget = ctl_widget
        if self.unknown_type:
            self.value = value
            if default_value is None:
                default_value = value
            self.default_value = default_value
        else:
            if default_value is not None:
                if isinstance(default_value, str) and self.value_type is not str:
                    default_value = self.str_to_value(default_value)
            elif value is not None:
                default_value = value
            self.default_value = default_value
            if value is None:
                value = default_value
    
            if value is not None:
                if isinstance(value, str):
                    value = self.str_to_value(value)
            self.value = value
        self.width = width
        
        
        
    def str_to_value(self, string):
        """ Convert string on entry to internal value based on type
            "" for non-string data evaluates to None
        :str: external string type
        :returns: string converted to control's data type
        """
        if string is None:
            return string
        
        if self.value_type is int:
            if string == "":
                return None
            
            return int(string)
        
        elif self.value_type is float:
            if string == "":
                return None
            
            return float(string)
        
        elif self.value_type is str:
            return string
        else:
            SlTrace.lg("str_to_value: Unrecognized value_type:", "valueck")        
        return string
    
    
    def to_value(self, val):
        """ Convert val on entry to internal value based on type
            "" for non-string data evaluates to None
        :val: default value, if none use local value
        :returns: data type
        """
        if val is None:
            return self.value
        

        if self.value_type is None:
            self.value_type = type(val)
        if isinstance(val, str):
            return self.str_to_value(val)
        
        if self.value_type is int:
            return int(val)
        
        if self.value_type is float:
            return float(val)

        if self.value_type is str:
            return str(val)

        raise SelectError("str_to_value: Unrecognized value_type:")


    def get_input(self):
        """ Get input from widget
            None if no widget
            Sets control's value
            :returns: input value
        """
        if self.ctl_widget is None:
            return None
        
        field_str = self.ctl_widget.get()
        self.value = self.str_to_value(field_str)
        return self.value


    
class ArrangeControl(Toplevel):
    CONTROL_NAME_PREFIX = "controlName"
    
    def __init__(self, ctlbase, title=None, change_call=None):
        """ Display / Control of figure
        :ctlbase: base control object
        :change_call: if present,called when control changes
        """
        self.control_d = {}      # name : (name, ctl_widget, default_value)
        self.call_d = {}        # Call by name
        self.ctl_lists = {}     # Control selection lists [current_index, selection_list]
        ###Toplevel.__init__(self, parent)
        self.ctlbase = ctlbase
        self.sar_max_duration = None        # Track arrange color duration
        """ Setup control names found in properties file
        Updated as new control entries are added
        """
        prop_keys = SlTrace.getPropKeys()
        pattern = ArrangeControl.CONTROL_NAME_PREFIX + r"\.(.*)"
        rpat = re.compile(pattern)
        name_d = {}
        ### TBD I need to think about what is going on here
        for prop_key in prop_keys:
            rmatch = re.match(rpat, prop_key)
            if rmatch:
                name = rmatch[1]
                prop_val = SlTrace.getProperty(prop_key)
                name_d[name] = prop_val
        self.ctl_name_d = name_d
        
        
        if title is None:
            title = "Arrange"
        self.change_control = change_call
        win_width =  500
        win_height = 700
        win_x0 = 100
        win_y0 = 100
                    
        self.mw = Toplevel()
        win_setting = "%dx%d+%d+%d" % (win_width, win_height, win_x0, win_y0)

        
        self.mw.geometry(win_setting)
        self.mw.title(title)
        top_frame = Frame(self.mw)
        self.mw.protocol("WM_DELETE_WINDOW", self.delete_window)
        top_frame.pack(side="top", fill="both", expand=True)
        self.top_frame = top_frame
        
        controls_frame = Frame(top_frame)
        controls_frame.pack(side="top", fill="both", expand=True)
        self.controls_frame = controls_frame
 
        """
        Window Setup
        """
        win_label = Label(master=controls_frame, text="Window", anchor='w')
        win_label.pack(side="top", fill="both", expand=True)
        self.add_change_ctl(master=controls_frame, ctl_name="window_width", text="width", value=win_width)
        self.add_change_ctl(master=controls_frame, ctl_name="window_height", text="height", value=win_height)
        ###self.add_change_ctl(master=controls_frame, ctl_name="window_x0", text="x0", value=win_width*.1)
        ###self.add_change_ctl(master=controls_frame, ctl_name="window_y0", text="y0", value=win_height*.1)

        """
        Figure Setup
        """
        Label(master=controls_frame, text="")
        win_label.pack(side="top", fill="both", expand=True) 
        win_label = Label(master=controls_frame, text="Figure", anchor='w')
        win_label.pack(side="top", fill="both", expand=True)
        self.add_change_ctl(master=controls_frame, ctl_name="figure_columns", text="columns", value=6)
        self.add_change_ctl(master=controls_frame, ctl_name="figure_rows", text="rows", value=5)
        self.add_change_ctl(master=controls_frame, ctl_name="figure_size", text="size",
                             value=50, min_value=20, max_value=200)

        """
        Color Selections
        """
        Label(master=controls_frame, text="")
        win_label.pack(side="top", fill="both", expand=True) 
        win_label = Label(master=controls_frame, text="Colors", anchor='w')
        win_label.pack(side="top", fill="both", expand=True)
        selection_list = self.set_list(ctl_name="color_spec",
                selection_list = ["frequency", "rgb", "bw", "rgb1prim", "rgb2prim"])
        self.add_color_ctl(master=controls_frame, ctl_name="color_spec", text="specification",
                           selection=selection_list,
                           selection_default= "rgb")
        selection_list = self.set_list(ctl_name="color_prog",
                selection_list = ["random", "ascend", "descend"])
        self.add_color_ctl(master=controls_frame, ctl_name="color_prog", text="progression",
                           selection=selection_list,
                           selection_default= "random")
        self.add_color_ctl(master=controls_frame, ctl_name="color_value", text="value")


        """
        Rearrangement Selections
        """
        Label(master=controls_frame, text="")
        win_label.pack(side="top", fill="both", expand=True) 
        win_label = Label(master=controls_frame, text="Rearrange", anchor='w')
        win_label.pack(side="top", fill="both", expand=True)
        arrange_arranged_list = self.set_list(ctl_name="arrange_arranged",
                selection_list = ["square", "2x2", "3x3", "4x4", "row", "column"])
        self.add_color_ctl(master=controls_frame, ctl_name="arrange_arranged", text="arranged",
                           selection=arrange_arranged_list,
                           selection_default= "square")
        arrange_extent_list = self.set_list(ctl_name="arrange_extent",
                selection_list = ["row", "column", "all"])
        self.add_color_ctl(master=controls_frame, ctl_name="arrange_extent", text="extent",
                           selection=arrange_extent_list,
                           selection_default= "all")
        arrange_propagate_list = self.set_list(ctl_name="arrange_propagate",
                selection_list = ["ripple", "grow", "bubble",
                        "ripple_horiz", "grow_horiz", "bubble_horiz"])
        self.add_color_ctl(master=controls_frame, ctl_name="arrange_propagate",
                           text="propagate",
                           selection=arrange_propagate_list,
                           selection_default= "grow")
        arrange_restore_list = self.set_list(ctl_name="arrange_restore",
                selection_list = ["random", "forward", "reverse"])
        self.add_color_ctl(master=controls_frame, ctl_name="arrange_restore",
                           text="restore",
                           selection=arrange_restore_list,
                           selection_default= "random")
        arrange_modify_list = self.set_list(ctl_name="arrange_modify",
                selection_list = ["replace", "switch", "darken"])
        self.add_color_ctl(master=controls_frame, ctl_name="arrange_modify",
                           text="modify",
                           selection=arrange_modify_list,
                           selection_default= "replace")
        self.add_change_ctl(master=controls_frame, ctl_name="arrange_time", text="time",
                             value=1000, min_value=1000, max_value=1000)
        self.add_change_ctl(master=controls_frame, ctl_name="arrange_number", text="number",
                             value=1, min_value=1, max_value=1)


 
        """
        Major Time Step
        """ 
        Label(master=controls_frame, text="")
        win_label.pack(side="top", fill="both", expand=True) 
        win_label = Label(master=controls_frame, text="Time(msec)", anchor='w')
        win_label.pack(side="top", fill="both", expand=True)
        self.add_change_ctl(master=controls_frame, ctl_name="time_step", text="step",
                            value=1000, min_value=1000, max_value=1000)
       
 
        run_pause_frame = Frame(top_frame)
        run_pause_frame.pack(side="top", fill="both", expand=True)
        self.run_pause_frame = run_pause_frame
        
        set_button = Button(master=run_pause_frame, text="Set", command=self.set)
        set_button.pack(side="left", expand=True)
        run_button = Button(master=run_pause_frame, text="Run", command=self.run)
        run_button.pack(side="left", expand=True)
        pause_button = Button(master=run_pause_frame, text="Pause", command=self.pause)
        pause_button.pack(side="left", expand=True)
        step_button = Button(master=run_pause_frame, text="Step", command=self.step)
        step_button.pack(side="left", expand=True)
        step_button = Button(master=run_pause_frame, text="StepDown", command=self.step_down)
        step_button.pack(side="left", expand=True)
        SlTrace.lg("End of TraceControl __init__")


    def add_change_ctl(self, master=None, ctl_name=None, text=None, value=None,
                       width=5, min_value=None, max_value=None):
        """ Add change control to data base and to frame
        :master: master frame into which we place the controls
        :ctl_name: unique name for this control in the data base
                    prefix for sub components
        :text:   text for control section
        :width: with of input field
        :value:  Optional value to set / display for current value
        :min_value: Optional min value, default is value
        :max_value: Optional max value, default is value
        """
        ctl_frame = Frame(master=master)
        ctl_frame.pack(side="top", fill="both", expand=True)
        Label(master=ctl_frame, text="    ", anchor='w').pack(side="left")
        ctl_label = Label(master=ctl_frame, text=text, anchor='w')
        ctl_label.pack(side="left", fill="both", expand=False)
        if min_value is None:
            min_value = value
        if max_value is None:
            max_value = value
        self.add_change_component(ctl_frame, base=ctl_name, name="current",
                                  width=width, value=value, text="")
        sp = Label(ctl_frame, text="    ", anchor="w")
        sp.pack(side="left")
        if value is not None and not isinstance(value,str):      # Don't include min,max if type str
            self.add_change_component(ctl_frame, base=ctl_name, name="min",
                                      width=width, value=min_value)
            self.add_change_component(ctl_frame, base=ctl_name, name="max",
                                      width=width, value=max_value)
        self.add_change_component(ctl_frame, base=ctl_name, name="next",
                                    selection=["same", "random", "ascend", "descend"],
                                    selection_default="random")
        self.add_change_component(ctl_frame, base=ctl_name, name="end",
                                    selection=["same", "reverse", "wrap", "random"],
                                    selection_default="reverse")


    def add_color_ctl(self, master=None, ctl_name=None, text=None, value=None,
                      selection=None, selection_default=None):
        """ Setup color control
        :master: master frame into which we place the controls
        :ctl_name: unique name for this control in the data base
                    prefix for sub components
        :text:   text for control section
        :value:  Optional value to set / display for current value
        :selection: - list of selection values
        :selection_default: - value of selection default
        """
        ctl_frame = Frame(master=master)
        ctl_frame.pack(side="top", fill="both", expand=True)
        Label(master=ctl_frame, text="    ", anchor='w').pack(side="left")
        ctl_label = Label(master=ctl_frame, text=text, anchor='w')
        ctl_label.pack(side="left", fill="both", expand=False)
        if selection is not None:
            self.add_change_component(ctl_frame, base=ctl_name, name="current",
                                    text="",
                                    selection=selection,
                                    selection_default=selection_default)
        else:
            self.add_change_component(ctl_frame, base=ctl_name, name="current",
                                    text="")
            
        if value is not None and not isinstance(value,str):      # Don't include min,max if type str
            self.add_change_component(ctl_frame, base=ctl_name, name="min")
            self.add_change_component(ctl_frame, base=ctl_name, name="max")
        self.add_change_component(ctl_frame, base=ctl_name, name="next",
                                            selection=["same", "random", "ascend", "descend"],
                                            selection_default="same")
        self.add_change_component(ctl_frame, base=ctl_name, name="end",
                                            selection=["reverse", "wrap", "random"],
                                            selection_default="reverse")


    def add_rearrange_ctl(self, master=None, ctl_name=None, text=None, value=None,
                      selection=None, selection_default=None):
        """ Setup rearrange control
        This is the rearrangement of existing squares/parts in the preesisting setup.
        These operations should be less computaionally expensive and therefore faster
        than the recreation of the whole figure.
        
        :master: master frame into which we place the controls
        :ctl_name: unique name for this control in the data base
                    prefix for sub components
        :text:   text for control section
        :value:  Optional value to set / display for current value
        :selection: - list of selection values
        :selection_default: - value of selection default
        """
        ctl_frame = Frame(master=master)
        ctl_frame.pack(side="top", fill="both", expand=True)
        Label(master=ctl_frame, text="    ", anchor='w').pack(side="left")
        ctl_label = Label(master=ctl_frame, text=text, anchor='w')
        ctl_label.pack(side="left", fill="both", expand=False)
        if selection is not None:
            self.add_change_component(ctl_frame, base=ctl_name, name="current",
                                    text="",
                                    selection=selection,
                                    selection_default=selection_default)
        else:
            self.add_change_component(ctl_frame, base=ctl_name, name="current",
                                    text="")
            
        self.add_change_component(ctl_frame, base=ctl_name, name="min")
        self.add_change_component(ctl_frame, base=ctl_name, name="max")
        self.add_change_component(ctl_frame, base=ctl_name, name="next",
                                            selection=["same", "random", "ascend", "descend"],
                                            selection_default="same")
        self.add_change_component(ctl_frame, base=ctl_name, name="end",
                                            selection=["reverse", "wrap", "random"],
                                            selection_default="reverse")
        

    def add_change_component(self, ctl_frame,
                             base=None, name=None,
                             text=None, typectl=Entry,
                             selection=None,
                             selection_default=None,
                             value=None,
                             value_type=None,
                             width=4):
        """ Add change control component
        :ctl_frame: frame in to which we add this component
        :base: base name e.g. "window"
        :name: component name e.g. "width"
        :selection: If present, array of selection strings
        :selection_default: selection default, None -> first
        :text: displayed text None - use name
                "" - no text label
        :typectl: Control widget type, default: Entry
        :value:  initial value (default), if not already present
        :value_type: Value type default: int
        :width: Field width in characters
        """
        if text is None:
            text = name
        
        if value is not None and value_type is None:
            value_type = type(value)
            
        if text != "":
            label_entry = Label(ctl_frame, text= "  "+text, anchor="w")
            label_entry.pack(side="left")
        ctl_name = base + "_" + name
        if SlTrace.trace("add_change"):
            SlTrace.lg("add_change_component %s %s" % (ctl_name, text))
        if selection is not None:
            selection_default =  self.get_prop_value(ctl_name, selection_default)
            val_entry = SelectDDChoice(ctl_frame,
                                     selection=selection,
                                     default=selection_default)
            value_type = str
            self.update_control_entry(ctl_name, ctl_widget=val_entry,
                                    value=value,
                                    value_type=value_type,
                                    width=width)

        else:
            if ctl_name in self.ctl_name_d:
                ctn = self.ctl_name_d[ctl_name]
                if isinstance(ctn, ControlEntry):
                    ctl_value = ctn.value  # Get entry value
                elif isinstance(ctn, str):
                    ctl_value = ctn           # Use properties value
                else:
                    ctl_value = value
                value = ctl_value    
            val_entry = Entry(ctl_frame, width=width)
            self.update_control_entry(ctl_name, ctl_widget=val_entry,
                                                value=value,
                                                value_type=value_type,
                                                width=width)
        val_entry.pack(side="left")
        self.show_entry(ctl_name)

    
    def show_entry(self, name):
        """ Display entry value in form
        :name: control name
        """
        ctl_entry = self.get_ctl_entry(name)
        if ctl_entry is None:
            return
        
        value = ctl_entry.value
        if value is not None:
            self.set_entry_field(name, value)     # Done after entry is created

       
    def delete_window(self):
        """ Process Trace Control window close
        """
        if self.mw is not None:
            self.mw.destroy()
            self.mw = None
        
        if self.ctlbase is not None and hasattr(self.ctlbase, 'arc_destroy'):
            self.tcbase.tc_destroy()


    def get_ctl_default(self, value_type):
        """
        Get control value from properties
        :value_type: - value data type None - int
        :returns: value, null if none
        """
        if value_type is None:
            value_type  = int
        if self.ctl_name_d is None:
            prop_keys = SlTrace.getPropKeys()
            pattern = ArrangeControl.CONTROL_NAME_PREFIX + r"\.(.*)"
            rpat = re.compile(pattern)
            name_d = {}
            ### TBD I need to think about what is going on here
            for prop_key in prop_keys:
                rmatch = re.match(rpat, prop_key)
                if rmatch:
                    name = rmatch[1]
                    prop_val = SlTrace.getProperty(prop_key)
                    name_d[name] = prop_val
            self.ctl_name_d = name_d
        try:
            value_str = self.ctl_name_d[name_d]
        except:
            return None
            
        if value_type is str:
            return value_str
        
        if value_str == "":
            return None
        
        if value_type is int:
            return int(value_str)
        
        if value_type is float:
            return float(value_str)
        
        return value_str     

    
    def set_call(self, name, function):
        """ Set for call back
        """
        self.call_d[name] = function
        
        
                
    def set_control_value(self, name, val,
                          unknown_type = False,
                          change_cb=True):
        """ Set trace level, changing Control button if requested
        An entry is created if none exists
        :name: - control name
        :val: - value to set
        :unknoqn_type: True - don't check / convert type
        :change_cb: True(default) appropriately change the control
        """
        ctl_entry = self.get_ctl_entry(name)
        if ctl_entry is None:
            self.control_d[name] = ControlEntry(name, value=val,
                                                unknown_type=unknown_type,
                                                default_value=val)
            ctl_entry = self.get_ctl_entry(name)
            
        if ctl_entry.ctl_widget is not None and change_cb:
            self.set_entry_field(name, val)


    
    def set_entry_field(self, name, val):
        """ Set control widget field value
        """
        ctl_entry = self.get_ctl_entry(name)
        if ctl_entry is None:
            return
        
        ctl_widget = ctl_entry.ctl_widget
        if ctl_widget is None:
            return
        
        if isinstance(ctl_widget, Entry):
            ctl_widget.delete(0,END)
            ctl_widget.insert(0,str(val))
        elif isinstance(ctl_widget, SelectDDChoice):
            ctl_widget.set_field(val)    

    def update_control_entry(self, ctl_name,
                            ctl_widget=None,
                            default_value=None,
                            value=None,
                            value_type=None,
                            width=None):
        """ Update / create control entry
        :ctl_name: full control name
        :ctl_widget: control widget, if one
        :default_value: default value
        :value_type: data type
        :width: entry value field width, in characters
        """
        if ctl_name not in self.control_d:
            self.control_d[ctl_name] = ControlEntry(ctl_name,
                                                    ctl_widget=ctl_widget,
                                                    value=value,
                                                    default_value=default_value,
                                                    value_type=value_type,
                                                    width=width)
            self.ctl_name_d[ctl_name] = self.control_d[ctl_name]
        else:
            ctl_entry = self.control_d[ctl_name]
            if ctl_widget is not None:
                ctl_entry.ctl_widget = ctl_widget    
            if value is not None:
                ctl_entry.value = value    
            if default_value is not None:
                ctl_entry.default_value = default_value    
            if value_type is not None:
                ctl_entry.value_type = value_type    
            if width is not None:
                ctl_entry.width = width    



    def get_ctl_names(self):
        """ Get sorted list of control names
            This is a union of control_d and those in the properties file
            
        """
        names = sorted(self.control_d.keys())
        return names

    def get_ctl_vals(self, con="=", sep=" "):
        """ get the list of name=val of all control names
        :con: connector between name and value
        :sep: is separator default = space
        """
        ret_str = ""
        for name in self.get_ctl_names():
            if name.endswith("_current"):
                if ret_str != "":
                    ret_str += sep
                val = self.get_component_val(name, default="NONE")
                ret_str += name + con + str(val)
        return ret_str


    def log_ctl_vals(self, con="=", sep=" ", trace=None):
        """ Log current control values
        See get_ctl_vals
        """
        if SlTrace.trace(trace):    # ck for trace before doing call
            SlTrace.lg(self.get_ctl_vals(con=con, sep=sep))
        

    def get_component_val(self, name, comp_name=None, default=None):
        """ Get component value of named control
        If widget is present, get from widget
        else if control is present, get from control
        else if properties is present, get from properties
        :name: - control name
        :comp_name: if present, append with "_" comp_name
        :default: - use if value not found - MANDATORY
                    data type is used if control entry data type is unknown
        """
        if default is None:
            raise SelectError("get_component_val: %s_%s mandatory default parameter missing"
                              % (name, comp_name))
            
        name_comp = name
        if comp_name is not None:
            name_comp += "_" + comp_name
        comp_entry = self.get_ctl_entry(name_comp)
        if comp_entry is None:
            raise SelectError("get_component_value(%s, %s - component NOT FOUD"
                               % (name, comp_name))

        if comp_entry is not None:
            if comp_entry.value_type is None:
                comp_entry.value_type = type(default)
            ctl_widget = comp_entry.ctl_widget
            if ctl_widget is not None:
                widget_val = comp_entry.get_input()
                if widget_val is not None:
                    vt = comp_entry.value_type
                    if vt == int:
                        if widget_val == "":
                            widget_val = "0"      # Treat undefined as 0
                        value = int(widget_val)
                    elif vt == float:
                        if widget_val == "":
                            widget_val = "0"      # Treat undefined as 0
                        value = float(widget_val)
                    elif vt == str:
                        value = widget_val
                    else:
                        value = widget_val          # No change - should we check?
                        SlTrace.lg("get_component_val: %s ??? value_type(%s) widget_val=%s type(%s)"
                                   % (name_comp, vt, widget_val, type(widget_val)))        
                        SlTrace.lg("  type(int)=%s comp_entry.value_type=%s"
                                   % (type(int), comp_entry.value_type))        
                    return value
                else:
                    SlTrace.lg("get_component_val: %s None return from comp_entry.get_input"
                               % comp_name)
            return comp_entry.value

        return default                  # No component entry - return default
    

    def step_end(self, name, new_value):
        """ Do appropriate end condition action for component
        :name: component base name
        :new_value: prospective new value
        """
        min_value = self.get_component_val(name, "min", new_value)
        max_value = self.get_component_val(name, "max", new_value)
        end_value = self.get_component_val(name, "end", "wrap")
        if new_value < min_value:
            if end_value == "reverse":
                self.set_component_value(name, "next", "ascend")
                new_value = min_value
            elif end_value == "wrap":
                new_value = max_value
            elif end_value == "random":
                new_value = random.randint(min_value, max_value)
        else:   # > max_value
            if end_value == "reverse":
                self.set_component_value(name, "next", "descend")
                new_value = max_value
            elif end_value == "wrap":
                new_value = min_value
            elif end_value == "random":
                new_value = random.randint(min_value, max_value)
        return new_value

    def get_component_next_val(self, name,
                            nrange=50,
                            inc_dir=1,
                            default_value=None):
        """ Next value for this component
        :name: control name
        :nrange: - number of samples for incremental
        :default_value: default value
        """
        cur_value = self.get_current_val(name, 1)
        next_direction = self.get_component_val(name, "next", "same")
        if SlTrace.trace("get_next_val"):
            SlTrace.lg("get_next_val %s cur_val=%s next=%s"
                       % (name, cur_value, next_direction))
        if isinstance(cur_value, str):
            next_value = self.ctl_list_value(name)
            SlTrace.lg("get_value %s str next=%s val=%s"
                        % (name, next_direction, next_value), "get_next_val")
            
            return next_value
        
        else:
            min_value = float(self.get_component_val(name, "min", cur_value))
            max_value = float(self.get_component_val(name, "max", cur_value))
            inc_value = (max_value-min_value)/nrange            
            if next_direction == "ascend":
                new_value = cur_value + inc_dir * inc_value
            elif next == "descend":
                new_value = cur_value - inc_dir * inc_value
            elif next_direction == "random":
                new_value = random.randint(min_value, max_value)
            else:
                new_value = cur_value + inc_value
            if new_value < min_value or new_value > max_value:
                new_value = self.step_end(name, new_value)
            self.set_current_val(name, new_value)

        

    def set_component_value(self, name, comp_name, value):
        """ Set component value of named control
        Get value from widget, if present, else use entry value
        :name: - base name
        :comp_name: - component name
        :value: if present, use this value,  else get from widget
        """
        name_comp = name + "_" + comp_name
        comp_entry = self.get_ctl_entry(name_comp)
        if comp_entry is None:
            raise SelectError("set_component_value(%s, %s - component NOT FOUD"
                               % (name, comp_name))
            return value
        
        if value is not None:                
            comp_entry.value = comp_entry.to_value(value)
            self.show_entry(name_comp)
        self.update_property(name_comp)
        return value
    

    def get_current_val(self, name, default):
        """ Get current value of named control
        Get value from widget, if present, else use entry value
        """
        return  self.get_component_val(name, "current", default)


    def set_current_val(self, name, value):
        """ Set component value of named control
        Get value from widget, if present, else use entry value
        """
        self.set_component_value(name, "current", value)


    def get_inc_val(self, name, default):
        """ Get current value of named control
        Get value from widget, if present, else use entry value
        """
        return  self.get_component_val(name, "inc", default)
    

    def get_ctl_entry(self, name):
        try:
            return self.control_d[name]
        except:
            return None


    def set_list(self, ctl_name, selection_list = None, current_index = 0):
        """ Setup selection list for control
        :ctl_name: control name (list name)
        :selection_list: list of choices
        """
        lists_entry = [current_index, selection_list]
        self.ctl_lists[ctl_name] = lists_entry
        return selection_list
    
    def ctl_list(self, ctl_name):
        lists_entry = self.ctl_lists[ctl_name]
        return lists_entry[1]
    
    def ctl_list_value(self, ctl_name, prog=None, end="wrap"):
        """ Return next list entry, given prog: same, random, ascend, descend
        """
        ctl_choice = self.get_component_val(ctl_name, "current", "NONE_FOUND")
        ctl_list = self.ctl_list(ctl_name)
        ctl_list_cur = 0            # If not found
        if ctl_choice != "NONE_FOUND":
            for i in range(len(ctl_list)): 
                if ctl_list[i] == ctl_choice:
                    ctl_list_cur = i
                    break
                
        if prog is None:
            prog = self.get_component_val(ctl_name, "next", "random")
        if end is None:
            end = self.get_component_val(ctl_name, "end", "wrap")
        
        ctl_list_entry = self.ctl_lists[ctl_name]
        nchoice = len(ctl_list)
        ctl_list_next = ctl_list_cur
        if prog == "random":
            ctl_list_next = random.randint(0, nchoice-1)
        if prog == "ascend":
            ctl_list_next = ctl_list_cur + 1
        elif prog == "descend":
            ctl_list_next = ctl_list_cur - 1
        elif prog == "same":
            ctl_list_next = ctl_list_cur 
            
        if ctl_list_next >= nchoice:
            ctl_list_next = 0
        if ctl_list_next < 0:
            ctl_list_next = nchoice-1
                              
        entry = [ctl_list_next, ctl_list]
        self.ctl_lists[ctl_name] = entry
        choice = ctl_list[ctl_list_next]
        self.set_component_value(ctl_name, "current", choice)        
        return choice
    
    
    def get_ctl_val(self, name, default):
        """ Get control value.  If none return default
        """
        ctl_entry = self.get_ctl_entry(name)
        if ctl_entry is None:
            self.update_control_entry(name, default_value=default)
            ctl_entry = self.get_ctl_entry(name)
        val = ctl_entry.value
        if val is None:
            val = ctl_entry.default_value
        if val is None:
            return default
        
        return val


    def get_prop_key(self, name):
        """ Translate full  control name into full Properties file key
        """
        
        key = self.CONTROL_NAME_PREFIX + "." + name
        return key
 
    def get_prop_value(self, name, value):
        """ Get property value, if one, else use value.
        If property exists convert to type of value
        :name: control name
        :value: default value used if no property found,
             data type of value used if prop string  found        
        """
        if name in self.ctl_name_d:
            val_str = self.ctl_name_d[name]
            if isinstance(value, str):
                return val_str          # is str
            
            if isinstance(value, int):
                if val_str == "":
                    val_str = "0"
                return int(val_str)
            
            if isinstance(value, float):
                if val_str == "":
                    val_str = "0"
                return float(val_str)
            
            return val_str          # Return uncvhanged (str)
        
        return value                # Send given default
        

    def list_controls(self):
        """ List controls' settings
        """
        for name in self.get_ctl_names():
            self.list_control(name)


    def list_control(self, name):
        """ List control's settings
        """
        SlTrace.lg("control: %s" % name)
    
    
    def set(self):
        self.update_properties()
        if "set" in self.call_d:
            self.call_d["set"]()
    
    def run(self):
        self.update_properties()
        if "run" in self.call_d:
            self.call_d["run"]()
        
    def pause(self):
        if "pause" in self.call_d:
            self.call_d["pause"]()
        
    def step(self):
        self.update_properties()
        if "step" in self.call_d:
            self.call_d["step"]()
        
    def step_down(self):
        self.update_properties()
        if "step_down" in self.call_d:
            self.call_d["step_down"]()


    

    def update_form(self):
        """ Update any field changes
        """
        for name in self.ctl_name_d:
            ctn = self.ctl_name_d[name]
            if isinstance(ctn, ControlEntry):
                self.update_property(name)


    def update_properties(self):
        for name in self.get_ctl_names():
            self.update_property(name)


    def update_property(self, name):
        ctl_entry = self.get_ctl_entry(name)
        if ctl_entry is None:
            return                  # No entry
        
        if ctl_entry.ctl_widget is None:
            return                  # No widget
        
        ctl_value = ctl_entry.ctl_widget.get()
        prop_key = self.get_prop_key(name)
        SlTrace.setProperty(prop_key, ctl_value)
        
if __name__ == '__main__':
    def report_change(flag, val, cklist=None):
        SlTrace.lg("changed: %s = %d" % (flag, val))
        new_val = SlTrace.getLevel(flag)
        SlTrace.lg("New val: %s = %d" % (flag, new_val))
        if cklist is not None:
            cklist.list_ckbuttons()

    def run_button():
        SlTrace.lg("arrange_control Run Button")

    def set_button():
        SlTrace.lg("arrange_control Set Button")

    def pause_button():
        SlTrace.lg("arrange_control Pause Button")

    def step_button():
        SlTrace.lg("arrange_control Step Button")
        
    root = Tk()

    frame = Frame(root)
    frame.pack()
    SlTrace.setProps()
    SlTrace.setFlags("flag1=1,flag2=0,flag3=1,flag4=0, flag5=1, flag6=1")
    actl = ArrangeControl(frame, title="arrange_control", change_call=report_change)
    actl.set_call("run", run_button)
    actl.set_call("set", set_button)
    actl.set_call("pause", pause_button)
    actl.set_call("step", step_button)
        
    root.mainloop()