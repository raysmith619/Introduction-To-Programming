# iteration_2_class.py 01Dec2020 crs  from iteration_1.py
"""
    + first iteration of twenty questions
        Prompt user for number
    + set target value
      Quit if number entered equals target
"""

target = 10
while True:
    inp = input("Enter Guess:")
    print("Number:", inp)
    guess = int(inp)
    if guess == target:
        print("guess:", guess, "matches the target")
        break
    
   
    

