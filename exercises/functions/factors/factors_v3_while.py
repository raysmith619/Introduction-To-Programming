#factors_v3_while.py  06Dec2020  crs
"""
Print each number's factors on same line
+ Omit 1, and number as factors
+ Only print if we have at least one nontrivial factor
"""
inp = input("Enter top:")
ntop = int(inp)
n = 2
while n  <= ntop:
    nfact = 2
    nf = 0     # number of factors so far
    while nfact < n:
        if n % nfact == 0:
            if nf == 0:
                print(n, ": ",sep = "", end="")               
            if nf > 0:
                print(", ", end="")
            print(nfact, end="")
            nf += 1     # short hand for nf = nf + 1
        nfact += 1      # Look at next
    if nf > 0:
        print()             # End line
    n += 1

r'''
Sample Ouput:
>>> 
= RESTART: C:\Users\raysm\workspace\python\
IntroductionToProgramming\exercises\
functions\factors\factors_v3.py
Enter top:15
4: 2
6: 2, 3
8: 2, 4
9: 3
10: 2, 5
12: 2, 3, 4, 6
14: 2, 7
15: 3, 5
>>>
'''
