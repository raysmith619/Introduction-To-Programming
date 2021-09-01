#my_salary    27-Jul-2021  crs, Author
"""
Salary Calculator
    Loop
        Ask salary pay period: Year, Month, Week
        Ask salary, per pay period:
        Print salary yearly, monthly, weekly, hourly


    Note to ease text formatting we introduce the
    following Python (f-string):
    
    f"text...{value:format}" evaluates to
    (is replaced by) text...text of value
    Example: f"{sum:1234.5:,.2f}" is replaced by
             sum:1,234.50

        
"""
# Generic names, incase we want to
# something like synomyns, abreviations, languages
CMD_QUIT = "bye"    # Command to quit loop
PP_YEAR = "year"
PP_MONTH = "month"
PP_WEEK = "week"
PP_HOUR = "hour"
periods = [PP_YEAR, PP_MONTH, PP_WEEK, PP_HOUR]
pay_period = PP_YEAR # Default period
yr_salary = 0.
mth_salary = 0.
wk_salary = 0.
hr_salary = 0.  # Hourly salary (2000hr/year)
pay_amt_inp = "123456"  # Default - to ease demo
print("Salary Calculator")
print("supporting pay periods of:")
for payp in periods:
    print(f"\t{payp}")
print("Enter BYE to quit")
while True:
    inp = input(f"Enter pay period[{pay_period}]: ")    
    if inp != "":
        inp = inp.lower()   # Uniformity
        if inp == CMD_QUIT:
            break

    else:
        inp = pay_period    
    if inp not in periods:
        print("Sorry - we don't"
              " currently support"
              " pay periods of", inp)
        continue    # Ask again
            
    pay_period = inp    # New default

    inp = input(f"Enter pay amount per {pay_period}: ")    
    if inp != "":
        inp = inp.lower()   # Uniformity
        if inp == CMD_QUIT:
            break
    else:
        inp = "1000"    # Just to have something
        print("Assuming amt:", inp)
    pay_amt = float(inp)
    if pay_period == PP_YEAR:
        yr_salary = pay_amt
    elif pay_period == PP_MONTH:
        yr_salary = 12*pay_amt
    elif pay_period == PP_WEEK:
        yr_salary = 50*pay_amt
    elif pay_period == PP_HOUR:
        yr_salary = 2000*pay_amt
    else:
        print("problem with pay_period", inp)
        exit()

    mth_salary = yr_salary/12
    wk_salary = yr_salary/50
    hr_salary = yr_salary/2000
    """
        Note: f"text...{value:format}" evaluates to
        (is replaced by) text...text of value
        Example: f"{sum:1234.5:,.2f}" is replaced by
                 sum:1,234.50
    """
    print(f"Salary: yr: {yr_salary:,.2f}",
          f" mth: {mth_salary:,.2f}",
          f" wk: {wk_salary:,.2f}",
          f" hr: {hr_salary:,.2f}")

print("Good Bye")
