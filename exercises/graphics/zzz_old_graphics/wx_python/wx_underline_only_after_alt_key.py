#wx_underscore_only_if_ALT  crs, Adapted from www.zetcode.com menu_simple.py
"""
Demonstrates that menu heading underscore, for shortcut
is only visible when holding down ALT key
"""
import wx

app = wx.App()
frame = wx.Frame(None)
menubar = wx.MenuBar()
fileMenu = wx.Menu()
menubar.Append(fileMenu, '&File')

frame.SetMenuBar(menubar)
frame.Show()
app.MainLoop()
