#staircase.py   18Jul2018
"""
Write a function staircase(first_n, last_n)
"""
def staircase(first_n, last_n):
    sum = 0
    n = first_n
    while n <= last_n:
        sum = sum + n
        n = n + 1
    return sum

print("1,10 ==> ", staircase(1,10))
print("1,100 ==> ", staircase(1,100))
print("5,5 ==> ", staircase(5,5))
print("10,1 ==> ", staircase(10,1))
