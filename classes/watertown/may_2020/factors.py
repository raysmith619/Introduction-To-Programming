#factors.py
"""
Print each number's factors on same line
"""
inp = input("Enter top:")
ntop = int(inp)
n = 1
while n  <= ntop:
    print(n, ": ",sep = "", end="")
    nfact = 1  # Candidate factor
    nf = 0     # number of factors so far
    while nfact <= n:
        if n % nfact == 0:  # Check if nfact is a factor of n
            if (nf > 0):
                print(", ", end="")
            print(nfact, end="")
            nf += 1     # short hand for nf = nf + 1
        nfact += 1      # Look at next
    print()             # End line
    n += 1

