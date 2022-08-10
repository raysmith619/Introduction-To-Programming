# my_if_more.py    27Dec2021  crs - exercise if statement

print("my_if_more")
a = 1
b = 2
c = 3
i = 1
max = 5
while i < max:
    a = i
    print("i:", i, "a(", a, "):")
    if a != b:
        print("a(", a, ") != ", " b(", b, ")")
    if a < b:
        print("a(", a, ") < ", " b(", b, ")")
    if a % 2 == 0:
        print("a(", a, ") is even ")
    else:
        print("a(", a, ") is odd ")
    i = i + 1
