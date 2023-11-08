# open_file.py  06Nov2023  crs, from open_file.py 
#               31Oct2023  crs
# check file path
# list file
import os

cwd = os.getcwd()
print(f"\ncurrent directory: {cwd}")   # f before quotes expands {value} in quotes

src_dir = os.path.dirname(__file__)
print(f"\nfile directory: {src_dir}")

if cwd.lower() != src_dir.lower():
    print("Changing directory to src dir")
    os.chdir(src_dir)
    
default_file_name = "open_file.py"
while True:
    inp = input(f"Enter file[{default_file_name}]:")
    if inp == "":
        inp = default_file_name
    file_name = inp
    try:
        finp = open(file_name)
        print("Opened", file_name)
        default_file_name = file_name
        break       # got file - go on
    except:
        print(f"Can't open {file_name}")
        print("At", os.path.abspath(file_name))
        
# list opened file
with open(file_name) as finp:
    line_no = 0     # Bump before each line
    for line in finp:
        line_no += 1
        print(line_no, line, end="")     # Lines already have endings
     