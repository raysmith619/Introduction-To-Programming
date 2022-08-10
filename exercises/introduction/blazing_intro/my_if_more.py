# my_if_more.py    27Dec2021  crs - exercise if statement

print("my_if_more")
i = 1
max = 7
while i < max:
    if i % 2 == 0:
        print("i(", i, ") is even ")
    else:
        print("i(", i, ") is odd ")
    if i % 3 == 0:
        print("i(", i, ") is divisible by 3 ")
    elif i % 4 == 0:
        print("i(", i, ") is divisible by 4 ")
    elif i % 5 == 0:
        print("i(", i, ") is divisible by 5 ")
    else:
        print("i(", i, ") is not divisible by 3,4, or 5 ")
        
        
    i = i + 1
