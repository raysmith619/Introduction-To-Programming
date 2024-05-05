# notes_3e.py   13Oct2022  crs, from notes_3d
#               26-Jul-2018
"""
Write a "Notes" program. The program will display lines
from a text file, containing a given text string.
Test:
file name = "people.notes"
text = "Watertown"
Loop asking for new file
Loop over patterns
Use regular expression search
"""
import re
import os

# Protect if current working directory not source file directory
src_dir = os.path.dirname(__file__)
os.chdir(src_dir)

# Default values
file_name = "test.notes"
file_name = "us_states.txt"
pattern = "student"
pattern = "mass"

while True:
    while True:
        while True:     # Loop till good file
            inp = input("Enter file name[" + file_name + "] ")
            inp = inp.rstrip()
            if inp == "":
                inp = file_name
            file_name = inp
            try:
                finp = open(file_name)
                finp.close()    # Just testing
                print("   at", os.path.abspath(file_name))
                break           # Successful open file
            
            except IOError :
                print("Can't open file ", file_name)
                print("   at", os.path.abspath(file_name))

        while True:
            with open(file_name) as finp:
                inp = input("Enter pattern(rex)[" + pattern + "] ")
                inp = inp.rstrip()
                if inp == "":
                    inp = pattern
                pattern = inp

                pattern_lc = pattern.lower()    # Force pattern to lower case
                for line in finp:
                    line = line.rstrip()        # All trailing white space
                    line_lc = line.lower()
                    match = re.search(pattern, line)
                    match = re.search(pattern_lc, line_lc) # lowercase
                    if (match):
                        print(line)
