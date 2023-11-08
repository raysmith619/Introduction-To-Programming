# product.py
"""
Write a function product(factor1, factor2, factor3) that returns the
product of the values factor1, factor2, factor3.
Test it on the following:
    .5, .4, .3;
    1, 2, 3;
    -1, -1, -1;
"""
def product(factor1, factor2, factor3):
    """ Do product of 3 factors, returning the product
    :factor1, factor2, factor3: factors
    :returns: factor1*factor2*factor3
    """
    prod = factor1*factor2*factor3
    return prod


def testit(f1,f2,f3):
    """ Test / Exercise product
    """
    prod = product(f1,f2,f3)
    print("testing prod(", f1,f2,f3, ") = ", prod)


testit(.5,.4,.3)
testit(1,2,3)
testit(-1,-1,-1)
