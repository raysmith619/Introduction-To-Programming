#friends_3.py    19Jun2020   crs, from friends_2.py
"""
A bit more to family and friends
Add a test for contents, example: is_friend
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
    print("\nadd_friends(",
          ",".join(friends), ")")    # passing on list to print
    for friend in friends:  # comma separated args become list
        add_one_friend(friend)

def is_friend(possible):
    """ Check if possible is a friend, that is in my_friends
    :possible: name of possible friend
    :returns: True if possible is a friend
    """
    for friend in my_friends:
        if possible == friend:
            return True         # possible is in list
    return False                # Not in list

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

def test_is_friend_ck(possible, expect=True):
    """ Helper function check if test passes
    :possible: possible friend
    :expect: expected value (True,False)
        default: True - expected friend
    """
    print("test_is_friend_ck:", possible, "expect=", expect, end="")
    result = is_friend(possible)
    if result == expect:
        print(" Passed Test")
    else:
        print(" FAILED Test result=", result, "expected=", expect)
        
def test_is_friend():
    """ Test is_friend function
    """
    global my_friends           # REQUIRED to allow us to modify
                                # variable outside function
    print("\ntest_is_friend()")
    print("Set up friends list")
    my_friends = []             # Start test with empty list
    add_friends("joe", "mary", "ray")
    print("\nCheck is_friend function")
    test_is_friend_ck("joe")    # Check if True as expected
    test_is_friend_ck("marty", expect=False)    # Check if False
    test_is_friend_ck("mary", expect=True)      # Ck if True explicit
    print("Test the testing - this should fail the test.")
    test_is_friend_ck("alex")               # Should fail this!
    
test_all = False
if test_all:
    test_add_one_friend()
    test_add_friends()
test_is_friend()
