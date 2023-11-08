# times_tables_function.py    21Oct2019
"""
Display a times-table suitable for grade school review
Allow a range first...last
Place table generation in a function to facilitate
repetitive use
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

def times_table():
    """ Do whole input, and print in table
    :returns: False to quit
    """
    
    inp = input("Enter to,from [5,3] ( - q to quit): ")
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
        
    for i in range(first, last+1):        # Vertical down page
        for j in range(first, last+1):    # Horizontal across page
            print(" ", i*j, end="")
        print("")           # End of line
    
    return True     # Successful - continue

"""
Continue till quit
"""

while True:
    if not times_table():
        print("quitting now")
        break
