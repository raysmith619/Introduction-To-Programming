#factors_v1_a_while.py  06Dec2020  crs
"""
Print each number's factors on same line
just ask, print n
"""
inp = input("Enter top:")
ntop = int(inp)
n = 1
while n  <= ntop:
    print(n, ": ",sep = "", end="")
    print()             # End line
    n += 1
