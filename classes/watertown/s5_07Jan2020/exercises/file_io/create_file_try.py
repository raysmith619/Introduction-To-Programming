#create_file_try.py 20Oct2020  crs from create_file.py
"""
Do a little checking
"""
file_name = "my.txt"
file_name ="bad////file name"    # Force eror
try:
    with open(file_name, "w") as fout:
        for i in range(1,5):
            print(f"line {i}", file=fout)
except IOError as e:
    print(f"IOError with file {file_name}: {e}")
