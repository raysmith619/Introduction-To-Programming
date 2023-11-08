# iteration_introduction.py 18Feb2020
# 3-4th adding random of tq
# + Prompt user for number
#
# + Set up target, check for match
# Use integer values
#
# + make target random
#
# + support multiple games
#
# + Include introduction
#
import random

target_low = 1      # lowest target
target_hi = 20      # highest
###target_hi = 5    # If we want to minimize our testing work
intro_str = f"""
I'm thinking of a number between {target_low} and {target_hi}
Please try to guess it.  I will let you know if your
guess is too high or two low.
"""
print(intro_str)
while True:
    target = random.randint(target_low, target_hi)
    while True:
        inp = input("Enter Guess:")
        print("Number:", inp)
        guess = int(inp)    # Convert to integer
        if guess < target:
            print("Sorry your input of", guess, "is too low")
            continue
        if guess > target:
            print("Sorry your input of", guess, "is too high")
            continue
        if guess == target:
            print("Congratulations", guess, "is the target")
            break
    inp = input("Enter N to quit playing:")
    if len(inp) > 0 and inp.lower()[0] == "no"[0]:
        break
    
   
    

