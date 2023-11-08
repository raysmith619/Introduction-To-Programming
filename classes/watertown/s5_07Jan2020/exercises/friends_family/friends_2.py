#friends_2.py    19Jun2020   crs, from friends_1.py
"""
A bit more to family and friends
Introduce variable number of function arguments, using the
parameter name "*args"
With the "*" python knows that the function definer (You)
wants to consider the list of comma-separated parameter
as a list.  Please see function definition "add_friends" below
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

def add_friends(*friends):
    """ Add zero or more friends
    :*friends: zero or more friend names
    """
    print("\nadd_friends(", *friends, ")")    # passing on list to print
    for friend in friends:  # comma separated args become list
        add_one_friend(friend)


"""
Do testing
"""    
def test_add_one_friend():    
    """ Test, or atleast exercise, add_one_friend function
    """
    global my_friends           # REQUIRED to allow us to modify
                                # variable outside function
    print("\ntest_add_one_friend")
    my_friends = []             # Start test with empty list
    add_one_friend("tom")
    add_one_friend("joe")

def test_add_friends():    
    """ Test, or atleast exercise, add_one_friend function
    """
    global my_friends           # REQUIRED to allow us to modify
                                # variable outside function
    print("\ntest_add_friends()")
    my_friends = []             # Start test with empty list
    add_friends("tom")
    add_friends("joe", "mary", "ray")
    
test_add_one_friend()
test_add_friends()
