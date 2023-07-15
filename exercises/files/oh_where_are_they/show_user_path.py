# show_user_path.py
import os

file_name = "test_file.txt"
inp = input(f"Enter File Name[{file_name}]:")
if inp != "":
    file_name = inp     # Use input
if not os.path.exists(file_name):
    print(f"Can't find file: {file_name}"
          f"\n at {os.path.abspath(file_name)}")
else:
    print(f"File: {file_name}"
          f"\n at {os.path.abspath(file_name)}"
          f"\n exists")

