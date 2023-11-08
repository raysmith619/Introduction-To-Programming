#factors_v3_for.py  06Dec2020  crs
"""
Print each number's factors on same line
+ Omit 1, and number as factors
+ Only print if we have at least one nontrivial factor
+ Using for loops
"""
inp = input("Enter top:")
ntop = int(inp)
for n in range(2, ntop+1):
    nfact = 2
    nf = 0     # number of factors so far
    for nfact in range(2, n):
        if n % nfact == 0:
            if nf == 0:
                print(n, ": ",sep = "", end="")               
            else:
                print(", ", end="")
            print(nfact, end="")
            nf += 1     # short hand for nf = nf + 1
    if nf > 0:
        print()             # End line

