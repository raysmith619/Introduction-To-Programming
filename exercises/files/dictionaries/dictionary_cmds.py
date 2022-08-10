#dictionary_cmds.py 03Oct2021  crs, from slide 4
#
#Dictionary  - As cmd list
commands = {"up":1, "down":1, "left":1, "right":1}

for inp in ["up", "down", "in", "out"]:
    if inp in commands:
        print("Do cmd:", inp)
    else:
        print("input:", inp, "not in:", commands)
