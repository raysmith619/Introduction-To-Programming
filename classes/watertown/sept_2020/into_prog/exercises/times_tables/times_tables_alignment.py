# times_tables_alignment.py    21Oct2019
"""
Display a times-table suitable for grade school review
Leave fancy row and column headings for later.
Allow a range first...last
Place table generation in a function to facilitate
repetitive use
Pad number printing to align output.
Request and accept limit from user.
Example for  3 to 5:
        3   4   5
       --  --  --
    3   9  12  15
    4  12  16  20
    5  15  20  25
    
    Headings are left for later.
"""
import sys      # system functions such as exit()
import math     # Math functions like log10

def times_table():
    """ Do whole input, and print in table
    :returns: False to quit
    """
    
    inp = input("Enter to,from [3,5] ( - q to quit): ")
    if inp == "":
        inp = "5,3"       # Default is 5 from 3
    elif inp.lower() == "q":
        return False
    
    inputs = inp.split(',')
    if len(inputs) < 2:
        inputs.append("1")      # Default start is 1
    
    max = int(inputs[0])
    min = int(inputs[1])
    
    first = min
    last = max
    if last < first:
        print("last({:d}) is less than first({:d}".format(last, first))
        sys.exit()
    maxprod = last*last 
    maxlength = int(math.log10(maxprod)+1)  # add 1 to round up
        
    for i in range(first, last+1):        # Vertical down page
        for j in range(first, last+1):    # Horizontal across page
            product = i*j 
            prod_len = int(math.log10(product)+1)
            pad_len = maxlength - prod_len
            print(" "*pad_len, product, end="")
        print("")           # End of line
    
    return True     # Successful - continue

"""
Continue till quit
"""

while True:
    if not times_table():
        print("quitting now")
        break
