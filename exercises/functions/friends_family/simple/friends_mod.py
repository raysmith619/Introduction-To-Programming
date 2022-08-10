#friends_mod.py    03Jul2022   crs, author
"""
Introduction writing a module - file which can be used

Add the following so we need never expose
my_friends variable to users.

Include a self test
"""
my_friends = []     # Initialize list of friends(names)
                    # as an empty list

def list_friends():
    print("\nFriends:")
    for friend in my_friends:
        print(friend)

def set_friends(friends=None):
    """ Set internal friends list
    :friends: new list to set friends
            default: clear out list to empty
    """
    global my_friends       # REQUIRED to allow setting
    
    if friends is None:
        friends = []        # To clear list
    my_friends = friends

def add_friend(friend):
    """ Add new friend
        NOTE: No check if friend already present
    :freind: new friend
    """
    my_friends.append(friend)

"""    
Do testing
"""
if __name__ == "__main__":
    set_friends()   # Clear list
    list_friends()
    set_friends(["Mary", "Tom", "Jane"])
    list_friends()
    add_friend("Ray")
    list_friends()

