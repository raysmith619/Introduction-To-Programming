# times_tables.py    23Aug2018
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
    inp = "5"   # Default is 5

max = int(inp)
first = 1
last = max
i = first
width = len(str(max*max)) + 1   # Room for largest plus a space
while i <= last:        # Vertical down page
    j = first
    while j <= last:    # Horizontal accross page
        prod = i*j
        prod_len = len(str(prod))
        print(" " * (width-prod_len), end = "")
        print(prod, end="")
        j = j + 1
    print("")           # End of line
    i = i + 1
    
