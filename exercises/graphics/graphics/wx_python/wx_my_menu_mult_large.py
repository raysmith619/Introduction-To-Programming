#wx_my_menu_mult.py   15Jun2023  crs, from my_menu_mult.py
"""
Using wxPython
Adapted from tkinter
    Demonstrates multiple menus with drop-downs
"""
import wx

# root window/frame
app = wx.App()
frame = wx.Frame(None)

# create a menubar
menubar = wx.MenuBar()

def menu_command(hi=0,ddj=0):
    """Generic Menu command
    :hi: heading index (no index guard)
    :ddi: drop-down index (no index guard)
    """
    print(f"menu_command({hi},{ddj})")


nhead = 50
ndrop = 60
# create heading menus
for i in range(nhead):
    heading_menu = wx.Menu()
    # create drop-down selections
    for j in range(ndrop):
        hi = i
        ddj = j


        # create a command for the current drop-down
        # Each command calls the common menu_command
        # with identifying heading, drop-down indexes
        def menu_cmd(e=None, h=hi, d=ddj):   #binding h,d to hi,ddj
            """
            Recieves event from menu binding
            :param e: Optional event unused, not present in tkinter
            :param h: Menu heading index set via hi
            :param d: Submenu index set via ddj
            :return: Not used
            """
            menu_command(hi=h, ddj=d)


        lbl = f"{hi}:{ddj}"      # Drop-down label
        menu_item = heading_menu.Append(wx.ID_ANY, lbl, "desc-" + lbl)
        frame.Bind(wx.EVT_MENU, menu_cmd, id=menu_item.GetId())
    menubar.Append(heading_menu,  f"h{i}")

frame.SetMenuBar(menubar)
frame.SetSize((nhead*35, 200))
frame.SetTitle('wx_my_menu_mult_large')
frame.Centre()
frame.Show()

app.MainLoop()     # Process events


