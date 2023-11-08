# iteration_multi_game.py 11Feb2020
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
import random

target_low = 1      # lowest target
target_hi = 20      # highest
target_hi = 5
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
    
   
    

