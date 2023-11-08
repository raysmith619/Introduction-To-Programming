# iteration_multi_game_no_continue_break_no_len_check.py 11Feb2020
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
while True:     # Game loop
    target = random.randint(target_low, target_hi)
    continue_loop = True
    while continue_loop:
        inp = input("Enter Guess:")
        print("Number:", inp)
        guess = int(inp)    # Convert to integer
        if guess < target:
            print("Sorry your input of", guess, "is too low")
        else:
            if guess > target:
                print("Sorry your input of", guess, "is too high")
            else:
                if guess == target:
                    print("Congratulations", guess, "is the target")
                    continue_loop = False
    inp = input("Enter N to quit playing:")
    if inp.lower()[0] == "no"[0]:
        break
    
   
    

