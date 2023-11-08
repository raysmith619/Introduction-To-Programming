# create_my_txt.py  19Sep2018
"""
Create my.txt file for class
"""
my_file = "my.txt2"
with open(my_file, "w") as fout:
    for i in range(1,5+1):      # Note that range goes from 1 to end-1
        print("line %d" % i, file=fout)
