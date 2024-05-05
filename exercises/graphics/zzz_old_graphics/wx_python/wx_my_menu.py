#wx_my_menu.py 14Jun2023  crs, Adapted from www.zetcode.com menu_simple.py

import wx

app = wx.App()
frame = wx.Frame(None)

def OnOpen(self, e=None):
    print("Open - to be implemented")

def OnQuit(self, e=None):
    print("Quitting")
    frame.Close()

menubar = wx.MenuBar()
fileMenu = wx.Menu()
open_fileItem = fileMenu.Append(wx.ID_OPEN, '&Open', 'Open file')
frame.Bind(wx.EVT_MENU, OnOpen, open_fileItem)

quit_fileItem = fileMenu.Append(wx.ID_EXIT, '&Quit', 'Quit application')
frame.Bind(wx.EVT_MENU, OnQuit, quit_fileItem)

menubar.Append(fileMenu, '&File')

frame.SetMenuBar(menubar)

frame.SetSize((300, 200))
frame.SetTitle('wx_my_menu')

frame.Centre()


frame.Show()
app.MainLoop()
