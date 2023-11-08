# mult_table_formatted.py 03Feb2020
"""
Provide a formatted(alligned) table
 n down (rows)
 m side (columns)
      1  2  3  4
    + -- -- -- --
   1|  1  2  3  4
   2|  2  4  6  8
"""
def get_in(prompt=None, default=None):
    """ get input, empty = default value
    :prompt: optional text prompt
    :default: default(MUST be integer) returned if NEWLINE
    :returns: integer value, default if NEWLINE
    """
    while True:
        if prompt is not None and default is not None:
            prompt = f"{prompt}[{default}]: "
        inp = input(prompt)
        if inp == "":
            return default
                
        try:
            num = int(inp)
            return num
        except:
            print(f"'{inp}' is not an integer - please try again")
            
nmin = get_in("nmin", 1)
nmax = get_in("nmax", nmin+5)
mmin = get_in("mmin", nmin)   # default to nmin
mmax = get_in("mmax", nmax)
print(f"table {nmin} to {nmax} by {mmin} to {mmax}")
max_len = max(len(str(nmax*mmax)),len(str(nmin*nmax)),len(str(nmax*mmin)),
              len(str(nmin*mmin)))
for n in range(nmin, nmax+1):
    for m in range(mmin, mmax+1):
        prod = n * m
        print(f"{prod:{max_len}}", end= " ")
    print()     # End of line
print()         # End of table

        
"""
Output in mult_table_formatted.out
"""
