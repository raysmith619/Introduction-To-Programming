# second.py 17Jul2018
"""
# Twenty questions
# loop asking number
# print number entered
#+
# Set target value
# Quit if number entered number equals target
"""

target_value = 5
while True:
    inp = input("Enter Number ")
    num = int(inp)
    print("Number:", num)
    if num == target_value:
        print("guess of ", num, " equals target ",target_value)
        break
