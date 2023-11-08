""" twenty_questions.py
A simple python learning program
to play twenty questions
"""
import random

bottom_number = 1
top_number = 10
print("Guesses are completed by pressing the ENTER key")

while True:
    game_choice = random.randint(bottom_number, top_number)
    print("I'm thinking of a number from", bottom_number, "to", top_number)
    while True:
        print("Make a guess")
        iline = input()
        try:
            guess = int(iline)
        except:
            print("I don't understand", iline)
            print("Please enter a number")
            continue
        if guess == game_choice:
            print("Your guess of ", guess, "is CORRECT - You WON")
            break
        if guess > game_choice:
            print(guess, "is Greater than my choice")
        if guess < game_choice:
            print(guess, "is Less than my choice")
    print("Want to quit? Enter q")
    iline = input()
    if iline == "q":
        break               # No more games

print("Thanks.  Let's play again soon!")
