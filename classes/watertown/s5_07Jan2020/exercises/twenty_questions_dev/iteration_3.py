# iteration_3.py    23Sep2020, Correct top line name
#                   21Jan2020
# first iteration of tq
# + Prompt user for number
#
# + Set up target, check for match
# Use integer values
#
# + Tell user if too high or too low
#

target = 15
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

    
   
    

