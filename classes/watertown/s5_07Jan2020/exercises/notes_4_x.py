# notes_4.py  26-Jul-2018
"""
Support multiple patterns:
 pat1 [& pat2 [& pat3 ...]] - must contain pat1 AND pat2 AND pat3 ...
 pat1 [| pat2 [| pate ...]] - must contain pat1 OR pat2 OR pat3 ...

 Interpretation:
     & pat_N ==> If pat_N is not in line => Don't print line
     | pat_N ==> If pat_N is present and no "& pat" are missing print line

     patterns have no embeded white space
 

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
import re

# Default values
def_file_name = "test.notes"
def_pattern = "student"

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
 



inp = input("Enter pattern[" + pattern + "] ")
inp = inp.rstrip()
if inp == "":
    inp = pattern
pattern = inp
"""
looking for
    begining of string
    or white space
    or &
    or |
    followed by group of non-(&|) characters
    We accept zero or more whitespace characters to preceed and
    follow the beginning character
"""
if pattern.find('&') < 0 and pattern.find('|') < 0:
    pats = []
    pat_list = pattern.split()          # all space separated
    for pat in pat_list:
        pats.append(('&', pat))
else:
    pats = re.findall(r'\s*(^|[\s&|])\s*([^&|]+)', pattern)
    
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
