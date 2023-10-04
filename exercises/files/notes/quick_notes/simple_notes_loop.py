# simple_notes_loop.py  25Jun2023  crs, from simple_notes.py
"""
list lines found in file
+ loop for next file
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
    with open(file_name) as finp:
        for line in finp:
            if line.find(pattern) > -1:
                print(line, end="")     # Lines already have endings
