#my_menu_mult.py   26Oct2022  crs, from my_menu.py
#
# Demonstrates multiple menus with drop-downs

import tkinter as tk

# root window
root = tk.Tk()
root.title('Multiple Menu Demo')
    
# create a menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

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
    heading_menu = tk.Menu(menubar)
    # create drop-down selections
    for j in range(len(sub_lst)):
        hi = i%len(menu_lst)    # clip to list sizes
        ddj = j%len(sub_lst)
        
        # create a command for the current drop-down
        # Each command calls the common menu_command
        # with identifying heading, drop-down indexes
        def menu_cmd(h=hi, d=ddj):   #binding h,d to hi,ddj
            menu_command(h,d)
            
        lbl = menu_lst[hi]      # Drop-down label
        lbl += "-" + sub_lst[ddj]
        heading_menu.add_command(    
            label=lbl,
            command=menu_cmd)

    # add the heading menu to the menubar
    menubar.add_cascade(
        label=menu_lst[i%len(menu_lst)],
        menu=heading_menu)

root.mainloop()     # Process window events


