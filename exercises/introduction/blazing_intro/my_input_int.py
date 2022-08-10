# my_input_int.py    27Dec2021  crs - exercise int()
# Get user input from the keyboard and check against an int
target = 5
while True:
    inp = input("Please enter number:")
    print("You entered", inp)
    ival = int(inp)
    if ival < target:
        print(ival, "is less than", target)
    elif ival > target:
        print(ival, "is greater than", target)
    elif ival == target:
        print(ival, "is equal to", target)
