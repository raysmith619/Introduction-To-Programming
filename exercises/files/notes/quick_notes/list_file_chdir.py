# list_file_chdir.py  23Jun2023  crs, Author
"""
list file - first of notes
"""
import os
cwd = os.getcwd()
print(f"\ncurrent directory: {cwd}")   # f before quotes expands {value} in quotes

src_dir = os.path.dirname(__file__)
print(f"\nfile directory: {src_dir}")

if cwd.lower() != src_dir.lower():
    print("Changing directory to src dir")
    os.chdir(src_dir)


file_name = "my_notes.txt"

inp = input("Enter File["+file_name+"]:")
if inp != "":
    file_name = inp     # Choose default
with open(file_name) as finp:
    for line in finp:
        print(line, end="")     # Lines already have endings
