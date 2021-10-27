# Python program to print
# red text with green background
 
from colorama import Fore, Back, Style
from colorama import init
print("NOTE: this does not display colors when run in IDLE")
print("This does display colors when run from Windows Shell")
init()
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
