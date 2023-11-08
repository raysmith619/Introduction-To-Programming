#add_friends_fun.py 24Sep2020  crs, new list_friends.py
"""
Friends - Simple List Example
Add names to list, print if entry is empty
using print_friends() function
"""
my_friends = [
    "Ray Smith",
    "Tony Suprano",
    "Chris Kringle",
    ]

def print_friends():
    """ Print my_friends list
    """
    global my_friends
    print("======================")
    for name in my_friends:
        print(name)
    print("======================")
    
while True:
    ans = input("Enter friend:")
    if ans == "":
        print_friends()
        break
    else:
        my_friends.append(ans)

       
