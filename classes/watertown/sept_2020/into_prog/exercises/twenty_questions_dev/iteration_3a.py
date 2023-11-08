# iteration_3a.py 28Jan2020 crs
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
import random
target_hi = 20    # High end of target
target_low = 1    # LOW END OF TARGET
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

    
   
    

