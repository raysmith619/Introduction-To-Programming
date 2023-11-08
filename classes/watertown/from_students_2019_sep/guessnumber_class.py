print("*** Program Starting ***")
# Guessing game
import random
import random 
# Generates a random number between 1 and 100
# a given positive range 
target_number = random.randint(1,100)
print("target_number = ", target_number)  # Show target
while True:
    inp = input("Please enter your guess: ")
    guess = int(inp)
    if target_number == guess:
        print(f"you got it! - Your guess is {guess} and the target is {target_number}")
    elif guess > target_number:
        print(f"Your Number {guess} is greater than guess: ")
    else:
        print(f"Your guess {guess} is less than number: ")
