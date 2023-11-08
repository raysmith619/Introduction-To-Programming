# thinking_of_no_rose_mary.py
# From thinking_of_no
#rosemarysu
#2020/01/21

# Suggestions:
# 1.Think of what comes first, for example the target value
#    Those things should preceed the loop
# 2. Think of what is repeated, for example the prompt, getting number
#    Those things should be in the loop body
# 3. For complicated/involved loops try "while True" with break to exit loop.
# 4. Name your variables as to there purpose.
#    e.g. target for the target value
target = 25      # Set target value (later randomize it)
print("I'm thinking of a number...")

while True:         # Loop till answer == target
    inp = input("Please enter guess:")
    guess = int(inp)
    print("Entered guess:", guess)      # Just to trace
    if guess == target:
        print(guess,"is the correct number I'm thinking! Congratulations")
        break
    if guess < target:
        print(inp, "is smaller than the number I'm thinking")
        print("try more than",guess)
        continue
    if guess > target:
        print(inp, "is larger than the number I'm thinking")
        print("try less than",guess)
        continue
