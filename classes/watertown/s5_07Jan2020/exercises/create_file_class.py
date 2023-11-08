# create_file_class.py  25Jul2018
"""
Simple file creation
"""
file_name = "my_second.txt"
with open(file_name, "w") as fout:
    print(f"# {file_name}")
    print(f"# {file_name}", file=fout)

    for i in range(1,10+1):
        print(f"write out: line {i}")
        print(f"line {i}", file=fout)
