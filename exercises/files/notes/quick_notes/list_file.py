# list_file.py  23Jun2023  crs, Author
"""
list file
"""
file_name = "my_notes.txt"

inp = input("Enter File["+file_name+"]:")
if inp != "":
    file_name = inp     # Choose default
with open(file_name) as finp:
    for line in finp:
        print(line, end="")     # Lines already have endings
