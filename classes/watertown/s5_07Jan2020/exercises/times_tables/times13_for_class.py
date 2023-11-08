#times13_for_class.py crs 29Dec2020  from times13.py

#times table....
# Using for, range()
nval = 13      # number to multiply
first = 1
last = nval

n = first    # begin at lowest value
for n in range(first, last+1):  # do first...last
    print(n, "x", nval, n*nval)
    n = n + 1
# How / when would for or while be a better choice?

