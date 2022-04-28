#factors_v1_b.py  06Dec2020  crs
"""
Print each number's factors on same line
ask, print n
print factors
"""
inp = input("Enter top:")
ntop = int(inp)
for n in range(1, ntop+1):
    print(n, ": ", end="")
    for fac in range(1,n+1):    # 1 through n
        if n%fac == 0:
            print(fac, end=",")
    print()             # End line
