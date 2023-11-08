my_friends = [  "Ray Smith",  "Tony Soprano",  "Chris Kringle",  ]

while True:
    ans = input("Enter friend name:")
    if ans == "":  #if ans is empty
        ## put list code here - cut from above  for name in
        for name in my_friends:
            print(name)

    else:
        my_friends.append(ans)
