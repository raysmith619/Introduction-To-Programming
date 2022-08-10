# my_break.py    27Dec2021  crs - exercise break,continue

print("my_break")
i = 0
max = 7
while i < max:
    i = i + 1   # Always insure bumping
    print("i(", i, ")")
    if i % 5 == 0:
        print("Restart loop at i:", i, "via continue")
        continue
    
    if i % 6 == 0:
        print("Force loop stoping at 6")
        break
    if i % 2 == 0:
        print("i(", i, ") is even")
    if i % 3 == 0:
        print("i(", i, ") is divisible by 3")
    if i % 5 == 0:
        print("i(", i, ") is divisible by 5")
        
