# times_tables_for_one.py   21Oct2018
# Prompt for number
# Then produce 1xN,... table
inp = input("Enter Number:")

num = int(inp)
first = 1
last = num
n = first
while n <= last:
    print(n, "x", num, "=", n*num)
    n = n + 1

