# divisible_1_to_n.py 17Jul2018
"""
2.    List the numbers from 1 to 50, that are evenly divisible by 2, 3, 4, and 5.
Hint: I found the following by an Internet search for
python evenly divisible
n % k == 0
evaluates true if and only if n is an exact multiple of k.
In elementary math this is known as the remainder from a division.

"""
print("We checking for divisible by 2, 3, 4, and 5"
    + " from 1 to n")

inp = input("Please enter n: ")
n = int(inp)
sum = 0
i = 1
while i <= n:
    ival = i                # Save for checking
    i = i + 1               # Increase for next loop
    if ival % 2 != 0:
        continue            # not divisible - go to next
    if ival % 3 != 0:
        continue            # not divisible - go to next
    if ival % 4 != 0:
        continue            # not divisible - go to next
    if ival % 5 != 0:
        continue            # not divisible - go to next

    print(ival)
