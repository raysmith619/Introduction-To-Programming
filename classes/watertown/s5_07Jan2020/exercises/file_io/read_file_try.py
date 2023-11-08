# read_file_try.py  15Oct2018
"""
Simple file read
with try/except to catch and report errors
"""
file_name = "my_second.txt"
file_name = "////my_second.txt"
try:
    with open(file_name) as finp:
        for line in finp:
            print(line, end="")
except IOError as e:
    print(f"Something wrong happened in file {file_name} {e}")
