# fourth.py 17Jul2018
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
#
intro = """
Welcome to our number guessing game
I've picked a number.
You can enter guesses and I'll let you know if your
guess is less than my number, greater than my number
or EXACTLY my number.
Please press the ENTER key after typing your guess.
"""
print(intro)
target_value = 5
while True:
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
    inp = input("Play another game? - q to quit ")
    if inp == 'q' or inp == 'Q':
        print("See you later!")
        break
    
