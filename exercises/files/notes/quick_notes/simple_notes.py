# simple_notes.py  20Jul2023  crs, Author
"""
List lines found in file containing pattern
"""
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
