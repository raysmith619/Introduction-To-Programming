#factors_v2_with_while.py  06Dec2020 crs
"""
Print each number's factors on same line
+ Omit 1, and number as factors
"""
inp = input("Enter top:")
ntop = int(inp)
n = 2
while n  <= ntop:
    print(n, ": ",sep = "", end="")
    nfact = 2
    nf = 0     # number of factors so far
    while nfact < n:
        if n % nfact == 0:
            if (nf > 0):
                print(", ", end="")
            print(nfact, end="")
            nf += 1     # short hand for nf = nf + 1
        nfact += 1      # Look at next
    print()             # End line
    n += 1

r'''
Sample output:
>>> 
= RESTART: C:\Users\raysm\workspace\python\IntroductionToProgramming\exercises\functions\factors\factors_v2.py
Enter top:15
2: 
3: 
4: 2
5: 
6: 2, 3
7: 
8: 2, 4
9: 3
10: 2, 5
11: 
12: 2, 3, 4, 6
13: 
14: 2, 7
15: 3, 5
>>>
'''
