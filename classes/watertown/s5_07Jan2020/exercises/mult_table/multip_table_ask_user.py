# 
# #############
# #############
# 
# Crap, since you reied to re-order/phrase the print statement everything
# has fallen to pieces...
# 
# 
# RESTART: C:/Users/Administrator/Desktop/Python 3, Source for BPL Class/_WFPL_PythonClass_RaySmith/Classwork/_Week5/multip_table_ask_user.py 
# Would you like to choose a low number for your multiplication table?: 2
# Thank you for your input. You have set the low range (across) as:  2
# 
# Please note the 2nd number you enter needs to be a number higher than your 1st input--or the program will exit).
# 
# 
# Traceback (most recent call last):
#   File "C:/Users/Administrator/Desktop/Python 3, Source for BPL Class/_WFPL_PythonClass_RaySmith/Classwork/_Week5/multip_table_ask_user.py", line 51, in <module>
#     print('Thank you. You have set the high range for (across) as: ', n_max)
# 
# 
# NameError: name 'n_max' is not defined
# >>> 
#
# 
# #########
# #########
# 
# multip_table_ask_user.py  -- 23 Jul 2019
# 
# ask user for min and max by Bill  (# from Ray Smith..... email)
# 
# 
# times_mn.py 17July2019  crs
# 
# times table printout using nested while (Ray Smith)
# 
# #######
# #######
# 
# The scope of this project is a times table print out across and down. (Bill)
# 
# Example:
# 
#  m down
#  |
#  V
# 
#      1  2  3  4 ... n -> side ways
#   1  1  2  3
#   2  2  4
#   3  3  6
#   4  4
# 
# So let's go and run the script!

from math import *
# 
# 
# n_min = int(input('Would you like to choose a low number for your multiplication table?: '))
n_min = int(input('Please enter a low number for your multiplication table.: '))
# 
# 
# print("Thank you for your input. You have set the low range (across) as: ", n_min)
print('')
print('')
print("Thank you for your input. You have set the low range as: ", n_min)
# 
# n_max = int(input('Would you like to choose a high number for N?: \
#                   Please note the 2nd number you choose needs to be a number \
#                   higher than your first input' ))
# print('')
# print('')
# n_max = int(input('Now we require a high number for the multiplication table. Please note the 2nd number you enter needs to be a number higher than your first input (or the program will exit): ' ))
# 
#
print('')
print('')
print('Please note the 2nd number you enter needs to be a number higher than your 1st input--or the program will exit).' )
# print('')
# print('')
# n_max = int(input('Please enter your 2nd number: ' )
#
# Next line, invalid syntax....
print('')
print('')
# 
# #########
# #########
# 
# Here it is,  n_max, not defined.... too early~
# 
# print('Thank you. You have set the high range for (across) as: ', n_max)
#
# print('Thank you. You have set the high range for (across) as: ')
print('')
print('')
#print('...')
# 
#print('Please note that setting N has now set M to match, and your times table will be symmetrical. Pretty nifty we thought')
# 
# 
# print('Please note that N (across) and M (down) now match, and your times table will be symmetrical. Pretty nifty we thought')
# print('')
# print('')
# 
# 
# ----
# ----
# ----
n_max = int(input('Please enter a high number for your multiplication table.: '))
#
#
print('')
print('')
print('Please note that N (across) and M (down) now match, and your times table will be symmetrical. Pretty nifty we thought.')
#
# 
print('')
print('')
# ____
# ____
m_min = n_min
m_max = n_max

m = m_min           # Initialise dowward numbers
while m <= m_max:
    n = n_min       # Initialize sideways numbers
    if m == m_min:  # put header before first line
        nh = n_min
        print("   ", end="")    # align header with sideways numbers
        while nh <= n_max:
            sp = "--"
            print(sp, nh, end=" ")
            nh += 1         # Increment side ways number
        print()
        print("   ", end="")    # align header with sideways numbers
        print(nh*3 * "-")
    print(m," ", end="")
    while n <= n_max:
        sp =""
        len_nm = int(log10(n*m))
        spnum = 3       # width alowed fo product
        sp =  (spnum-len_nm) * " "
        print(sp, n*m, sep="", end=" ")
        n += 1         # Increment side ways number
    print()         # end sideways line of nums
    m += 1          # Increment downward numbers



#  ___===============
