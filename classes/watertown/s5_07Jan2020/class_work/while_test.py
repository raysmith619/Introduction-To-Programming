#while_test.py 24Sep2020 crs

i = 1
while i < 5:
    print("i:", i)
    i = i + 1

i = 1
while True:
    print("i:", i)
    if i > 4:
        print("i:", i, "breaking out (i>4)")
        break
    i += 1       # same as i = i + 1
    
