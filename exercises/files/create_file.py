#create_file.py 29Aug2021  crs, slight changes
#               29Dec2020  crs
with open("new_data.txt", "w") as fout:
    for n in range(1,5+1):
        print(f"line {n}")   # Print output copy
        print(f"line {n}", file=fout)

r'''
Sample Output:
= RESTART: C:\Users\raysm\workspace\
python\IntroductionToProgramming\
exercises\files\create_file.py
line 1
line 2
line 3
line 4
line 5
>>> 
Created File: new_data.txt:
line 1
line 2
line 3
line 4
line 5
'''
