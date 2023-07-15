# help_user_path.py
import os

"""
    ONLY as a suggestion, let's assume the user,
    unless specifying an absolute file path, expects
    the file to be in the directory of, or relative to the
    program's directory.     
"""
file_name = "test_file.txt"
inp = input(f"Enter File Name[{file_name}]:")
if inp != "":
    file_name = inp     # Use input
file_path = file_name   # Changed, if appropriate
if not os.path.isabs(file_path):
    pgm_dir = os.path.dirname(__file__)
    file_path = os.path.join(pgm_dir,file_name)
    
if not os.path.exists(file_path):
    print(f"Can't find file: {file_name}"
          f"\n at {os.path.abspath(file_path)}")
else:
    print(f"File: {file_name}"
          f"\n at {os.path.abspath(file_path)}"
          f"\n exists")

