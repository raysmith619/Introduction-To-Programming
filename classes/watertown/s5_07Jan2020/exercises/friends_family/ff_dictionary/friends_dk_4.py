#friends_dk_4.py   23Jun2020  crs, adapted from friends_4
"""
Note that, except that we used a different file for the
module (friends_dk_mod.py instead of friends_mod.py)
no code needed changing.

This is an example of using import to use code (functions)
existing in other files
The two main forms of import
import <file>
from <file> import function_name1, function_name2,...

Importing all functions, as well as visible
variables defined in file friends_mod.py:
from friends_mod import *
"""
from friends_dk_mod import *
add_friends("a", "b", "c")
list_friends()

for fr in my_friends:   # NOTE fr(name) is a dictionary key
    if is_friend(fr):
        print(fr, "is a friend")
