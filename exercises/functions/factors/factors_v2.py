#factors_v2.py  06Dec2020  crs
"""
Print each number's factors on same line
+ ask, print n
+ print factors
+ separate factors with ", "
+ Omit factors 1,n
"""
inp = input("Enter top:")
ntop = int(inp)
n = 1
for n in range(1, ntop+1):
    nfac = 0                    # Track number of factors
    print(n, ": ", end="")
    for fac in range(2,n):    # 2 through n-1
        if n%fac == 0:
            if nfac > 0:
                print(", ", end="")
            print(fac, end="")
            nfac += 1
    print()             # End line
