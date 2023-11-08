# sum_numbers_1_to_n.py 17Jul2018
"""
1. Tell the users you are going to sum numbers
2. Ask the user to enter the sum limit (Limit).
3. Sum the numbers whose sum is less than or equal to
   the Limit, listing the sum and the last number added.
"""
print("We are summing integers"
    + " from 1 to n")

inp = input("Please enter n: ")
n = int(inp)
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print("sum=", sum)