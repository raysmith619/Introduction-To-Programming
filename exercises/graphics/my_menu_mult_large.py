#my_menu_mult_large.py   26Oct2022  crs, from my_menu_mult.py
#
# Demonstrates multiple menus with drop-downs
# with large numbers

import tkinter as tk

# root window
root = tk.Tk()
root.title('Multiple Menu Demo')
    
# create a menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

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
    heading_menu = tk.Menu(menubar)
    # create drop-down selections
    for j in range(ndrop):
        hi = i
        ddj = j
        
        # create a command for the current drop-down
        # Each command calls the common menu_command
        # with identifying heading, drop-down indexes
        def menu_cmd(h=hi, d=ddj):   #binding h,d to hi,ddj
            menu_command(h,d)
            
        lbl = f"{hi}:{ddj}"      # Drop-down label
        heading_menu.add_command(    
            label=lbl,
            command=menu_cmd)

    # add the heading menu to the menubar
    menubar.add_cascade(
        label=f"h{i}",
        menu=heading_menu)

root.mainloop()     # Process window events


