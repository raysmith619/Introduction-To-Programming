# notes_3c.py  26-Jul-2018
"""
Re-ask if can't open data file

Write a "Notes" program. The program will display lines
from a text file, containing a given text string.
Test:
file name = "people.notes"
text = "Watertown"
Loop
"""
import os
os.chdir(os.path.dirname(__file__))
file_name = "test.notes"

# Default values
def_file_name = "test.notes"
def_pattern = "student"

while True:
    # Set to default values
    pattern = def_pattern

    while True:
        file_name = def_file_name
        inp = input("Enter file name[" + file_name + "] ")
        inp = inp.rstrip()
        if inp == "":
            inp = file_name
        file_name = inp
        try:
            finp = open(file_name)
            break               # Got opened file
        
        except IOError :
            print("Can't open file ", file_name)
     



    inp = input("Enter pattern[" + pattern + "] ")
    inp = inp.rstrip()
    if inp == "":
        inp = pattern
    pattern = inp

    pattern_lc = pattern.lower()    # Force pattern to lower case
    for line in finp:
        line = line.rstrip()        # All trailing white space
        line_lc = line.lower()
        pat_index = line_lc.find(pattern_lc)
        if (pat_index > -1):
            print(line)
