#while_nested_simple_1.py
var = 1
limit = 5
while var < limit:
    var2 = 2
    limit2 = 4
    print("var:", var)
    while var2 < limit2:
        print("var:", var, "var2:", var2)
        var2 = var2 + 1
    var = var + 1
