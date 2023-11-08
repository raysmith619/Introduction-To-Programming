#input_test.py 24Sep2020 crs
balance = 50000.
ans = input("Enter withdrawal ammount: ")
if ans == "ALL":
    withdrawal = balance
else:
    withdrawal = float(ans)
print("You entered", ans)
if withdrawal > balance:
    print("Sorry:", ans, "is more than", balance, "your balance")
else:
    print("Here comes", withdrawal)

