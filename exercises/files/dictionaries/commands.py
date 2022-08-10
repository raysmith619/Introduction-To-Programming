# commands.py   08Aug2021  crs, Author
# Example of dictionay as command list

commands = {"up":1, "down":1, "left":1, "right":1}
for inp in ["up", "down", "in", "out"]:
    if inp in commands:
        print("Do cmd:", inp)
    else:
        print("input:", inp, "not in:", commands)
