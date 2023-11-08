# iteration_3_class.py 08Dec2020  crs  from iteration_2
"""
first iteration of twenty questions
 + Prompt user for number

 + Set up target, check for match
 Use integer values
 + Check if guess is greater than or less than target
"""

target = 15
while True:
    inp = input("Enter Guess:")
    print("Number:", inp)
    guess = int(inp)    # Convert to integer
    if guess == target:
        print("Congratulations", guess, "is the target")
        break
    if guess < target:
        print("The guess:", guess, " is less")
        continue
    if guess > target:
        print("The guess:", guess, " is too great")
        continue
    

    
   
    

