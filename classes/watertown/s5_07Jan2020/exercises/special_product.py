#special_product.py  18Jul2018
"""
Exercise - Special product
Write a function product(factor1, factor2, factor3)
that returns the product of the values factor1, factor2, factor3.
Test it on the following: .5, .4, .3; 1, 2, 3; -1, -1, -1;
"""
def product(factor1, factor2, factor3):
    return factor1 * factor2 * factor3

print(".5,.4,.3 ==> ", product(.5,.4,.3))

prod = product(1,2,3)
print("1,2,3 ==> ", prod)

p1 = -1
p2 = -1
p3 = -1
prod = product(p1, p2, p3)
print(p1,",", p2,",", p3, " ==> ", prod)