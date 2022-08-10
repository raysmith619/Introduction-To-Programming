#list_range_limit.py  23Jul2022  crs
# Use range, making limit a variable
# range(start, end) – start,…,end-1
#range(end) – 0,…,n-1
limit = 9
print("limit:", limit)
print("for n in range(1,",limit,"):")
for n in range(1,limit):	# 1 to limit-1
    print("n:", n)

print("for n in range(",limit,"):")
for n in range(limit):	# 0-9
    print("n:", n)

print("for n in range(2,",limit,",3):")
for n in range(2,limit,3):	# 2 by 3 to before limit 
    print("n:", n)
