# timestableN.py    19Aug2018
"""
Exercise: “Times Tables” for nval – 1xnval, 2xnval, …,nvalxnval
"""
inp = input("Enter multiplier:")

nval = int(inp)   # times value
first = 1
last = nval
n = first
while n <= last:
    print(n, "x ", nval, "= ", n*nval)
    n = n + 1

