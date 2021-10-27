#print_odd_1to9.py 15Sep2021  crs, Review
# Demonstrate test while and for loop
print("\nTesting while loop printing odd numbers")
start = 1
end = 10+1
n = start
while n < end:
    if n % 2 == 1:
        print("n:", n)
    n = n + 1
    
print("\nTesting for loop printing odd numbers")
start = 1
end = 10+1
for n in range(start, end):
    if n % 2 == 1:
        print("n:", n)
    
