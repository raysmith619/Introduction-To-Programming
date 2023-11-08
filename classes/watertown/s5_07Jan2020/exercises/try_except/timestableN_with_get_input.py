# timetableN_with_get_input.py 03Feb2020
"""
Program to ask user for number and then do times table
for that number: 1 x num,..., num x num
Use get_int from get_input.py to 
"""
from get_input import get_int
nval = get_int("Please enter number: ")

first = 1       # Start table at first x nval
last = nval     # Stop at nval x nval
inc = 1         # Do every numver 1 x, to last x             
n = first
while n<=nval:
    print(n,"x",nval,"=",n*nval) 
    n = n+inc

