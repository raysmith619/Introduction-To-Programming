#my_menu.py   22Oct2022  crs, very simple menu
#
# From: https://www.pythontutorial.net/tkinter/tkinter-menu/
# With a few modifications

import tkinter as tk

# root window
root = tk.Tk()
root.title('Menu Demo')

def file_open_cmd():
    """ File Open - called via File-->Open
    To be done
    """
    print("file_open not yet implemented")
    
# create a menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = tk.Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='Open',
    command=file_open_cmd)

# add a menu item to the menu
file_menu.add_command(
    label='Exit', underline=1,
    command=root.destroy)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu)

root.mainloop()
print("After mainloop")



