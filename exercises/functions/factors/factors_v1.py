#factors_v1.py  06Dec2020  crs
"""
Print each number's factors on same line
"""
inp = input("Enter top:")
ntop = int(inp)
n = 1
while n  <= ntop:
    print(n, ": ",sep = "", end="")
    nfact = 1  # Candidate factor
    nf = 0     # number of factors so far
    while nfact <= n:
        if n % nfact == 0:  # Check if nfact is a factor of n
            if (nf > 0):
                print(", ", end="")
            print(nfact, end="")
            nf += 1     # short hand for nf = nf + 1
        nfact += 1      # Look at next
    print()             # End line
    n += 1

r''' r avoids potential problems with '\' character
Sample output:
>>> 
= RESTART: C:\Users\raysm\workspace\python\
IntroductionToProgramming\exercises\
functions\factors\factors_v1.py
Enter top:15
1: 1
2: 1, 2
3: 1, 3
4: 1, 2, 4
5: 1, 5
6: 1, 2, 3, 6
7: 1, 7
8: 1, 2, 4, 8
9: 1, 3, 9
10: 1, 2, 5, 10
11: 1, 11
12: 1, 2, 3, 4, 6, 12
13: 1, 13
14: 1, 2, 7, 14
15: 1, 3, 5, 15
>>>
'''
