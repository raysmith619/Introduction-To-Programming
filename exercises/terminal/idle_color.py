#idle_color.py  20Oct2021  crs, from StackOverflow
"""
https://stackoverflow.com/questions/
42472958/how-do-i-print-colored-text-in-idles-terminal
"""
import sys

try:
    color = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

color.write("Hi, are you called Miharu461? \n","KEYWORD")
color.write("Yes","STRING")
color.write(" or ","KEYWORD")
color.write("No\n","COMMENT")
