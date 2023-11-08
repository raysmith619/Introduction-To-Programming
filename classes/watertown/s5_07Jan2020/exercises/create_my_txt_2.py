# create_my_txt2.py 12Nov2018
#                   19Sep2018
"""
Create my.txt file for class
"""
my_file = "my.txt2"
print("Creatng file", my_file)
with open(my_file, "w") as fout:
    for i in range(1,7+1):      # Note that range goes from 1 to end-1
        print("line %d" % i, file=fout)
