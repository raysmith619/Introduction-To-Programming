# Program name: Guess_my_number_version4.py

"""
In this exercise we are programming a game, which goal is that the player guess
the integer number that we choosed. In this case the target or chosen number will be a random number. 
The player may keep playing or may stop at any time. 
"""
# imports random module 
import random 
print ("Let's play! You must guess a random number between 1 and 100")
print ("I will help you letting know if your guess is lower, higher or equal to that random number.")
print ("You may stop playing anytime, writing the word STOP. " )

stop = "STOP"
while True:
      # Generates a random number between 1 and 100
      # a given positive range 
      target = random.randint(1,100)
      
       #This will show the randon number just for programming verification purpose.
      
      print ("This will show the randon number just for programming verification purpose.")
      print ("Random number between 0 and 100 is " , target) 
      
      is_stop = False         # Set to True if we are to stop program
      while True:
            inp = input ("Please enter your guess or enter STOP if you do not want to play anymore:   ")
            
            if inp != stop:
              
                  guess = int (inp)

                  if guess < target:
                     print ("Sorry, your guess, ", guess, "is lower than my number")

                  if guess > target:
                     print ("Sorry, your guess,", guess,  "is higher than my number")

                  if guess == target:
                     print ("         ")   
                     print ("  Congratulations! YOU DID GUESS THE RANDOM NUMBER!   " )
                     break
            elif inp == stop:
                  is_stop = True    # So next level can check
                  break
      if is_stop:
            print ("                        ")
            print (" Thank you for playing with me. Good bye!")
            break             # Break out of the games loop
      
      print ("                                   ")
      print ("Do you want to play again? ")
      inp = input ("1 for Yes or 2 for No:  ")
      answer = int(inp)             
      if answer == 2:
            print ("                        ")
            print (" Thank you for playing with me. Good bye!") 
            break

