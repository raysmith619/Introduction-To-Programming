# simple_notes_cmd_flags.py 23Jul2023  crs, 
#                           20Jul2023  crs, simple_notes_cmd.py
"""
list lines found in file
+ support cmd line arg flags [-f <file>] [-p <pattern>]]
"""
import sys

                        # Optional cmd line args
file_name_arg = None    # set if -f present
pattern_arg = None      # set if -p arg present

argi = 1            # start after pgm name
while argi <  len(sys.argv):
    arg = sys.argv[argi]
    if arg == "-f":
        file_name_arg = sys.argv[argi+1]
        argi += 2   # Pass to next flag index
    elif arg == "-p":
        pattern_arg = sys.argv[argi+1]
        argi += 2
    else:
        print("Don't recognize flag:", arg, "ignoring it plus value")
        argi += 2

# Default values     
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