# first.py 2/14/2019
"""
Twenty question - number guessing
+ loop getting guesses

...
"""
import sys
while True:
    inp_str = input("Please enter guess: ")
    try:
        guess = int(inp_str)
    except:
        print("'int' doesn't like", inp_str, "as an argument")
        continue
    print("Number entered:", guess)
