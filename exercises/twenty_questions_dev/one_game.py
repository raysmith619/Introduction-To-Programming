# one_game.py  crs, Author
"""
Play one game subroutine(function)
"""

import random
def one_game(target_low=1, target_hi=20):
    """ Play one game
    :target_low: low end of target
    :target_hi: High end of target
    """
    target = random.randint(target_low, target_hi)
    while True:
        inp = input(f"Enter Guess ({target_low} and {target_hi}):")
        print("Number:", inp)
        try:
            guess = int(inp)    # Convert to integer
        except:
            print(f"I don't recognize '{inp}' as a number"
                  " please try again.")
            continue
        if guess < target:
            print("Sorry your input of", guess, "is too low.")
            continue
        if guess > target:
            print("Sorry your input of", guess, "is too high.")
            continue
        if guess == target:
            print("Congratulations", guess, "is my number!")
            break       # End this game

if __name__ == "__main__":
    target_hi = 5    # TFD
    while True:
        one_game(target_hi=target_hi)
        print("Play a new game?")
        inp = input("Enter N to quit: ")
        if inp == "N" or inp == "n":
            break
    print("See you next time.")
