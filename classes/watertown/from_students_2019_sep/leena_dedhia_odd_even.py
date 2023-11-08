# leena_dedhia_odd_even.py 
"""
Leena Dedhia
Mon, Oct 28, 6:36 PM (2 days ago)
to raysmith
"""
# first of twenty questions --LD
# while true repeat
while True:
    inp = input("Please use your num-key and enter a number: ")
    guess = int(inp)
    print("You Entered the number: ",guess)
    if (guess % 2) == 0:
       # print("{0} is Even".format(guess))
       print(guess," is even")
    else:
       #print("{0} is Odd".format(guess))
        print(guess," is odd")
    print("")
