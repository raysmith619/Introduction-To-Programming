#wx_#my_label.py    10Jun2023  crs, from my_label.py
import wx

app = wx.App()
mf = wx.Frame(None)
panel = wx.Panel(mf)

# place a label on the root window
label = wx.StaticText(panel, label="Here's my label")

mf.Show()


# keep the window displaying
app.MainLoop()
