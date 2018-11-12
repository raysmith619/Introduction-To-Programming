#remove_non_utf8.py
"""
An attempt to remove non-UTF8 characters from text
pasted from Wikapedia
"""
import re

def_file_name = r"C:\Users\raysm\Desktop\freq_info.txt"
file_name = def_file_name
inp = input("Enter file name[" + file_name + "] ")
inp = inp.rstrip()
if inp == "":
    inp = file_name
file_name = inp
try:
    finp = open(file_name)
except IOError :
    print("Can't open file ", file_name)
    exit()
for line in finp:
    new_line =re.sub(r'[^\x00-\x7F]', '', line)
    print(new_line, end="")
finp.close()
    
