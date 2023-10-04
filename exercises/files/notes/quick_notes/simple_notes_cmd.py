# simple_notes_cmd.py  20Jul2023  crs, from simple_notes.py
"""
list lines found in file
+ support cmd line args [<file> [<pattern>]]
"""
import sys

file_name_arg = None    # set if cmd line arg present
if len(sys.argv) > 1:
    file_name_arg = sys.argv[1]

pattern_arg = None    # set if cmd line arg present
if len(sys.argv) > 2:
    pattern_arg = sys.argv[2]
     
file_name = "us_states.txt"
pattern = "Ala"

if file_name_arg is None:
    inp = input("Enter Notes File["+file_name+"]:")
    if inp != "":
        file_name = inp
else:
    file_name = file_name_arg

# Loop over patterns unless pattern on command line
while True:
    if pattern_arg is None:    
        inp = input("Enter pattern:["
                    +pattern+"]:")
        if inp != "":
            pattern = inp
    else:
        pattern = pattern_arg
        
    with open(file_name) as finp:
        for line in finp:
            if line.find(pattern) > -1:
                print(line, end="")     # Already have endings
    if pattern_arg is not None:
        break       # No looping if cmd line pattern arg