# timetableN.py 2/7/19
"""
Program to ask user for number and then do times table
for that number: 1 x num,..., num x num
...
"""
inp = input("Please enter number: ")
nval = int(inp)
first = 1       # Start table at first x nval
last = nval     # Stop at nval x nval
inc = 1         # Do every numver 1 x, to last x             
n = first
while n<=nval:
    print(n,"x",nval,"=",n*nval) 
    n = n+inc


"""
Please enter number: 5
1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25
>>> 
 RESTART: C:\Users\raysm\workspace\python\IntroductionToProgramming\class3b\timestableN.py 
Please enter number: 3
1 x 3 = 3
2 x 3 = 6
3 x 3 = 9

"""

