# t4.py 17Jul2018
"""
# Twenty questions
# loop asking number
# print number entered
+
Announce goals, rules before start
#+
# Set target value
# Quit if number entered number equals target
#+
# Announce if guess greater, less or equal
#
"""
target_value = 5
while True:
    inp = input("Enter Number ")
    num = int(inp)
    print("Number:", num)
    if target_value > num:
        print("Sorry, my number is greater than", num)
        continue            # continue with loop
    if target_value < num:
        print("Sorry, my number is less than", num)
        continue            # continue with loop
    if num == target_value:
        print("You Got it - ", num, " is my number ")
        break

