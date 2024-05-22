# notes_2.py  26-Jul-2018
"""
Write a "Notes" program. The program will display lines
from a text file, containing a given text string.
Test:
file name = "people.notes"
text = "Watertown"
 Implementation Iterations:
Setup test file(s): "test.notes",  "people.notes"
    1.	Read specific file e.g. "test.notes", printing out all lines
    2.	Print only lines containing "student"
            How to match lines ? Google "python search for substring" ?
            Support case insensitive match (Student, STUDENT)
    3.	Prompt for, then accept file name, pattern
    4.	[Extra Credit]  Support multiple text patterns
+ print lines with pattern
"""
import os
os.chdir(os.path.dirname(__file__))
file_name = "test.notes"

pattern = "student"
with open(file_name) as finp:
    for line in finp:
        line = line.rstrip()    # All trailing white space
        pat_index = line.find(pattern)
        if (pat_index > -1):
            print(line)
