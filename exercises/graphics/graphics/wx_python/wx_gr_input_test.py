#wx_gr_input_test.py   10Jun2023  crs, from gr_input_test.py
#gr_input_test.py   12Aug2021   crs, from gr_input.py
"""
Prompt User and accept input
"""
from wx_gr_input import *  # Get all gr_input.py functions
"""
Testing Code
"""
app = wx.App()

inp = gr_input("Enter Number:")
print("We got:", int(inp))

inp = gr_input("Enter String:")
print("We got:", inp)

app.MainLoop()


