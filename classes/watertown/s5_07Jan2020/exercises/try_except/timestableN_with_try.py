# timetableN_with_try.py 2/7/19
"""
Program to ask user for number and then do times table
for that number: 1 x num,..., num x num
Starting with timestable_NN.py - add check for valid integer.
Checking was done by using a "try - except" group.
If the code, indented after the "try:" gets an "exception", in our
case an illegal string in the "int" call, then the code indented
after the following "except:" gets executed.
See timestableN_out.txt for output from several runs of this program,
including one with illegal(noninteger) input.
"""

while True:
    inp = input("Please enter number: ")
    try:
        nval = int(inp)
    except:
        print("'int' doesn't like '", inp, "' as an argument")
        continue        # Ask again - continue the loop
    break               # We're OK - break out of the loop          

first = 1       # Start table at first x nval
last = nval     # Stop at nval x nval
inc = 1         # Do every numver 1 x, to last x             
n = first
while n<=nval:
    print(n,"x",nval,"=",n*nval) 
    n = n+inc

