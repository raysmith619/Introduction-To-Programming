# print_keywords.py 08Aug2021  crs, Author
# Showing builtin function print with keywords
print("\nTesting end keyword")
print("All-", end= "")
print("on-", end= "")
print("one-", end= "")
print("line-", end="\nCan be any string\n")

print("\nTesting sep keyword")
print("Using","our","separator", sep=":", end="+THE END+")

"""
Sample Output:
>>> 
= RESTART: C:/Users\raysm\workspace\python
\IntroductionToProgramming\exercises\
functions\print_keywords.py

Testing end keyword
All-on-one-line-
Can be any string

Testing sep keyword
Using:our:separator+THE END+
>>>
"""
