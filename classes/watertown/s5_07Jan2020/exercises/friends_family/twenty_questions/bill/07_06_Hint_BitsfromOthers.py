#
# 07_06_Hint_BitsfromOthers.py  Jul 06, 2019  BD
#
# from,  02_11_Homework_2nd_iteration.py
#
# and 02_19_Sys.exit_Graceful_Exit.py
#
# ############
# ############
#
# Runs, but gives hint right away.....
#
#    >>> 
#      RESTART: C:\Users\Administrator\Desktop\Python 3, Source for BPL Class\_WFPL_PythonClass_RaySmith\Classwork\twenty_questions\07_06_Hint_BitsfromOthers.py 
#     Enter Number 5
#     Number: 5
#     Do you want a hint? 5 Maybe what you are looking for.
#     Enter Number 
#
# #############
# #############
# 
# entering hint results in:
# 
#     Enter Number hint
#     Traceback (most recent call last):
#       File "C:\Users\Administrator\Desktop\Python 3, Source for BPL Class\_WFPL_PythonClass_RaySmith\Classwork\twenty_questions\07_06_Hint_BitsfromOthers.py", line 27, in <module>
#         num = int(inp)
#     ValueError: invalid literal for int() with base 10: 'hint'
#
#
#
#
#
#"""
import sys
import random
target_value = random.randint (3, 101)
randomhint = target_value +9
while True:
    inp = input("Enter Number ")
    num = int(inp)
    print("Number:", num)
    if target_value > num:
#  Ah, you do need the comma before num...)
#        print("Sorry, my number is greater than" num)
        print("Sorry Square, my number is greater than", num)
        continue
    if target_value < num:
        print("Sorry wiggles, my number is less than", num)
        continue
#    if target_value == hint:
#        print("Do you want a hint?", target_value, "Maybe what you are looking for.")
#        continue
    if num == target_value:
        print("Bingo Bigs, you got it", num, " is the number I was looking for")
        break
#
# Hmmm, prompts "program is still running, do you want to ----terminate?
# exit()
#
# With import sys at the top, this works~!!!
sys.exit()
