# iteration_7_change_hi.py  crs, From iteration _7.py
"""
Show use of subroutine for game
Support changing hi guess limit
+ Prompt user for number

+ Set up target, check for match
Use integer values

+ Check / Report too high, low,..

+ Randomize the target

+ Add preamble with range

+ Add multiple game support

+ Protect against typos - ask again
"""
from one_game import *
target_low = 1
target_hi = 30
target_hi = 5    # TFD
    
preamble = f"""
I'm thinking of a number between {target_low} and {target_hi}
Can you guess it?  Remember to press the ENTER key
to enter your guess.  Good Luck!
"""
print(preamble)
while True:
    one_game(target_hi=target_hi)
    print("Play a new game?")
    inp = input("Enter N to quit, M to change hi: ")
    if inp == "N" or inp == "n":
        break
    if inp == "M" or inp == "m":
        inp = input("Enter new Hi: ")
        target_hi = int(inp)
print("See you next time.")
