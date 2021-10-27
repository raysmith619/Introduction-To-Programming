#read_file_old.py   13Oct2021, crs from read_file.py
# Older fashion
file_name = "my_data.txt"
finp = open(file_name)
line_no = 0         # Keep track of line
for line in finp:
    line_no += 1    # Bump each line
    print(line_no,line, end="")
