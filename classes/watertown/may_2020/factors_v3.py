#factors_v3.py  06Dec2020  crs
"""
Print each number's factors on same line
+
Omit 1, and number as factors
Only print if we have at least one nontrivial factor
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

