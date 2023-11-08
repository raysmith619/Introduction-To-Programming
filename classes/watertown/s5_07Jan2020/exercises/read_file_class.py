# read_file_class.py  15Oct2018
"""
Simple file read
"""
file_name = "my_second.txt"
try:
    with open(file_name) as finp:
        for line in finp:
            print(line, end="")
except:
    print(f"Something wrong happened in open({file_name})")
