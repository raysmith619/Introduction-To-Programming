# iteration_2.py 21Jan2020
# first iteration of tq
# + Prompt user for number
#
# + Set up target, check for match
# Use integer values
#
# +

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

    
   
    

