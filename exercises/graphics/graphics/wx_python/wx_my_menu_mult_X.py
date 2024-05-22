#wx_my_menu_mult.py   15Jun2023  crs, from my_menu_mult.py
"""
Using wxPython
Adapted from tkinter
    Demonstrates multiple menus with drop-downs
"""
import wx

from get_menu_cmd import *

# root window/frame
app = wx.App()
frame = wx.Frame(None)
#frame.title('wx Multiple Menu Demo')
    
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
heading_menus = []
menu_cmds = []
menu_items = []
for i in range(len(menu_lst)):
    heading_menus.append(wx.Menu())
    heading_menu = heading_menus[-1]
    # create drop-down selections
    for j in range(len(sub_lst)):
        hi = i%len(menu_lst)    # clip to list sizes
        ddj = j%len(sub_lst)
        print(f"i:{i} hi:{hi} j:{j} ddj:{ddj}")
        # create a command for the current drop-down
        # Each command calls the common menu_command
        # with identifying heading, drop-down indexes
        '''
        def menu_cmd(e=None, h=hi, d=ddj):   #binding h,d to hi,ddj
            print(f"menu_cmd: menu_cmd:{menu_cmd} hi:{hi} ddj:{ddj} e:{e} h:{h} d:{d}")
            menu_command(hi=h, ddj=d)
        '''

        lbl = menu_lst[hi]      # Drop-down label
        lbl += "-" + sub_lst[ddj]
        menu_items.append(heading_menu.Append(wx.ID_ANY, lbl, "desc-" + lbl))
        menu_item = menu_items[-1]
        menu_cmds.append(get_menu_cmd(proc=menu_command, hi=hi, ddj=ddj))
        menu_cmd = menu_cmds[-1]
        print(f"menu_cmd: menu_cmd:{menu_cmd} hi:{hi} ddj:{ddj}")

        frame.Bind(wx.EVT_MENU, menu_cmd, id=menu_item.GetId())
    menubar.Append(heading_menu,  menu_lst[i%len(menu_lst)])

frame.SetMenuBar(menubar)
frame.SetSize((300, 200))
frame.SetTitle('wx_my_menu_mult')
frame.Centre()
frame.Show()

app.MainLoop()     # Process events


