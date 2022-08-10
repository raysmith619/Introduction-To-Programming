#friends_e2.py    03Jul2022   crs, author
"""
Introduction writing a module - file which can be used
Include a self test
shorten name 
"""
import friends_d_mod as fr
"""
Test friends_d_mod
"""
fr.my_friends = []
fr.list_friends()
fr.my_friends = ["Mary", "Tom", "Jane"]
fr.list_friends()
fr.my_friends.append("Ray")
fr.list_friends()

