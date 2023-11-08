# mult_table_unformatted.py 03Feb2020
"""
Provide a nonformatted(not necessarily alligned) table
 n down (rows)
 m side (columns)
"""
def get_in(prompt=None, default=None):
    """ get input, empty = default value
    :prompt: optional text prompt
    :default: default returned if NEWLINE
    :returns: integer value, default if NEWLINE
    """
    if prompt is not None and default is not None:
        prompt = f"{prompt}[{default}]: "
    inp = input(prompt)
    if inp == "":
        return default
    return int(inp)
            
nmin = get_in("nmin", 1)
nmax = get_in("nmax", nmin+5)
mmin = get_in("mmin", nmin)   # default to nmin
mmax = get_in("mmax", nmax)
print(f"table {nmin} to {nmax} by {mmin} to {mmax}")
for n in range(nmin, nmax+1):
    for m in range(mmin, mmax+1):
        prod = n * m
        print(f"{prod}", end= " ")
    print()     # End of line
print()         # End of table
