# wx_gr_hello.py    09Jun2023  crs, From gr_hello.py
# gr_hello.py       12Aug2021   crs, use tkMessageBox
#                   07Mar2019   crs Author
"""

Put up a message
Simplest graphics example I know.
"""
import wx
title = "Hello"
message = "Hello World!"

app = wx.App()
ex = wx.Frame(None)
ex.Show()
wx.MessageBox(message, 'Info', wx.OK | wx.ICON_INFORMATION)



# Let's do another.
title = "New Title"
message = """ Longer message
- Multiple Lines
are supported.
"""
wx.MessageBox(message)

app.MainLoop()


