# times_tables_simple_for.py    23Aug2018
"""
Display a times-table suitable for grade school review
Request and accept limit from user.
Example for 5:
    1   2   3   4   5
    2   2   6   8  10
    3   6   8  12  15    
    4   8  12  16  20
    5  10  15  20  25
"""
inp = input("Enter times table length: ")
if inp == "":
    inp = "5"       # Default is 5

max = int(inp)
first = 1
last = max

for i in range(first, last+1):        # Vertical down page
    for j in range(first, last+1):    # Horizontal across page
        print(" ", i*j, end="")
    print("")           # End of line
    