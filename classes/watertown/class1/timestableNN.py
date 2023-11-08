# timestableNN.py    19Aug2018
"""
Exercise: “Times Tables” for 13 – 1x13, 2x13, …,13x13
"""
nval = 13   # times value
first = 1
last = nval
n = first
while n <= last:
    print(n, "x ", nval, "= ", n*nval)
    n = n + 1

