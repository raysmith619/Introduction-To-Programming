#add2.py 11Jan2022  crs, simple function example
def add2(value1,value2):
    """ Add two numbers
    :value1: first addend
    :value2: second addend
    :retuns: sum of value1 and value2
    """
    return value1 + value2

print("Testing add2")
sum = add2(1,2)
print("sum:", sum)
a = 1000
b = 2000
print("sum:","a:", a, "b:", b, "add2:", add2(a,b))
a=1
b=2
print("sum:","a:", a, "b:", b, "add2:", add2(a,b))
a=3
b=4
print("sum:","a:", a, "b:", b, "add2:", add2(a,b))
a=99
b=100
print("sum:","a:", a, "b:", b, "add2:", add2(a,b))

    
