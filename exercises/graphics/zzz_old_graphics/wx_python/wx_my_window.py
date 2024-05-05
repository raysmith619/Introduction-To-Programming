#wx_my_window.py

import wx

app = wx.App()
frame = wx.Frame(None)  # None is IMPORTANT otherwise nothing is displayed
frame.Show()

app.MainLoop()
