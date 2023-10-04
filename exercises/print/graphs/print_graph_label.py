# print_graph_label.py    14Sep2023  crs, Author
x_len = 9
x_min = -x_len/2
x_max = x_len/2
marker = "x"
spacer = "-"
print("fun = x**2")
for x in range(x_len):
    f_x = x**2
    print(x, f_x, sep=" ", end= " ",)
    for y in range(f_x):
        print(marker, end="")
    print()
