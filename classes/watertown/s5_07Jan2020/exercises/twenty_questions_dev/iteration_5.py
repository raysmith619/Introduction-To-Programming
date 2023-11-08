# iteration_5.py 12Aug2020 crs
# first iteration of tq
# + Prompt user for number
#
# + Set up target, check for match
# Use integer values
#
# + Check / Report too high, low,..
#
# + Randomize the target
#
# + Add preamble with range
#
import random
target_hi = 20      # High end of target
###target_hi = 5       # TFD
target_low = 1      # LOW END OF TARGET
preamble = f"""
I'm thinking of a number between {target_low} and {target_hi}
Can you guess it?  Remember to press the ENTER key
to enter your guess.  Good Luck!
"""
print(preamble)
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
        print("Congratulations", guess, "is my number")
        break       # End this game
print("See you next time.")
