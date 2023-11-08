#factors_from_to.py  06Dec2020  crs
"""
Print each number's factors on same line
+ Omit 1, and number as factors
+ Only print if we have at least one nontrivial factor
+ Using for loops
+ ask from, two
"""
import math

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

