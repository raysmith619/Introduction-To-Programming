#friends_c.py    03Jul2022   crs, author
"""
Simplest introduction to function tool building
A simple demonstration of functions' purpose  and use
Add a list_friends function.
"""
my_friends = []     # Initialize list of friends(names)
                    # as an empty list

def list_friends():
    print("\nFriends:")
    for friend in my_friends:
        print(friend)
"""
Do testing
"""
list_friends()
my_friends = ["Mary", "Tom", "Jane"]
list_friends()
my_friends.append("Ray")
list_friends()

