# fourth_with_random.py 24Jun2020   crs, add random
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
#+
# Set the target to a random number.
# We tell the contestant the range.

import random           # Bring in python support for random numbers

target_min = 1
target_max = 20

intro = ("""
Welcome to our number guessing game
I've picked a number.  It is between """
+ str(target_min) + " and " + str(target_max)
+
"""

You can enter a guess.

I'll let you know if your
guess is
    less than my number
      OR
    greater than my number
      OR
    EXACTLY my number.
Please press the ENTER key after typing your guess.
"""
)
print(intro)
target_value = random.randint(target_min, target_max) # Include max
###target_value = 6    # Uncomment this to test with one value
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

