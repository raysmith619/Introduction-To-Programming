#second.py   11Jun2020  crs, adapted from first
"""
Twenty Questions
+
Just loop prompting user for guess, print out number
+

"""
target = 20
while True:
    inp = input("Enter Guess: ")
    guess = int(inp)
    print("Guess:", guess)
    if guess == target:
        print("Guess(", guess, ") equals target(", target, ") - Congrats!")
        break
    
    
