# file_search.py    11Aug2021  crs, from read_file_try.py

"""
Simple file search/scan similar to simple UNIX/Linux grep
 1. Loop over files/strings
"""
prev_name = "REQUIRED"
prev_search_string = "REQUIRED"
while True:
    file_name = input(f"Enter File Name [{prev_name}]:")
    if file_name == "":
        file_name = prev_name
    if file_name == "REQUIRED":
        continue        # Try again
    
    prev_name = file_name       # Remember as default
    search_string = input(f"Enter search string[{prev_search_string}]:")
    if search_string == "":
        search_string = prev_search_string
    if search_string == "REQUIRED":     # What if we want to search
                                        # for "REQUIRED" ?
        continue    # Ignore empty search string
    prev_search_string = search_string
    
    try:
        with open(file_name) as finp:
            for lineno, line in enumerate(finp, start=1):
                if line.find(search_string) > -1:
                    print(f"{lineno:3}: {line}", end="")
    except IOError as e:
        print(f"Something wrong happened in file {file_name} {e}")

r'''
= RESTART: C:/Users/raysm/workspace/python/
IntroductionToProgramming/presentation/Class_5_Files
/homework/solutions/file_search.py
Enter File Name [REQUIRED]:file_search.py
Enter search string[REQUIRED]:while
  9: while True:
Enter File Name [file_search.py]:
Enter search string[while]:if
 11:     if file_name == "":
 13:     if file_name == "REQUIRED":
 18:     if search_string == "":
 20:     if search_string == "REQUIRED":     # What if we want to search
 28:                 if line.find(search_string) > -1:
Enter File Name [file_search.py]:../../../../exercises/files/read_file_try.py
Enter search string[if]:try
  1: # read_file_try.py  15Oct2018
  4: with try/except to catch and report errors
  8: try:
Enter File Name [../../../../exercises/files/read_file_try.py]:

'''
