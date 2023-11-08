# open_file.py  31Oct2023  crs
# check file path
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
        open(file_name)
        print("Opened", file_name)
        default_file_name = file_name
    except:
        print(f"Can't open {file_name}")
        print("At", os.path.abspath(file_name))