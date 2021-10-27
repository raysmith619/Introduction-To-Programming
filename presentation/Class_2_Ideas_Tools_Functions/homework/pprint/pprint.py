# pprint.py 04-Aug-2021  crs, Author
"""
print function but does something
"special" for us, for example,
precede the printed text with an
optional prefix.
Note this is a simple version with only
one arg.  One can make a more general
version to handle an arbitrary number of
args.
"""
def pprint(arg, end=None, sep=None,
           prefix=None):
    """
    print arg, but adds prefix if present
    :arg: argument to print
    :end: print's end arg
    :sep: print's sep arg
    :prefix: optional prefix
            default: no prefix
    """
    if prefix is not None:
        print(prefix, end="", sep=sep)  # Supress newline
    print(arg, end=end, sep=sep)
# Self test, not using if __name__ == '__main__'
print("Test pprint")
arg = "Our String"
print("\nTesting no prefix:", "arg:", arg)
pprint(arg)

prefix = "PREFIX:"
print("\nTesting with prefix: arg:", arg, " prefix:", prefix)
pprint(arg, prefix=prefix)

print("\nTesting with variable prefix:")
for i in range(7):
    pprint("Increasing prefix", prefix='='*i)
