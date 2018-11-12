#select_window.py 19Sep2018
"""
Program Level Menu control
 From PoolWindow
"""
import os
from tkinter import *
from select_trace import SlTrace
from trace_control import TraceControl
from arrange_control import ArrangeControl

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class SelectWindow(Frame):
            
        
    # Define settings upon initialization. Here you can specify
    def __init__(self,
                 master=None,
                 title=None,
                 pgmExit=exit,
                 games=[],          # text, proc pairs
                 actions=[],
                 ):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.title = title
        self.master = master
        self.pgmExit = pgmExit
        self.games = games
        self.actions = actions
        self.tc = None          # Trace control
        self.arc = None         # Arrangement control
        self.arc_call_d = {}     # arc call back functions
        
        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

        
    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget 
        if self.title is not None:
            self.master.title(self.title)

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # create the file object)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.File_Open_tbd)
        filemenu.add_command(label="Save", command=self.File_Save_tbd)
        filemenu.add_separator()
        filemenu.add_command(label="Properties", command=self.Properties)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.pgmExit)
        menubar.add_cascade(label="File", menu=filemenu)

                                # Arrange control
        menubar.add_command(label="Arrange", command=self.arrange_control)

                                # Trace control
        menubar.add_command(label="Trace", command=self.trace_control)

    def File_Open_tbd(self):
        print("File_Open_menu to be determined")

    def File_Save_tbd(self):
        print("File_Save_menu to be determined")

    def get_arc(self):
        """ Return reference to arrange control
        """
        return self.arc
    
    
    def Properties(self):
        print("Display Properties File")
        abs_propName = SlTrace.defaultProps.get_path()
        SlTrace.lg("properties file  %s"
                    % abs_propName)
        ###osCommandString = "notepad.exe %s" % abs_propName
        ###os.system(osCommandString)
        import subprocess as sp
        programName = "notepad.exe"
        sp.Popen([programName, abs_propName])
        
        
    def select_all(self):
        if self.tc is None:
            self.select_trace()
        self.tc.select_all()
        
            
    def select_none(self):
        if self.tc is None:
            self.select_trace()
        self.tc.select_none()

        

    def arrange_control(self):
        """ Create arrangement window
        :returns: ref to ArrangeControl object
        """
        if self.arc is not None:
            self.arc.delete_window()
            self.arc = None
        
        self.arc = ArrangeControl(self, title="Arrange")
        for callname, callfn in self.arc_call_d.items():     # Enable any call back functions
            self.arc.set_call(callname, callfn)
        return self.arc

    def ctl_list(self, ctl_name, selection_list):
        return self.arc.ctl_list(ctl_name, selection_list)


    def get_ctl_entry(self, name):
        """ Get control value.  If none return default
        """
        if self.arc is None:
            return None
        return self.arc.get_entry_val(name)
 

    def get_current_val(self, name, default=None):
        """ Get control value.  If none return default
        """
        if self.arc is None:
            return default
        return self.arc.get_current_val(name, default)


    def get_component_val(self, name, comp_name, default=None):
        """ Get component value of named control
        Get value from widget, if present, else use entry value
        """
        if self.arc is None:
            return default
        return self.arc.get_component_val(name, comp_name, default)

    def get_component_next_val(self, base_name,
                            nrange=50,
                            inc_dir=1,
                            default_value=None):
        """ Next value for this component
        :control_name: control name
        :comp_name: component name
        :nrange: - number of samples for incremental
        :default_value: default value
        """
        return self.arc.get_component_next_val(base_name,
                                nrange=nrange, inc_dir=inc_dir, default_value=default_value)


    def get_inc_val(self, name, default):
        """ Get inc value.  If none return default
        """
        if self.arc is None:
            return default
        return self.arc.get_inc_val(name, default)
 

    def set_current_val(self, name, val):
        """ Set current value.
        """
        if self.arc is None:
            return
        return self.arc.set_current_val(name, val)
 

    def set_component_val(self, name, comp_name, val):
        """ Set current value.
        """
        if self.arc is None:
            return
        return self.arc.set_component_val(name, comp_name, val)
        
    
    def set_call(self, name, function):
        """ Set for call back from arrange control
           1. If arc present via arc
           2. Else store for later enabling when arc is created
        """
        if self.arc is not None:
            self.arc.set_call(name, function)
        else:
            self.arc_call_d[name] = function
 
        

    def trace_control(self):
 
        def report_change(flag, val, cklist=None):
            SlTrace.lg("changed: %s = %d" % (flag, val), "controls")
            new_val = SlTrace.getLevel(flag)
            SlTrace.lg("New val: %s = %d" % (flag, new_val), "controls")
            if cklist is not None:
                cklist.list_ckbuttons()
        
        if self.tc is not None:
            self.tc.delete_tc_window()
            self.tc = None
        
        self.tc = TraceControl(self, change_call=report_change)


    def tc_destroy(self):
        """ Called if TraceControl window closes
        """
        self.tc = None


    def update_form(self):
        """ Update any field changes
        """
        if self.arc is not None:
            self.arc.update_form()
#########################################################################
#          Self Test                                                    #
#########################################################################
if __name__ == "__main__":
    from trace_control import TraceControl    
        
    # root window created. Here, that would be the only window, but
    # you can later have windows within windows.
    mw = Tk()
    def user_exit():
        print("user_exit")
        exit()
        
    SlTrace.setProps()
    SlTrace.setFlags("flag1=1,flag2=0,flag3=1,flag4=0, flag5=1, flag6=1")
        
    mw.geometry("400x300")
    
    #creation of an instance
    app = SelectWindow(mw,
                    title="select_window Testing",
                    pgmExit=user_exit,
                    )
    

    
    #mainloop 
    mw.mainloop()  

