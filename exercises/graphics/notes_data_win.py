# notes_data_win.py 20Oct2022  crs, split off from notes_graphics.py
"""
Window GUI for notes_graphics.py
Developed after notes_g.py

Window:

data file         [___________]  [OPRN]
pattern(regex)    [___________]  [SEARCH]

[CLEAR]
________________________________
... lines
... where
... pattern
... was found
_______________________________
"""
import tkinter as tk
from tkinter import messagebox

class NotesDataWin:
    def __init__(self, mw=None, file_name=None,
                 pattern=None,
                 file_open_proc=None,
                 pattern_search_proc=None
                 ):
        """ Setup initial search
        :mw: master window default: create
        :file_name: file name
        :pattern: search pattern reg exp
        :file_open_proc: function to call, with file name, to open file
        :pattern_search_proc: function to call, with file name, pattern
                to search for and list
        """
        if mw is None:
            mw = tk.Tk()
        if file_name is None:
            file_name = def_file_name
        self.file_name = file_name
        if pattern is None:
            pattern = def_pattern
        self.pattern = pattern
        self.mw = mw
        self.file_name = file_name
        self.pattern = pattern
        self.file_open_proc = file_open_proc
        self.pattern_search_proc = pattern_search_proc
        self.setup_window()

    def setup_window(self):
        self.df_entry_var = tk.StringVar()    # Data file entry variable
        self.df_entry_var.set(self.file_name)
        self.pat_entry_var = tk.StringVar()     # Search pattern entry var
        self.pat_entry_var.set(self.pattern)

        # Controls: data file, pattern
        self.ctl_frame = tk.Frame(self.mw)
        self.ctl_frame.pack()
        # data file
        self.df_frame = tk.Frame(self.ctl_frame)    # file 
        self.df_frame.pack(side=tk.TOP)
        self.df_label = tk.Label(self.df_frame,
                                 text="data file")
        self.df_label.pack(side=tk.LEFT)

        self.df_entry = tk.Entry(self.df_frame,
                                 textvariable=self.df_entry_var,
                                 bd=3)
        self.df_entry.pack(side=tk.LEFT)
        self.df_entry.bind("<Return>",
                           self.df_entry_proc)

        self.df_set_button = tk.Button(self.df_frame,
                                       text="OPEN",
                                       command=self.df_open_cmd,
                                       fg="blue", bg="light gray")
        self.df_set_button.pack(side=tk.LEFT)


        # Pattern                         
        self.pat_frame = tk.Frame(self.ctl_frame)   # Pattern search
        self.pat_frame.pack(side=tk.TOP)


        self.pat_label = tk.Label(self.pat_frame,
                                  text="pattern(regex)")
        self.pat_label.pack(side=tk.LEFT)

        self.pat_entry = tk.Entry(self.pat_frame,
                                  textvariable=self.pat_entry_var,
                                  bd=3)
        self.pat_entry.bind("<Return>",
                            self.pat_entry_proc)
        self.pat_entry.pack(side=tk.LEFT)
        self.pat_search_button = tk.Button(self.pat_frame,
                                    text="SEARCH",
                                    command=self.pat_search_cmd,
                                    fg="blue", bg="light gray")
        self.pat_search_button.pack(side=tk.LEFT)


        # Listing
        self.list_frame = tk.Frame(self.mw)
        self.list_frame.pack(side=tk.BOTTOM)
        self.list_ctl_frame = tk.Frame(self.list_frame)
        self.list_ctl_frame.pack(side=tk.TOP)
        self.list_clear_button = tk.Button(self.list_ctl_frame,
                                    text="CLEAR",
                                    command=self.list_clear_cmd,
                                    fg="blue", bg="light gray")
        self.list_clear_button.pack(side=tk.TOP)
        self.list_text_frame = tk.Frame(self.list_frame)
        self.list_text_frame.pack(side=tk.TOP)
        # Vertical Scrollbar
        v = tk.Scrollbar(self.list_text_frame,
                         orient='vertical')
        v.pack(side=tk.RIGHT, fill='y')
        self.pat_list_text_region = tk.Text(
                                self.list_text_frame,
                                yscrollcommand=v.set)
        v.config(command=self.pat_list_text_region.yview)
        self.pat_list_text_region.pack(side=tk.BOTTOM)
        self.scroll_v = v
        
    def file_open(self):
        """ Open data file
        """
        if self.file_open_proc is not None:
            self.file_open_proc(self.file_name)

    def pattern_search(self):
        """ search for pattern
        """
        if self.pattern_search_proc is not None:
            self.pattern_search_proc(self.file_name,
                                     self.pattern)

    def df_open_cmd(self):
        """ data file OPEN button function command
        """
        self.df_entry_proc(self.df_entry)
        
    def df_entry_proc(self, _UNUSED_):
        """ data file entry return processing
            or OPEN button click
        """
        file_name = self.df_entry_var.get()
        if self.file_open_proc is not None:
            self.file_open_proc(file_name)
        else:
            print(f"df_entry return entered with {file_name}")

    def list_clear_cmd(self):
        """ Clear listing area
        """
        self.pat_list_text_region.delete(1.0, tk.END)
        
    def list_print(self,*args, end="\n"):
        """ print to listing area
        :*args: print-like args
        """
        lstr = ""
        for ls in args:
            lstr += (str(ls)+end)
        print(*args,end=end)    
        self.pat_list_text_region.insert(tk.END, lstr)
        self.pat_list_text_region.yview(tk.END)  # scroll to end

    def pat_search_cmd(self):
        """ pattern SEARCH button function command
        """
        self.pat_entry_proc(self.df_entry)

    def pat_entry_proc(self, _UNUSED_):
        """ search pattern entry return
            or SEARCH command processing
        """
        self.file_name = self.df_entry_var.get()    # also get
        self.pattern = self.pat_entry_var.get()
        if self.pattern_search_proc is not None:
            self.pattern_search_proc(self.file_name,
                                     self.pattern)
        else:
            print(f"pat_entry return entered with {self.pat_entry_var}")

    def error_message(self, msg):
        """ error message
        :msg: message text
        """
        messagebox.showerror(msg)

    def info_message(self, title=None, msg=None):
        """ error message
        :msg: message text
        """
        messagebox.showinfo(title=title, message=msg)


    def warning_message(self, msg):
        """ warning message
        :msg: message text
        """
        messagebox.showwarning(msg)

if __name__ == "__main__":    
    import re

    # Default values
    def_file_name = "test.notes"
    def_pattern = "student"

    def file_open_proc(file_name):
        """ open/reopen file
        :file_name: file name
        :returns: file pointer if successful, None if not
        """
        print(f"file_open_proc({file_name})")

    def pattern_search_proc(file_name, pattern):
        """ search for pattern within file
        :file_name: file in which to search
        :pattern: pattern for which to search
        """
        print(f"pattern_search_proc({file_name}, {pattern})")
        
    NotesDataWin(file_name=def_file_name,
                 pattern=def_pattern,
                 file_open_proc=file_open_proc,
                 pattern_search_proc=pattern_search_proc)
    tk.mainloop()
