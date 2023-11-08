# iteration_7.py 12Aug2020 crs
"""
first iteration of tq
+ Prompt user for number

+ Set up target, check for match
Use integer values

+ Check / Report too high, low,..

+ Randomize the target

+ Add preamble with range

+ Add multiple game support

+ Protect against typos - ask again
"""

import random
target_hi = 20      # High end of target
target_hi = 30      # High end of target
###target_hi = 5    # TFD
target_low = 1      # LOW END OF TARGET
preamble = f"""
I'm thinking of a number between {target_low} and {target_hi}
Can you guess it?  Remember to press the ENTER key
to enter your guess.  Good Luck!
"""
print(preamble)
while True:
    target = random.randint(target_low, target_hi)
    while True:
        inp = input(f"Enter Guess ({target_low} and {target_hi}):")
        print("Number:", inp)
        try:
            guess = int(inp)    # Convert to integer
        except:
            print(f"I don't recognize '{inp}' as a number"
                  " please try again.")
            continue
        if guess < target:
            print("Sorry your input of", guess, "is too low.")
            continue
        if guess > target:
            print("Sorry your input of", guess, "is too high.")
            continue
        if guess == target:
            print("Congratulations", guess, "is my number!")
            break       # End this game

    print("Play a new game?")
    inp = input("Enter N to quit: ")
    if inp == "N" or inp == "n":
        break
print("See you next time.")
