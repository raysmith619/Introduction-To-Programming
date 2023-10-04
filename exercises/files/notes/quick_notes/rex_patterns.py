# rex_patterns.py  19Jul2023  crs, from simple_notes_loop.py
"""
list lines found in file
+ loop for regular expression pattern
"""
import re

file_name = "my_notes.txt"
file_name = "us_states.txt"
pattern = "mass"
while True:
    inp = input("Enter Notes File["+file_name+"]:")
    if inp != "":
        file_name = inp
    while True:
        with open(file_name) as finp:        
                inp = input("Enter pattern (rex)["
                            +pattern+"]:")
                if inp != "":
                    pattern = inp

                for line in finp:
                    if re.search(pattern, line) is not None:
                        print(line, end="")     # Lines already have endings
