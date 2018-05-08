""" twenty_questions.py
A simple python learning program
to play twenty questions
I'm thinking of a number from 1 to 10
You make guesses as to if the number is greater,
less, or equal to some number within that range.
Please enter >NUMBER to guess is it greater than that number
I'll answer yes or no.
"""
import random

bottom_number = 1
top_number = 10
print("""
    I'm thinking of a number from %d to %d
    You make guesses as to if the number is greater,
    less, or equal to some number within that range.
    Use < NUMBER to ask "Is the choice less than NUMBER?"
        <= NUMBER to ask "Is the choice less than or equal to NUMBER?"
        = NUMBER  equal to NUMBER
        > NUMBER  greater than NUMBER
        >= NUMBER greater than or equal NUMBER
    Examples: >5 : "Is it greater than 5?"
              <= 7 : "Is it greater than or equal to 7?"
    I'll answer yes or no.
""" % (bottom_number, top_number))

while True:
    game_choice = random.randint(bottom_number, top_number+1)
    print("I made a choice from %d to %d" % (bottom_number, top_number))
    ##print("my choice is %d" % (game_choice))
    while True:
        print("Make a guess")
        iline = input()
        if iline == "q":
            break           # End this game

                            # Determine guess direction
        is_greater = False
        is_greater_equal = False
        is_less = False
        is_less_equal = False
        is_equal = False

        while " " in iline:     # Remove all blanks
            iline = iline.replace(" ", "")

        if ">=" in iline:
            is_greater_equal = True
            iline = iline.replace(">=", "")
        elif ">" in iline:
            is_greater = True
            iline = iline.replace(">", "")
        elif "<=" in iline:
            is_less_equal = True
            iline = iline.replace("<=", "")
        elif "<" in iline:
            is_less = True
            iline = iline.replace("<", "")
        elif "=" in iline:
            is_equal = True
            iline = iline.replace("=", "")
        else:
            print("I'm sory, but I only understand >, >=, <, <=, =, and q, please guess again")
            continue

        guess = int(iline)
        ##print("guess=%d" % (guess))
        is_yes = False                      # Set True if guess is right
        if is_greater and game_choice > guess:
            is_yes = True
        elif is_greater_equal and game_choice >= guess:
            is_yes = True
        elif is_less_equal and game_choice <= guess:
            is_yes = True
        elif is_less and game_choice < guess:
            is_yes = True
        elif is_equal and game_choice == guess:
            is_yes = True

        if is_yes:
            print("yes")
            if is_equal:
                print("YOU HAVE GUESSED THE ANSWER %d" % (guess))
                print("The game is WON")
                break
        else:
            print("no")


    print("Want to play another? Enter y")
    iline = input()
    if iline != "y":
        break               # No more games

print("Thanks.  Let's play again soon!")
