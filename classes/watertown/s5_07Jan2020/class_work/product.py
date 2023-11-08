#product.py 01Nov2020  crs, Author
"""
Special Product Function
Test Cases: .5, .4, .3; 1, 2, 3; -1, -1, -1;
"""
def product(factor1, factor2, factor3):
    """ Return product of 3 factors
    """
    return factor1*factor2*factor3

print(".5,.4,.3:", product(.5,.4,.3))
print("1,2,3:", product(1,2,3))
print("-1, -1, -1:", product(-1, -1, -1))
