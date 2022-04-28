#add_friends_fun.py    20Sep2022  crs, simple add to list
"""
Add to list, else print list
  Loop
     1. prompt for name
     2. if "" print whole list
     3. else add input to list
"""
my_friends = []     # list of my friends' names
while True:
    inp = input("Enter name[list all]")
    name = inp
    if inp == "":
        for name in my_friends:
            print(name)
    elif inp.upper()  == "BYE":
        print("Quitting")
        break
    else:
        my_friends.append(name)
        
