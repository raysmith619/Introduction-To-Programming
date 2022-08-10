# my_input_loop.py    27Dec2021  crs - exercise input loop()
# Get user input from the keyboard ina loop

while True:
    inp = input("Please enter number:")
    print("You entered", inp)
    number = int(inp)   # Convert kbd str to int
    if number > 3:
        print("number:", number,  "is > 3")
