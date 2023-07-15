# first_reduction.property
import os

file_name = "test_file.txt"
if not os.path.exists(file_name):
    print(f"Can't find file: {file_name}")
else:
    print(f"File: {file_name} exists")

