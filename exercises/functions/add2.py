#add2.py    03Aug2021  crs, Author
# Simple program to demonstrate functions

def add2(value1, value2):
    """
    Add value1 to value2, returning value1+value2
    """
    return value1 + value2

print("Testing add2")
sum = add2(1,2)
print("sum:",1,2," sum:", sum)

a = 1000
b = 2000
print("sum:", " a:", a, " b:", b, " sum:", add2(a,b))

r'''
Output:
>>> 
= RESTART: C:/Users/raysm/workspace/
python/IntroductionToProgramming/
exercises/functions/add2.py
Testing add2
sum: 1 2  sum: 3
sum:  a: 1000  b: 2000  sum: 3000
>>> 
'''
