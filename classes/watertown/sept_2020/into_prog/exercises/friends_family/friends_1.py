#friends_1.py    19Jun2020   crs, author
"""
First introduction to family and friends
A simple demonstration of functions' purpose  and use
More introduction can be found in the README text file.
"""
my_friends = []     # Initialize list of friends(names) as an empty list

def list_friends():
    """ list friends
    """
    nf = 0                          # Count of number listed so far
    print("friends: ", end="")
    for friend in my_friends:
        if nf > 0:
            print(", ", end="")     # Separate after first
        print(friend, end="")       # On one line
        nf += 1
    print()         # Add newline end of list
    
def test_list_friends():    
    """ Test, or atleast exercise, list_friends function
    """
    global my_friends           # REQUIRED to allow us to modify
                                # variable outside function
    print("\ntest_list_friends")
    my_friends = []             # check on empty list
    print("Empty list")
    list_friends()
    new_friends = ["a", "b", "c"]
    print("New friends:", new_friends)
    my_friends = new_friends
    list_friends()
    
def add_one_friend(friend):
    """ Adds one friend to our list
    :friend: friend's name
    """
    global my_friends           # REQUIRED to allow us to modify
                                # variable outside function
    print("add_one_friend(",
          friend, ")", sep="")
    my_friends.append(friend)   # Add to list (no check to insure
                                # not here already)
    list_friends()
    
def test_add_one_friend():    
    """ Test, or atleast exercise, add_one_friend function
    """
    global my_friends           # REQUIRED to allow us to modify
                                # variable outside function
    print("\ntest_add_one_friend")
    my_friends = []             # Start with empty list
    add_one_friend("tom")
    add_one_friend("joe")
    list_friends()

"""
Do testing
"""
test_list_friends()
test_add_one_friend()
