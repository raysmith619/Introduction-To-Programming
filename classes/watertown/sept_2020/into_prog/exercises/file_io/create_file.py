#create_file.py
with open("my.txt", "a") as fout:
    for i in range(1,5):
        print(f"line {i}", file=fout)
