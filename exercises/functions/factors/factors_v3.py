#factors_v3.py  12Jan2022  crs
"""
Print each number's factors on same line
+ ask, print n
+ print factors
+ separate factors with ", "
+ Omit factors 1,n
+ Only print numbers which have one nontrivial factor
"""
inp = input("Enter top:")
ntop = int(inp)
n = 1
for n in range(1, ntop+1):
    nfac = 0                    # Track number of factors
    for fac in range(2,n):    # 2 through n-1
        if n%fac == 0:
            if nfac == 0:
                print(n, ": ", end="")  # we got one
            if nfac > 0:
                print(", ", end="")
            print(fac, end="")
            nfac += 1
    if nfac > 0:
        print()             # End line
