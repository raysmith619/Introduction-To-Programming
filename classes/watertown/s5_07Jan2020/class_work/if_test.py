#if_test.py 24Sep2020 crs

a=2
if a > 1:
    print("a:", a, "a >1")
    
a= 1
if a > 1:
    print("a:", a, "a >1")
else:
    print("a:", a, "a > 1 else")

    
a= -2
if a > 1:
    print("a:", a, "a >1")
elif a == 0:
    print("a:", a, "a > 1 elif a==0")
elif a == -1:
    print("a:", a, "a > 1 elif a==-1")
elif a == -2:
    print("a:", a, "a > 1 elif a==-2")
else:
    print("a:", a, "a > 1 else")
    
a= -3
if a > 1:
    print("a:", a, "a >1")
elif a == 0:
    print("a:", a, "a > 1 elif a==0")
elif a == -1:
    print("a:", a, "a > 1 elif a==-1")
elif a == -2:
    print("a:", a, "a > 1 elif a==-2")
else:
    print("a:", a, "a > 1 else")
