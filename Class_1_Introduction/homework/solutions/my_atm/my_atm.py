#my_atm.py  16-Jan-2022  crs, Check if not a number
#           20-Sep-2021  crs, A few adjustments
#           23-Jul-2021  crs, Author
"""
MY_ATM – THE BEGINNINGS OF AN ATM MACHINE PROGRAM
An ATM or Automatic Teller Machine facilitates
the depositing and dispersal of money.
Even without the mechanical aspects the programming
involved can be very complex.  Our program here
will begin with just concerning the accepting and
dispersing money.  We will just consider the single
individual having already logged on and verified.
To further simplify the demands on the program only
deposits or withdrawals will be accepted.

1. Initial balance is 0.
2. Pressing the ENTER key with no amount will
   exit
3. Positive number will withdraw that amount,
   IF SUFFICIENT BALANCE, and display the balance
4. Negative number will deposit that amount,
   and display the balance
"""
cust_balance = 0.   # Customer balance (USD)
while True:         # Default - go forever
    inp = input("Withdrawal AMOUNT:")
    if inp == "":
        break
    try:
        amt = float(inp)
    except ValueError:
        print("Sorry", inp, "is not a valid number")
        print("Please try again.")
        continue
    
    if amt < 0:
        deposit = -amt
        cust_balance += deposit
        print("Deposit:", deposit)
        print("New Balance:", cust_balance)
        continue

    if amt > 0:
        if cust_balance < amt:
            print("Insufficient Funds for withdrawal")
            print("Balance:", cust_balance, " request: ", amt)
            continue
        cust_balance -= amt
        print("Withdrawal:", amt)
        print("New balance:", cust_balance)

print("Bye - Have a good day")
