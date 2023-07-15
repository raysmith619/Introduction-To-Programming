# there_or_there.py
import os

"""
    Often the case is the file(s) may be in multiple places,
    some of which are not know until the program is executed.
    An example would be a directory of image files which
    exist in one location during development but a different
    location during production, neither of which may be directly
    related to the source code location
"""
pgm_dir = os.path.dirname(__file__)
data_dir = os.path.join(pgm_dir,"..","data")    # Sister
data_dir = os.path.abspath(data_dir)
while True:
    dadir = data_dir    # Candidate
    inp = input(f"Enter Data dir[{data_dir}]:")
    if inp != "":
        dadir = ""
    if not os.path.exists(dadir):
        print(f"{dadir} does not exist"
                f"\n   relative path: {os.path.relpath(pgm_dir, dadir)}"
                f"\n   at {os.path.abspath(dadir)}")
        continue
    
    if not os.path.isdir(dadir):
        print(f"{dadir} is not a directory"
                f"\n   relative path: {os.path.relpath(pgm_dir,dadir)}"
                f"\n   at {os.path.abspath(dadir)}")
        continue
    
    data_dir = dadir
    print(f"\nFound directory {data_dir}"
            f"\n   relative path: {os.path.relpath(data_dir,pgm_dir)}"
            f"\n   at {os.path.abspath(data_dir)}")
    break
        
file_name = "test_file.txt"
while True:
    inp = input(f"Enter File Name[{file_name}]:")
    fname = file_name       # Adjusted if appropriate
    if inp != "":
        fname = inp     # Use input
    file_path = fname   # Changed, if appropriate
    if not os.path.isabs(file_path):
        file_path = os.path.join(data_dir,fname)
        
    if not os.path.exists(file_path):
        print(f"Can't find file: {fname}"
            f"\n   relative path: {os.path.relpath(__file__,file_path)}"
            f"\n at {os.path.abspath(file_path)}")
        continue

    print(f"File: {fname}"
        f"\n   relative path: {os.path.commonpath([__file__,file_path])}"
        f"\n at {os.path.abspath(file_path)}"
        f"\n exists")
    break

print(f"\nListing file: {file_name}")
with open(file_path) as fp:
    ln = 0
    for line in fp.readlines():
        ln += 1
        print(f"{ln:3}: {line}", end="")
        
