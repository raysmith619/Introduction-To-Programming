# if_elif_else.py
x = 3
y = 4
print("x:", x, "y:", y)
print("\nif x > y:")
if x > y:
        print("x:", x, "y:", y, "if x > y => if PASSED")
elif x+1 > y:
        print("x+1:", x+1, "y:", y, "x+1 > y => elif executed")
else:
        print("x:", x, "y:", y, "=> else executed")
