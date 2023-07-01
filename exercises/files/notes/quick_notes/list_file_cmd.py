# list_file_cmd.py  23Jun2023  crs, add cmd line option
"""
list file
with option to take file name from command line first argument
"""
import sys

file_name = "my_notes.txt"  # Default file name
if len(sys.argv) > 1:       # argv[0] is program name
    file_name = sys.argv[1] # Use first argument as file name
else:
    # No command line arguments - prompt user for file name
    inp = input("Enter File["+file_name+"]:")
    if inp != "":
        file_name = inp     # Choose default

with open(file_name) as finp:
    for line in finp:
        print(line, end="")     # Lines already have endings
