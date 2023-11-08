#for_test.py 24Sep2020 crs


for i in range(5):
    print("i:", i)

for i in range(1,5):
    print("i:", i)
 
for i in range(1,5+1):
    print("i:", i)

print("Testing %") 
for i in range(1,5+1):
    if i % 2 == 0:
        continue
    print("i:", i)
   
