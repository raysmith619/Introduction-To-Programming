#add_friends.py    23Sep2020  crs, From list_friends
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

while True:             # No stop in sight
    ans = input("Enter name, empty to list:")
    if ans == "":
        # Simple loop to print out names from list
        for name in my_friends:
            print(name)
    else:
        my_friends.append(ans)  # Add to list
