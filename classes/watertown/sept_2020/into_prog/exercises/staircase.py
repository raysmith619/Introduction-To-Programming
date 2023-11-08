# staircase.py  25-Jul-2018
# Write a function staircase(first_n, last_n) that returns the
# sum of the numbers first_n, first_n+1, …, last_n.  Test
# it on the following: 1,10; 1,100; 5, 10;  5,5; 10,1;
#
def staircase(first_n, last_n):
    """
    Sum the numbers from first_n to last_n inclusive
    """
    
    sum = 0
    for n in range(first_n, last_n+1):  # including last_n
        sum += n      # short hand for sum = sum + n
    return sum

def testit(first_n, last_n):
    """
    test our staircase function
    """
    print("staircase(", first_n, last_n, ") ",
          staircase(first_n, last_n))
testit(1,10)
testit(1,100)
testit(5, 10)
testit(10, 1)
