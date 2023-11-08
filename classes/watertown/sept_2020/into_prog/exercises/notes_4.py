# notes_4.py  26-Jul-2018
"""
Support multiple patterns:
 1. nospacepat1 nospacpat2 .... == all patterns must be in line
 2. [|&] nospacepat1 nospacepat2 ... == | any of the pat, & all of the pat
 3. pat1 [&|] pat2 [&|] pat3 ... all & pats plus, if any | atleast one of | pat

Write a "Notes" program. The program will display lines
from a text file, containing a given text string.
Test:
file name = "people.notes"
text = "Watertown"
 Implementation Iterations:
Setup test file(s): "test.notes",  "people.notes"
    1.	Read specific file e.g. "test.notes", printing out all lines
    2.	Print only lines containing "student"
            How to match lines ? Google "python search for substring" ?
            Support case insensitive match (Student, STUDENT)
    3.	Prompt for, then accept file name, pattern
    4.	[Extra Credit]  Support multiple text patterns

"""
import re            # Support Regular Expression Pattern Searching

# Default values
def_file_name = "test.notes"
def_pattern = "student"

#########################################################################
# Utility Functions                                                     #
# NOTE: Python requires function definitions come before function calls #
#########################################################################


"""
Search file with pattern
"""
def search_pat(file_name, pattern):
    finp = open(file_name)      # Assume no error since we have just succeeded
    def_pat_type = '&'
    # Use the leading marker, if any as the default choice OR, AND
    if len(pattern) > 0:
        ind = pattern[0]
        if ind == '&':
            def_pat_type = ind
            pattern = pattern[1:]
        elif ind == '|':
            def_pat_type = ind
            pattern = pattern[1:]

    # Check if rest of line is devoid of markers
    if pattern.find('&') < 0 and pattern.find('|') < 0:
        pats = []
        pat_list = pattern.split()          # all space separated
        for pat in pat_list:
            pats.append((def_pat_type, pat))
    else:
        pats = re.findall(r'\s*([|&])\s*([^&|]*)', pattern)        
        
    or_pats = []            # | pat - accept if no and pat missing        
    and_pats = []           # & pat - accept only if present

    def_pat_type = '&'      # Default type
    if pattern.find('|') >= 0:
        def_pat_type = '|'      # If we find | we make the default
        
    for ind, pat in pats:
        if ind == '|':
            def_pat_type = ind
            or_pats.append(pat)
        elif ind == '&':
            and_pats.append(pat)
            def_pat_type = ind
        else:
            if def_pat_type == '|':    # treat as default type
                or_pats.append(pat)
            else:
                and_pats.append(pat)

    pattern_lc = pattern.lower()    # Force pattern to lower case
    for line in finp:
        line = line.rstrip()        # All trailing white space
        line_lc = line.lower()
        and_found = 0
        or_found = 0
        for and_pat in and_pats:
            if line_lc.find(and_pat)  >= 0:
                and_found += 1
        for or_pat in or_pats:
            if line_lc.find(or_pat) >= 0:
                or_found += 1
        if len(and_pats) > 0:
            if and_found == len(and_pats):
                if len(or_pats) > 0:
                    if or_found > 0:
                        print(line)     # At least one of the ors
                else:
                    print(line)         # No ors to check
        elif or_found > 0:
            print(line)

################################################
#               End of Utility Functions       #
################################################


# Set to default values
pattern = def_pattern

while True:
    file_name = def_file_name
    inp = input("Enter file name[" + file_name + "] ")
    inp = inp.rstrip()
    if inp == "":
        inp = file_name
    file_name = inp
    try:
        finp = open(file_name)
        break               # Got opened file
    
    except IOError :
        print("Can't open file ", file_name)
    inp.close()         # So we can reopen

# Loop over patterns until &&& to quit
quit_sign = "&&&"
while True:
    inp = input("Enter pattern[" + pattern + "] " + quit_sign + " to quit: ")
    inp = inp.lstrip().rstrip()
    if inp == quit_sign:
        break
    
    if inp == "":
        inp = pattern
    pattern = inp
    search_pat(file_name, pattern)
