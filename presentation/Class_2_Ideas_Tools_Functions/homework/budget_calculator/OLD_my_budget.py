#my_budget    27-Jul-2021  crs, Author
"""
Budget Calculator
Sometimes it may be useful to see how budget goals
(e.g., save 200/year reflect on other time periods).
This exercise is to build a program which takes an
amount / percentage per time period (%, year, month,
week) reflects on the other time periods.
    a.	Ask salary pay period: Year, Month, Week
    b.	Ask salary, per pay period: 
    c.	Loop
        i.  Ask budget(save) period: Percent,
            Year, Month, Week
        ii. Ask budget(save) amount: per period
            or percentage
        iii.Print percentage, yearly amount,
            monthly amount, weekly amount
"""
# Generic names, incase we want to
# something like synomyns, abreviations, languages
PP_YEAR = "Year"
PP_MONTH = "Month"
PP_WEEK = "Week"
PP_HOUR = "Hour"
pay_period = PP_YEAR # Default period
yr_salary = 0.
mth_salary = 0.
wk_salary = 0.
hr_salary = 0.  # Hourly salary (2000hr/year)

pay_per = input("Enter pay period[Year]:")
if pay_per == "":
    pay_per = pay_period    # Use default
while True:
    pay_amt_inp = input("Enter pay amount per period:")
    if pay_amt_inp == "":
        pay_amt_inp = "1000"    # Just to have something
        print("Assuming amt:", pay_amt_inp)
    pay_amt = float(pay_amt_inp)
    if pay_per == PP_YEAR:
        yr_salary = pay_amt
    elif pay_per == PP_MONTH:
        yr_salary = 12*pay_amt
    elif pay_per == PP_WEEK:
        yr_salary = 50*pay_amt
    elif pay_per == PP_HOUR:
        yr_salary = 2000*pay_amt
    else:
        print("Sorry - we don't currently support"
              " pay periods of", pay_per)
        exit()

    mth_salary = yr_salary/12
    wk_salary = yr_salary/50
    hr_salary = yr_salary/2000
        
    print(f"Salary: yr: {yr_salary:,.2f}",
          f" mth: {mth_salary:.2f}",
          f" wk: {wk_salary:.2f}",
          f" hr: {hr_salary:.2f}")
