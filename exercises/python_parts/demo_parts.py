#demo_parts.py  02Oct2023  crs, Author
"""Support to facilitate demonstration of simple python
language parts
"""
def vals(*vals):
    """ Print strings followed by evaluations
    :vals: zero or more expressions
            if val is str just print string
            else print string followed by the value of the
            string evaluated as an expression
    """
    vals_str = ""
    for val in vals:
        if vals_str != "":
            vals_str += ", "
        vals_str += str(val) 
        try:
            val_val = eval(val)
            vals_str += ": " + str(val_val)
        except:
            pass
    print(vals_str)

if __name__ == "__main__":
    print("Testing", __name__)
    vals("Selftest")
    vals("1+1", "2*2", "3**3")
    a = 1
    b = 2
    c = 2
    vals("a+b", "a", "b")
    vals("c=a+b", "a", "b", "c")