# product.py    25-Jul-2018
# Write a function product(factor1, factor2, factor3) that returns
# the product of the values factor1, factor2, factor3.
# Test it on the following: .5, .4, .3; 1, 2, 3; -1, -1, -1;
#
def product(factor1, factor2, factor3):
    return factor1*factor2*factor3

def testit(factor1, factor2, factor3):
    """
    test our product function, providing 3 factors
    """
    result = product(factor1, factor2, factor3)
    print("product(", factor1, factor2, factor3, ") ", result)

testit(.5, .4, .3)
testit(1, 2, 3)
testit(-1, -1, -1)
