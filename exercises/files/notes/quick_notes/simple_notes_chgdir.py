# simple_notes_chgdir.py    20Nov2023  crs, use src dir
#                           20Jul2023  crs, Author
"""
list lines found in file
use source directory for data files
"""
import os

src_dir = os.path.dirname(__file__) # find source file directory
os.chdir(src_dir)           # Change to source file directory

file_name = "my_notes.txt"
file_name = "us_states.txt"
pattern = "Mass"        # Default pattern

inp = input("Enter Notes File["+file_name+"]:")
if inp != "":
    file_name = inp
inp = input("Enter pattern["+ pattern + "]:")
if inp != "":
    pattern = inp

with open(file_name) as finp:
    for line in finp:
        if line.find(pattern) > -1:
            print(line, end="")     # Already have endings
