#tk_wx_example.py   20Oct2023  crs
"""
tk program calling wxPython module 
"""
import tkinter as tk
import tk_wxapp
import wx

import multiprocessing as mp

########################################################################
class WxProc(mp.Process):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """"""
        mp.Process.__init__(self)
        self.start()

    #----------------------------------------------------------------------
    def run(self):
        """"""
        app = wx.App(False)
        frame = tk_wxapp.MyFrame()
        app.MainLoop()


########################################################################
class MyApp(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title = "tk App"

        self.frame = tk.Frame(parent)
        self.frame.pack()

        btn = tk.Button(self.frame, text="Open wxPython App",
                             command=self.run_wx)
        btn.pack()

    def run_wx(self):
        self.root.withdraw()
        proc = WxProc()
        proc.join()
        self.root.deiconify()

#----------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()


