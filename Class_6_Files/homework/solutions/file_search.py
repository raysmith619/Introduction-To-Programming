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
    
    search_string = input(f"Enter search string[{prev_search_string}]:")
    if search_string == "":
        search_string = prev_search_string
    if search_string == "REQUIRED":     # What if we want to search
                                        # for "REQUIRED" ?
        continue    # Ignore empty search string
    prev_search_string = search_string
    
    lineno = 0          # Line number, bumped before each
    try:
        with open(file_name) as finp:
            prev_name = file_name       # Remember as default
            for line in finp:
                lineno += 1
                if line.find(search_string) > -1:
                    print(f"{lineno:3}: {line}", end="")
    except IOError as e:
        print(f"Something wrong happened in file {file_name} {e}")

