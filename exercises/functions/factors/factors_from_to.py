#factors_from_to.py  07Dec2020  crs
"""
Print each number's factors on same line
+ Omit 1, and number as factors
+ Only print if we have at least one nontrivial factor
+ Using for loops
+ ask from, to
"""
inp = input("Enter from[2]:")
if inp == "":
    nfrom = 2      # Default[ENTER]
else:
    nfrom = int(inp)
deftop = nfrom + 9
inp = input(f"Enter top[{deftop}]:")
if inp == "":
    ntop = deftop      # Default[ENTER]
else:
    ntop = int(inp)
n = 2
for n in range(nfrom, ntop+1):
    nf = 0     # number of factors so far
    for nfact in range(2, n):   # don't include 1 or n
        if n % nfact == 0:
            if nf == 0:
                print(n, ": ",sep = "", end="")               
            else:
                print(", ", end="")
            print(nfact, end="")
            nf += 1     # short hand for nf = nf + 1
    if nf > 0:
        print()             # End line

r'''
Sample output:
>>> 
= RESTART: C:\Users\raysm\workspace\python\
IntroductionToProgramming\exercises\
functions\factors\factors_from_to.py
Enter from[2]:9699691
Enter top[9699700]:9699694
9699691: 347, 27953
9699692: 2, 4, 109, 218, 436, 22247,
        44494, 88988, 2424923, 4849846
9699693: 3, 3233231
9699694: 2, 113, 167, 226, 257, 334,
        514, 18871, 29041, 37742,
        42919, 58082, 85838, 4849847
>>> 
'''
