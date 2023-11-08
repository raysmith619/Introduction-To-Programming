# read_my_txt_trim.py  19Sep2018
"""
Read my.txt file for class
Stripping off trailing whitespace (including newline)
"""
file_name = "my.txt"
with open(file_name) as finp:
    for line in finp:
        line = line.rstrip()
        print(line)
