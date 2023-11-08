# first_try.py 2/14/2019
"""
Twenty question - number guessing
+ loop getting guesses

...
"""
while True:
    inp_str = input("Please enter guess: ")
    try:
        guess = int(inp_str)
    except:
        print(inp_str, "is not a number, please try again")
        continue
    print("Number entered:", guess)
