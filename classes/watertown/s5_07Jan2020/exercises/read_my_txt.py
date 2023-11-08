# read_my_txt.py  19Sep2018
"""
Read my.txt file for class
"""
file_name = "my.txt"
with open(file_name) as finp:
    for line in finp:
        print(line)
