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
    ans = input("Enter name[list all]:")
    if ans == "":
        print_friends()
    else:
        my_friends.append(ans)  # Add to list

r'''
Output:
= RESTART: C:\Users\raysm\workspace\python\
IntroductionToProgramming\exercises\functions\
friends_family\simple_friends\add_friends_fun.py
Enter name[list all]:
Ray Smith
Phil Fontain
Rich Parker
Enter name[list all]:tom
Enter name[list all]:jo
Enter name[list all]:egor
Enter name[list all]:
Ray Smith
Phil Fontain
Rich Parker
tom
jo
egor
Enter name[list all]:
'''
