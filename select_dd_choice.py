"""
Created on Oct 6, 2018

@author: raysm
"""
from tkinter import *

class SelectDDChoice(object):
    """
    Dropdown choice one of n text strings
    """


    def __init__(self, ctl_frame,
                    selection,
                    default=None):
        """ Setup Dropdown menu for selection
        :ctl_frame: containing / controling frame/widget
        :selection:  list  of text strings
        :default: default text string - None  - use first
        """
        tkvar = StringVar(ctl_frame)

        if default is None:
            default = selection[0]
        tkvar.set(default)
        self.tkvar = tkvar
        sel_dict = {}
        for s in selection:
            sel_dict[s] = s
        popup_menu = OptionMenu(ctl_frame,  tkvar, *sel_dict)
        self.popup_menu = popup_menu
        ###popup_menu.pack()
        
        
    def get(self):
        return self.tkvar.get()


    def pack(self, **kwargs):
        self.popup_menu.pack(kwargs)
        
        
    def set(self, val):
        self.tkvar.set(val)

    
    def set_field(self, val):
        self.set(val)
        
        
            
if __name__ == '__main__':
    root = Tk()
    root.title("SelectDDChoice test")
    
    ctl_frame = Frame(root)
    ctl_frame.pack()
    sel=["random", "ascend", "descend"]
    sel_default="random"
    val_entry = SelectDDChoice(ctl_frame,
                                selection=sel,
                                default=sel_default)
    value_type = str
    # on change dropdown value
    def change_dropdown(*args):
        print( val_entry.tkvar.get() )
     
    # link function to change dropdown
    val_entry.tkvar.trace('w', change_dropdown)
 
    root.mainloop()