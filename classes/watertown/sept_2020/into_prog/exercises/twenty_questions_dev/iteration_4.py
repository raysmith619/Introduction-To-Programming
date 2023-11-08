# iteration_4.py 28Jan2020 crs
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
# + Facilitate multiple games
#
import random
target_hi = 20      # High end of target
###target_hi = 5       # TFD
target_low = 1      # LOW END OF TARGET
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
            break       # End this game

    print("Play a new game?")
    inp = input("Enter N to quit: ")
    if inp == "N" or inp == "n":
        break
print("See you next time.")
