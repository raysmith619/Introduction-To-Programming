# iteration_2_class_2.py 21Jan2020
# second iteration of twenty questions
"""
   Prompt user for number

 + Set target value
   Quit if number entered number
   equals target

"""
target = 15     # Guessing target

while True:
    inp = input("Enter Guess:")
    print("Number:", inp)
    guess = int(inp)    # Convert to integer
    if guess == target:
        print(guess, " is the target")
        print("Bye! Thanks for playing!")
        break
        
   
    

