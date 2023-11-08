#factors.py 01Nov2020  crs
""" Prompt usr for number
For numbers 1 to n print that number's factors
"""
inp = input("Enter number:")
num = int(inp)
for n in range(1, num+1):
    print(n, end=": ")
    for nn in range(2, n):      # Skip 1 and itself
        if n % nn == 0:
            print(nn, end=",")
    print()



