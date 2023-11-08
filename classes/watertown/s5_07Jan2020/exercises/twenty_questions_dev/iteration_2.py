# iteration_2.py 21Jan2020
# first iteration of twenty questions
# + Prompt user for number
#
# + Set up target, check for match
# Use integer values

target = 15
while True:
    inp = input("Enter Guess:")
    print("Number:", inp)
    guess = int(inp)    # Convert to integer
    if guess == target:
        print("Congratulations", guess, "the target")
        break

    
   
    

