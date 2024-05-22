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

menu_lst = ["One", "Two", "Three", "Four","Five"]
sub_lst = ["A", "B", "C", "D"]


def menu_command(hi=0,ddj=0):
    """Generic Menu command
    :hi: heading index (no index guard)
    :ddi: drop-down index (no index guard)
    """
    print(f"menu_command({menu_lst[hi]},{sub_lst[ddj]})")


# create heading menus
for i in range(len(menu_lst)):
    heading_menu = wx.Menu()
    # create drop-down selections
    for j in range(len(sub_lst)):
        hi = i%len(menu_lst)    # clip to list sizes
        ddj = j%len(sub_lst)

        def menu_cmd(e=None, h=hi, d=ddj):   #binding h,d to hi,ddj
            """
            Recieves event from menu binding
            :param e: Optional event unused, not present in tkinter
            :param h: Menu heading index set via hi
            :param d: Submenu index set via ddj
            :return: Not used
            """
            menu_command(hi=h, ddj=d)


        lbl = menu_lst[hi]      # Drop-down label
        lbl += "-" + sub_lst[ddj]
        menu_item = heading_menu.Append(wx.ID_ANY, lbl, "desc-" + lbl)
        frame.Bind(wx.EVT_MENU, menu_cmd, id=menu_item.GetId())
    menubar.Append(heading_menu,  menu_lst[i%len(menu_lst)])

frame.SetMenuBar(menubar)
frame.SetSize((300, 200))
frame.SetTitle('wx_my_menu_mult')
frame.Centre()
frame.Show()

app.MainLoop()     # Process events


