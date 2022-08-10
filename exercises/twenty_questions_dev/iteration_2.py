# iteration_2.py 21Jan2020 crs, from iteration_1.py
"""
Second iteration of twenty questions

 + Prompt user for number

 + Set up target, check for match
 Use integer values
"""

target = 15
while True:
    inp = input("Enter Guess:")
    print("Number:", inp)
    guess = int(inp)    # Convert to integer
    if guess == target:
        print("Congratulations", guess, "is the target")
        break

    
   
    

