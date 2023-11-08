# input_loop_number.py 17-Jul-2017
# Input list of numbers summing them
sum = 0
while True:
    inp = input("enter number (q or Q to quit)")
    if inp == "q" or inp == "Q":
        break
    ###inp_number = int(inp)       # Convert string to integer
    inp_number = float(inp)     # Convert string to floating point
    sum = sum + inp_number

print("sum=", sum)