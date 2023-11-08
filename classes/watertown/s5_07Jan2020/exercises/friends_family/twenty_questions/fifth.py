# fifth.py 17Jul2018
# Twenty questions
# loop asking number
# print number entered
#+
# Set target value
# Quit if number entered number equals target

#+
# Announce if guess greater, less or equal

#+
# Announce goals, rules before start

#+
# Ask user if they want to play again
intro = """
Welcome to our number guessing game
I've picked a number.
You can enter guesses and I'll let you know if your
guess is less than my number, greater than my number
or EXACTLY my number.
Please press the ENTER key after typing your guess.
"""
print(intro)
while True:                 # Loop over games
    target_value = 5
    while True:
        inp = input("Enter Number ")
        num = int(inp)
        print("Number:", num)
        if target_value > num:
            print("Sorry, my number is greater than", num)
            continue            # continue with loop
        if target_value < num:
            print("Sorry, my number is less than", num)
            continue            # continue with loop
        if num == target_value:
            print("You Got it - ", num, " is my number ")
            break
    ans = input("Want to play another game? y for yes, n for no ")
    
    if ans == "n" or ans == "N":
        print("Thanks for playing.  See you next time")
        break
    print("Then we'll play another")
