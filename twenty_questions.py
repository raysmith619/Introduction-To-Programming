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
    You make guesses about this number.
    Press the ENTER key to complete the guess.
    Use a number, like 5, to guess that number exactly.
    Use the characters < for LESS than, > for GREATER than, = for EQUAL to

    Use < NUMBER to ask "Is the choice less than NUMBER?"
        <= NUMBER to ask "Is the choice less than or equal to NUMBER?"
        = NUMBER  (or just enter the number) equal to NUMBER
        > NUMBER  greater than NUMBER
        >= NUMBER greater than or equal NUMBER
    Examples: >5 : "Is it greater than 5?"
              <= 7 : "Is it greater than or equal to 7?"
    I'll answer yes or no.
""" % (bottom_number, top_number))

while True:
    game_choice = random.randint(bottom_number, top_number)
    print("I made a choice from %d to %d" % (bottom_number, top_number))
    ##print("my choice is %d" % (game_choice))
    while True:
        print("Make a guess")
        iline = input()
        if iline == "q":
            break           # End this game

        is_yes = False      # Set True if correct

                            # Determine guess direction
        is_greater = False
        is_greater_equal = False
        is_less = False
        is_less_equal = False
        is_equal = False


        iline = iline.replace(" ", "")  # Remove all blanks

        # Check for simple number
        # Treat this as "="
        is_a_number = False
        try:
            guess = int(iline)
            is_a_number = True
            is_equal = True
            if guess == game_choice:
                is_yes = True
        except ValueError:
            pass            # Not just a number
        
        if not is_a_number:
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
                print(
            """
            I'm sorry, but I only understand >, >=, <, <=, =,
            just a number,
            or q,
            Please guess again
            """
            )
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
                print("You have WON the game!")
                break
        else:
            if is_a_number:     # Help if just gave a number
                if game_choice > guess:
                    print("no, but the answer is GREATER than %d" % guess)
                elif game_choice < guess:
                    print("no, but the answer is LESS than %d" % guess)
            else:
                print("no")


    print("Want to play another? Enter y")
    iline = input()
    if iline.startswith("t"):
        iline = iline.replace("t", "")
        iline = iline.replace(" ", "")
        top_number = int(iline)
        print("New top_number is %d" % top_number)
        continue
    
    if iline != "y":
        break               # No more games

print("Thanks.  Let's play again soon!")
