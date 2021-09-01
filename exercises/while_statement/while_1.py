#while_1.py
var = 1
limit = 5
print("BEFORE: var:", var, "limit:", limit)
while var < limit:
	print("    BODY: var:", var, "limit:", limit)
	var = var + 1
print("AFTER: var:", var, "limit:", limit)

"""
Output:
>>> 
= RESTART: C:\Users\raysm\workspace\python\
IntroductionToProgramming\exercises\
while_statement\while_1.py
BEFORE: var: 1 limit: 5
    BODY: var: 1 limit: 5
    BODY: var: 2 limit: 5
    BODY: var: 3 limit: 5
    BODY: var: 4 limit: 5
AFTER: var: 5 limit: 5
>>> 
"""
