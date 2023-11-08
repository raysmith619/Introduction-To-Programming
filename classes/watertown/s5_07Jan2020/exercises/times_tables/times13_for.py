#times13_for.py crs 29Dec2020  From times13.py

#times table....
# Using a for statement
nval = 13      # number to multiply
first = 1
last = nval

for n in range(first, last+1):
    print(n, "x", nval, n*nval)
    n = n + 1

# 
# How is this a better choice than while?

