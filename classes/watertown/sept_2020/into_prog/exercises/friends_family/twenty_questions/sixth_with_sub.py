# sixth_with_sub.py 12Nov2018
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

#+
# Set the target to a random number

#+ Make one game into a subroutine
def tq_game(target_value):
    """ Plays one game
    :target_value: my value to guess
    """
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
 


import random           # Bring in python support for random numbers

target_min = 1
target_max = 20
intro1 = """
Welcome to our number guessing game
I've picked a number between
"""
intro2 = """ and """

intro3 = """
You can enter guesses and I'll let you know if your
guess is less than my number, greater than my number
or EXACTLY my number.
Please press the ENTER key after typing your guess.
"""
print(intro1, target_min, intro2, target_max, intro3)
while True:                 # Loop over games
    target_value = random.randint(target_min, target_max) # Include max
    tq_game(target_value)
    ans = input("Want to play another game? y for yes, n for no ")
    if ans == "n" or ans == "N":
        print("Thanks for playing!  See you next time.")
        break

