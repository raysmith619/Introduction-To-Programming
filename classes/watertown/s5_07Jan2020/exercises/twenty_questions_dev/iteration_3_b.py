# iteration_3_b.py 24Sep2020  Ray
# first iteration of twenty questions
# + Prompt user for number
#
# + Set up target, check for match
# Use integer values
#
# + Add Say if greater, less or equal

target = 15
while True:
    inp = input("Enter Guess:")
    print("Number:", inp)
    guess = int(inp)    # Convert to integer
    if guess < target:
        print("Sorry your guess is less than my value")
        continue
    if guess > target:
        print("Sorry your guess is greater than the target")
        continue
    if guess == target:
        print("Congratulations", guess, "is the target")
        break

    
   
    

