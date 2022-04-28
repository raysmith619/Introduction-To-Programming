#while_1.py     24Feb2022  crs
#Simple example of while loop
var = 1
limit = 5
print("BEFORE: var:", var, "limit:", limit)
while var < limit:
        print("    BODY: var:", var, "limit:", limit)
        var = var + 1
print("AFTER: var:", var, "limit:", limit)
