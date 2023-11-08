# tk_wxapp.py  20Oct2023  crs
"""
wxPython app called from tkinter
Developed from Mike Driscoll's stackoverflow answer
"""


import wx

btn_height = 50
btn_width = int(1.5 * btn_height)
pos_1 = wx.Point(int(btn_width/2),btn_height)
ok_height = btn_height
ok_width = btn_width

def ok_cmd(e):
    print("ok_cmd")

########################################################################
class MyFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, win_no):
        """Constructor"""
        wx.Frame.__init__(self, None, title=f"wxPython App {win_no}")
        panel = wx.Panel(self)
        ok_button = wx.Button(panel, label="OK", pos=pos_1,
                            size=(ok_width, ok_height))
        ok_button.Bind(wx.EVT_BUTTON, ok_cmd)
        
        self.Show()