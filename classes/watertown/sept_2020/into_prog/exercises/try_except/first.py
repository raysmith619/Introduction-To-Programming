# first.py 2/14/2019
"""
Twenty question - number guessing
+ loop getting guesses

...
"""
while True:
    inp_str = input("Please enter guess: ")
    guess = int(inp_str)        # Convert string to internal integer
    print("Number entered:", guess)
