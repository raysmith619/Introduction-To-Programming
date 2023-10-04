# simple_notes_case_insensitive.py  19Jul2023  crs, from simple_notes.py
"""
list lines found in file
+ case insensitive
"""
file_name = "my_notes.txt"
file_name = "us_states.txt"
inp = input("Enter Notes File["+file_name+"]:")
if inp != "":
    file_name = inp
while True:
    inp = input("Enter pattern:")
    if inp != "":
        pattern = inp
        break

with open(file_name) as finp:
    for line in finp:
        line_lower = line.lower()
        pattern_lower = pattern.lower()
        if line_lower.find(pattern_lower) > -1:
            print(line, end="")     # Lines already have endings
