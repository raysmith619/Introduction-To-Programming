#create_file.py 29Dec2020  crs
with open("my.txt", "w") as fout:
    for i in range(1,5):
        print(f"line {i}", file=fout)
