#second py    vt47555 
#20 questions
# loop asking number
import random
guesses_taken = 0
print('hello!')
number = random.randint(1,20)
print ('Play a game with me! I am thinking of a number between 1 and 20.')

while guesses_taken < 6:
    print ('take a guess')
    guess = input()
    guess = int(guess)

    guesses_taken = guesses_taken + 1

    if guess < number:
        print ('too low')

    if guess > number:
        print ('too high')

    if guess == number:
        break

if guess == number:
    guesses_taken = str(guesses_taken)
    print ('you got it! you guesses the number in '  + guesses_taken + ' guesses!')
if guess != number:
    number = str(number)
    print ('The number I was thinking of was' + number)
