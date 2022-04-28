#factors_v1_a.py  06Dec2020  crs
"""
Print each number's factors on same line
just ask, print n
"""
inp = input("Enter top:")
ntop = int(inp)
for n in range(1,ntop+1):
    print(n, ": ",sep = "", end="")
    print()             # End line
