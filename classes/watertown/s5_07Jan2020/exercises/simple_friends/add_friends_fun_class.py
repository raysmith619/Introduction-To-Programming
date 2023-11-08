#add_friends_fun_class.py    01Dec2020  crs, From list_friends
# Simple List Example
"""
Add to list
Print list, if entry is empty
"""
# Initial list of friends names
my_friends = [
    "Ray Smith",
    "Phil Fontain",
    "Rich Parker",
    ]
def print_friends():
    for name in my_friends:
        print(name)

while True:             # No stop in sight
    ans = input("Enter name, empty to list:")
    if ans == "":
        print_friends()
    else:
        my_friends.append(ans)  # Add to list
