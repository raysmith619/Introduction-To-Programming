#my_budget  04-Aug-2021  crs, from my_salary.py
#           27-Jul-2021  crs, Author
"""
Budget Calculator
Sometimes it may be useful to see how budget goals
(e.g., save 200/year reflect on other time periods).
This exercise is to build a program which takes an
amount / percentage per time period (%, year, month,
week) reflects on the other time periods.
Loop
    a.	Ask salary pay period: Year, Month, Week
    b.	Ask salary, per pay period
    c. Loop in budget()
        i.  Ask budget(save) period: Percent,
            Year, Month, Week
        ii. Ask budget(save) amount: per period
            or percentage
        iii.Print percentage, yearly amount,
            monthly amount, weekly amount

    Note to ease text formatting we introduce the
    following Python:
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


"""
Budget calculation function
This function does the budget calculations
in a loop, using the salary calculations
made in the main program level
"""


def do_budget():

    budget_period = pay_period  # Initial budget period
                                #   default to pay_period
    budget_specs = periods
    BA_PERC = "%"
    budget_specs.append(BA_PERC)    # Add % for percent budget
    budget_spec = BA_PERC
    budget_amt = 0              # Most recent ammount

    
    while True:
        inp = input(f"Enter Budget period or %[{budget_spec}]")
        if inp != "":
            inp = inp.lower()   # Uniformity
            if inp == CMD_QUIT:
                break           # Go back to top loop

            if inp not in budget_specs:
                print("Sorry - we don't"
                      " currently support"
                      " budget specification of", inp)
                continue    # Ask again

            budget_spec = inp   # Use as default
        else:
            inp = budget_spec # Use current specification
            print("Assuming:", inp)
        if budget_spec == BA_PERC:
            budget_percent = 10
            prompt = f"Enter Budget percent:[{budget_percent}]:"
        else:
            prompt = (f"Enter {budget_spec}ly Budget"
                     f"[{budget_amt}]:")
        inp = input(prompt)
        if inp != "":
            inp = inp.lower()   # Uniformity
            if inp == CMD_QUIT:
                break           # Go back to top loop

        if budget_spec == BA_PERC:
            if inp != "":
                budget_percent = float(inp)
        else:
            if inp != "":
                budget_amt = float(inp)
            if budget_spec == PP_YEAR:
                budget_percent = budget_amt/yr_salary*100.
            elif budget_spec == PP_MONTH:
                budget_percent = budget_amt/mth_salary*100.
            elif budget_spec == PP_WEEK:
                budget_percent = budget_amt/wk_salary*100.
            elif budget_spec == PP_HOUR:
                budget_percent = budget_amt/hr_salary*100.
            else:
                print("problem with budget_spec",
                      budget_spec)
                exit()

        yr_budget = yr_salary*budget_percent/100
        mth_budget = mth_salary*budget_percent/100
        wk_budget = wk_salary*budget_percent/100
        hr_budget = hr_salary*budget_percent/100
        print(f"Budget: {budget_percent:.1f}%"
              f" yr: {yr_budget:,.2f}",
              f" mth: {mth_budget:,.2f}",
              f" wk: {wk_budget:,.2f}",
              f" hr: {hr_budget:,.2f}")

# Main program starts    
print("Budget Calculator")
print("supporting pay periods of:")
for pyp in periods:
    print(f"\t{pyp}")
print("Enter BYE to quit level")
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
        inp = "1000."    # Just to have something
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
    print(f"Salary: yr: {yr_salary:,.2f}",
          f" mth: {mth_salary:,.2f}",
          f" wk: {wk_salary:,.2f}",
          f" hr: {hr_salary:,.2f}")

    do_budget() #  Do budgeting
        
print("Good Bye")