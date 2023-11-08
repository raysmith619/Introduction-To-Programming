# sum_numbers_sums_less_than_sum.py 17Jul2018
"""
1. Tell the users you are going to sum numbers
2. Ask the user to enter the sum limit (Limit).
3. Sum the numbers whose sum is less than or equal to
   the Limit, listing the sum and the last number added.
"""
print("We are summing integers"
    + " whose sum is less than"
    + " or equal to sum")

inp = input("Please enter sum: ")
sum_limit = int(inp)
sum = 0
last_n = 0
n = 1
while True:
    next_sum = sum + n
    if next_sum > sum_limit:
        break       # Next is past(or equal) limit
    sum = next_sum
    last_n = n
    n = n + 1
print("sum=", sum, " last n: ", last_n)