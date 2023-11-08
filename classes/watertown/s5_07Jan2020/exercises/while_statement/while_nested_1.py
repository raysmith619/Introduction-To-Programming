#while_nested_1.py
var = 1
limit = 5
print("BEFORE: var:", var, "limit:", limit)
while var < limit:
    print("    BODY: var:", var, "limit:", limit)
    var2 = 2
    limit2 = 4
    print("    BEFORE2: var2:", var2, "limit2:", limit)
    while var2 < limit2:
        print("        BODY2: var2:", var2, "limit2:", limit2)
        var2 = var2 + 1
    print("    AFTER2: var2:", var2, "limit2:", limit2)
    var = var + 1
print("AFTER: var:", var, "limit:", limit)
