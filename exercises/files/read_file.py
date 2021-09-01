#read_file.py   29Dec2020
file_name = "my_data.txt"
with open(file_name) as finp:
    line_no = 0         # Keep track of line
    for line in finp:
        line_no += 1    # Bump each line
        print(line_no,line, end="")
