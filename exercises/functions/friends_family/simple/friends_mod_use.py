#friends_mod_use.py    03Jul2022   crs, author
"""
Introduction writing a module - file which can be used
Use friends_mod via import
"""
import friends_mod as fr    # shortened name

"""    
Do testing
"""
fr.set_friends()   # Clear list
fr.list_friends()
fr.set_friends(["Mary", "Tom", "Jane"])
fr.list_friends()
fr.add_friend("Ray")
fr.list_friends()

