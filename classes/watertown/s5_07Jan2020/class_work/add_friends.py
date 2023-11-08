#add_friends.py 24Sep2020  crs, Adapted from list_friends.py
"""
Friends - Simple List Example
Add names to list, print if entry is empty
"""
my_friends = [
    "Ray Smith",
    "Tony Suprano",
    "Chris Kringle",
    ]
    
while True:
    ans = input("Enter friend:")
    if ans == "":
        for name in my_friends:
            print(name)
            break
    else:
        my_friends.append(ans)

       
