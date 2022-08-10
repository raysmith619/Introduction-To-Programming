#friends_e.py    03Jul2022   crs, author
"""
Introduction writing a module - file test module
"""
import friends_d_mod
"""
Test friends_d_mod
"""
friends_d_mod.my_friends = []
friends_d_mod.list_friends()
friends_d_mod.my_friends = ["Mary", "Tom", "Jane"]
friends_d_mod.list_friends()
friends_d_mod.my_friends.append("Ray")
friends_d_mod.list_friends()

