# wx_notes_data_win.py 21Jun2023  crs, from notes_data_win.py
# notes_data_win.py 20Oct2022  crs, split off from notes_graphics.py
"""
wxPython version
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
import wx


class NotesDataWin(wx.Frame):
    def __init__(self, mf=None, file_name=None,
                 pattern=None,
                 file_open_proc=None,
                 pattern_search_proc=None
                 ):
        """ Setup initial search
        :mw: master window Frame default: create
        :file_name: file name
        :pattern: search pattern reg exp
        :file_open_proc: function to call, with file name, to open file
        :pattern_search_proc: function to call, with file name, pattern
                to search for and list
        """
        if mf is None:
            mf = wx.Frame(None)
        super(wx.Frame, self).__init__(mf, title="Notes")

        if file_name is None:
            file_name = def_file_name
        self.file_name = file_name
        if pattern is None:
            pattern = def_pattern
        self.pattern = pattern
        self.mf = mf
        self.file_name = file_name
        self.pattern = pattern
        self.file_open_proc = file_open_proc
        self.pattern_search_proc = pattern_search_proc
        self.setup_window()

    def setup_window(self):
        panel = wx.Panel(self)
        notes_vbox = wx.BoxSizer(wx.VERTICAL)

        ctl_vbox = wx.BoxSizer(wx.VERTICAL)
        notes_vbox.Add(ctl_vbox, flag=wx.CENTER)

        df_hbox = wx.BoxSizer(wx.HORIZONTAL)
        ctl_vbox.Add(df_hbox, flag=wx.CENTER)
        df_label = wx.StaticText(panel, label="data file")
        df_hbox.Add(df_label, flag=wx.CENTER, border=20)
        df_entry = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        df_entry.SetValue(self.file_name)
        df_entry.Bind(wx.EVT_TEXT_ENTER, self.df_entry_proc)
        self.df_entry = df_entry
        df_hbox.Add(df_entry, flag=wx.RIGHT)
        df_set_button = wx.Button(panel, label='OPEN')
        df_set_button.Bind(wx.EVT_BUTTON, self.df_entry_proc)
        df_hbox.Add(df_set_button)

        pat_hbox = wx.BoxSizer(wx.HORIZONTAL)
        ctl_vbox.Add(pat_hbox, flag=wx.CENTER)
        pat_label = wx.StaticText(panel, label="pattern (rex)")
        pat_hbox.Add(pat_label, flag=wx.CENTER, border=20)
        pat_entry = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        pat_entry.SetValue(self.pattern)
        pat_entry.Bind(wx.EVT_TEXT_ENTER, self.pat_entry_proc)
        self.pat_entry = pat_entry
        pat_hbox.Add(pat_entry, flag=wx.RIGHT)
        pat_set_button = wx.Button(panel, label='SEARCH')
        pat_set_button.Bind(wx.EVT_BUTTON, self.pat_entry_proc)
        pat_hbox.Add(pat_set_button)


        list_ctl_vbox = wx.BoxSizer(wx.VERTICAL)
        notes_vbox.Add(list_ctl_vbox,  1, flag=wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM|wx.EXPAND)
        list_clear_button = wx.Button(panel, label='CLEAR')
        list_clear_button.Bind(wx.EVT_BUTTON, self.list_clear_proc)
        list_ctl_vbox.Add(list_clear_button, flag=wx.CENTER)
        list_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_PROCESS_TAB)
        self.list_text = list_text
        list_ctl_vbox.Add(list_text, 1, flag=wx.EXPAND)

        panel.SetSizerAndFit(notes_vbox)
        self.Show()

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
        file_name = self.df_entry.GetValue()
        if self.file_open_proc is not None:
            self.file_open_proc(file_name)
        else:
            print(f"df_entry return entered with {file_name}")

    def list_clear_proc(self, _UNUSED_):
        """ Clear listing area
        """
        self.list_text.Clear()

    def list_print(self,*args, end="\n"):
        """ print to listing area
        :*args: print-like args
        """
        lstr = ""
        for ls in args:
            lstr += (str(ls)+end)
        print(*args,end=end)
        self.list_text.write(lstr)

    def pat_search_cmd(self):
        """ pattern SEARCH button function command
        """
        self.pat_entry_proc(self.df_entry)

    def pat_entry_proc(self, _UNUSED_):
        """ search pattern entry return
            or SEARCH command processing
        """
        self.file_name = self.df_entry.GetValue()    # also get
        self.pattern = self.pat_entry.GetValue()
        if self.pattern_search_proc is not None:
            self.pattern_search_proc(self.file_name,
                                     self.pattern)
        else:
            print(f"pat_entry return entered with {self.pat_entry_var}")

    def error_message(self, msg):
        """ error message
        :msg: message text
        """
        dlg = wx.MessageDialog(parent=self, message=msg, caption="ERROR")
        ans = dlg.ShowModal()
        dlg.Destroy()

    def info_message(self, title=None, msg=None):
        """ error message
        :msg: message text
        """
        dlg = wx.MessageDialog(parent=self, message=msg, caption="Info")
        ans = dlg.ShowModal()
        dlg.Destroy()

    def warning_message(self, msg):
        """ warning message
            :msg: message text
            """
        dlg = wx.MessageDialog(parent=self, message=msg, caption="Warning")
        ans = dlg.ShowModal()
        dlg.Destroy()

if __name__ == "__main__":    
    import re

    app = wx.App()

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
        
    ndw = NotesDataWin(file_name=def_file_name,
                 pattern=def_pattern,
                 file_open_proc=file_open_proc,
                 pattern_search_proc=pattern_search_proc)

    ndw.list_print("""
    Test string
    More of the same
    ABC
    """)

    app.MainLoop()
