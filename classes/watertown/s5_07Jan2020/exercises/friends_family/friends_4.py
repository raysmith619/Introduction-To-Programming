#friends_4.py   23Jun2020  crs, showing import
"""
This is an example of using import to use code (functions)
existing in other files
The two main forms of import
import <file>
from <file> import function_name1, function_name2,...

Importing all functions, as well as visible
variables defined in file friends_mod.py:
from friends_mod import *
"""
from friends_mod import *
add_friends("a", "b", "c")
list_friends()

for fr in my_friends:
    if is_friend(fr):
        print(fr, "is a friend")
