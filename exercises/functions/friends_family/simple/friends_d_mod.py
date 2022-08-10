#friends_d_mod.py    03Jul2022   crs, author
"""
Introduction writing a module - file which can be used
Include a self test
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
print("__name__:",__name__)
if __name__ == "__main__":
    list_friends()
    my_friends = ["Mary", "Tom", "Jane"]
    list_friends()
    my_friends.append("Ray")
    list_friends()

