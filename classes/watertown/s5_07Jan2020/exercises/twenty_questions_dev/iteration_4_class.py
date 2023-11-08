# iteration_4_class.py 08Dec2020  crs  from iteration_3
"""
first iteration of twenty questions
 + Prompt user for number

 + Set up target, check for match
 Use integer values
 + Check if guess is greater than or less than target
 + Set the target to a random number
"""

import random
target_min = 1     # Minimum target
target_max = 20    # Maximum target
###target_max = 5     # TFD - temporary for debugging
print("Target is between:", target_min, "and", target_max)
target = random.randint(target_min, target_max)
while True:
    inp = input("Enter Guess:")
    print("Number:", inp)
    guess = int(inp)    # Convert to integer
    if guess == target:
        print("Congratulations", guess, "is the target")
        break
    if guess < target:
        print("The guess:", guess, " is less")
        continue
    if guess > target:
        print("The guess:", guess, " is too great")
        continue
    

    
   
    

