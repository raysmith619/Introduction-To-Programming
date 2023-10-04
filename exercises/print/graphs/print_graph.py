# print_graph.py    14Sep2023  crs, Author
x_len = 9
x_min = -x_len/2
x_max = x_len/2
marker = "x"
print("fun = x**2")
for x in range(x_len):
    fun = x**2
    for y in range(fun):
        print(marker, end="")
    print()
