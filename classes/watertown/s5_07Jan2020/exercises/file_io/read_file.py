#read_file.py   29Dec2020
file_name = "my.txt"
with open(file_name) as finp:
    for line in finp:
        print(line, end="")
