#tk_wx_example_tk_show.py   20Oct2023  crs
"""
tk program calling wxPython module
leave tk_window visible 
"""
import tkinter as tk
import tk_wxapp
import wx

import multiprocessing as mp

########################################################################
class WxProc(mp.Process):
    """ Process
    which holds a wxPython application
    """

    #----------------------------------------------------------------------
    def __init__(self, win_no):
        """ Setup process to contain the wxPython
        window
        """
        print(f"WxProc({win_no})")
        mp.Process.__init__(self, target=self.wx_run, args=[win_no])
        self.start()

    #----------------------------------------------------------------------
    def wx_run(self, win_no):
        """ Open and run wxPython window
        """
        print(f"wx_run: {win_no}")
        app = wx.App(False)
        frame = tk_wxapp.MyFrame(win_no)
        app.MainLoop()


########################################################################
class MyApp(object):
    """ tkinter based application
    """

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.win_no = 1     # Bumped after each call
        self.root = parent
        self.root.title = "tk App"

        self.frame = tk.Frame(parent)
        self.frame.pack()
        self.btn_text = tk.StringVar()
        self.btn_text.set(f"wxPython window {self.win_no}")
        btn = tk.Button(self.frame, textvariable=self.btn_text,
                             command=self.run_wx)
        btn.pack()

    def run_wx(self):
        """ Run wxPython based process
        """
        proc = WxProc(self.win_no)
        self.win_no += 1
        self.btn_text.set(f"wxPython window {self.win_no}")

#----------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()


