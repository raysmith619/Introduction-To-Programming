# mult_ask_user.py
# #############
# #############
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
def mult_game_one():
    """ Does one session and returns
    In the future one might have parameters e.g. high number, low number
    """
    n_min = int(input('Please enter a low number for your multiplication table.: '))
    print('')
    print('')
    print("Thank you for your input. You have set the low range as: ", n_min)
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
    print('')
    print('')
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

    spnum = int(log10(n_max*n_min)) + 1  # width alowed for product +1
    m = m_min           # Initialise dowward numbers
    while m <= m_max:
        n = n_min       # Initialize sideways numbers
        if m == m_min:  # put header before first line
            nh = n_min
            print(spnum*" ", sep="", end="")    # align header with sideways numbers
            while nh <= n_max:
                len_nh = int(log10(nh)+1)
                sp = (spnum-len_nh+1)*"-"
                print(sp, nh, sep="", end=" ")
                nh += 1         # Increment side ways number
            print()
            print(spnum*" ", sep="", end="")    # align header with sideways numbers
            ncol = n_max - n_min + 1
            nc = 0
            while nc <= ncol:
                print((spnum)*"-", end="")
                nc += 1
            print()
    # Adjust for m changes in length
        len_m = int(log10(m)) + 1
        print((spnum-len_m)*" ", m, sep="", end="")
        while n <= n_max:
            len_nm = int(log10(n*m)) + 1
            sp =  (spnum-len_nm+1) * " "
            print(sp, n*m, sep="", end=" ")
            n += 1         # Increment side ways number
        print()         # end sideways line of nums
        m += 1          # Increment downward numbers

"""
Let's do the multiple game as calls to the single game
"""
while True:
    mult_game_one()
    inp = input("Enter y/yes/ENTER to play again: ")
    if inp == "y" or inp == "yes" or inp == "":
       continue
    print("Thanks for playing - see you next time.")
    break

    
