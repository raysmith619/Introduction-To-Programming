print("*** Program Starting ***")
"""Lakpa SAnge
program about raise salary code """
###> My Comments
###> Looks to be working except "* .02" should be "* .01"

def money():
    current_salary = float(input("Enter the starting salary: "))
    years = int(input("Enter the number of years: "))
    raise_percent = float(input("percent of raise each year: ")) * 0.02

    for years in range(1, years + 1):
        current_salary += current_salary * raise_percent
        print("you will be making", current_salary,' in ', years,'years.')
money()
print("***program Ending ***")
