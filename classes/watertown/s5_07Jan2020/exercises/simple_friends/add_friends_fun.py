#add_friends_fun.py    23Sep2020  crs, From add_friends
# Simple List Example, using functions
"""
Add to list
Print list, if entry is empty, using a function
"""
# Initial list of friends names
my_friends = [
    "Ray Smith",
    "Phil Fontain",
    "Rich Parker",
    ]

def print_friends():
    # Simple loop to print out names from list
    for name in my_friends:
        print(name)
    
while True:             # No stop in sight
    ans = input("Enter name, empty to list:")
    if ans == "":
        print_friends()
    else:
        my_friends.append(ans)  # Add to list
