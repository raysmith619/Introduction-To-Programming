#times_mn.py 17July2019  crs
""" 
times table printout using nested while
 m down
  |
  v
       1  2  3  4 ... n -> side ways
    1  1  2
    2  2  4
    3
    4
    
    
"""
from math import *
n_min = 1
n_max =12
m_min = n_min
m_max = n_max

m = m_min           # Initialise dowward numbers
while m <= m_max:
    n = n_min       # Initialize sideways numbers
    if m == m_min:  # put header before first line
        nh = n_min
        print("   ", end="")    # align header with sideways numbers
        while nh <= n_max:
            sp = "--"
            print(sp, nh, end=" ")
            nh += 1         # Increment side ways number
        print()
        print("   ", end="")    # align header with sideways numbers
        print(nh*3 * "-")
    print(m," ", end="")
    while n <= n_max:
        sp =""
        len_nm = int(log10(n*m))
        spnum = 3       # width alowed fo product
        sp =  (spnum-len_nm) * " "
        print(sp, n*m, sep="", end=" ")
        n += 1         # Increment side ways number
    print()         # end sideways line of nums
    m += 1          # Increment downward numbers
    
