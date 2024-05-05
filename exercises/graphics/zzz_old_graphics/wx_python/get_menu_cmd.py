# get_menu_cmd  15Jun2023  crs, Author
"""
Translate event call into two value call

"""
fn_num = 0      # Track instances

def get_menu_cmd(proc=None, hi=0, ddj=0):
    """ Returns event function fn(e=0, h=hi, d=ddj)
    which, when called fn(e), calls proc(hi=hi, ddj=ddj
    :proc: function to call via (proc(hi=hi, ddj=ddj)
    :hi: value to pass as hi
    :ddj: value to pass as ddj
    """
    global fn_num
    fn_num += 1
    def fn(e=None):
        """ Event function called with optional unused parameter e
        :e: optional event object
        """
        fn_num_n = fn_num
        print(f"fn: called {fn_num_n} {fn} hi: {hi}, ddj: {ddj}")
        proc(hi=hi, ddj=ddj)


    print(f"get_menu_cmd: {fn_num} fn:{fn} hi:{hi} ddj:{ddj}")
    return fn

if __name__ == "__main__":
    menu_lst = ["One", "Two", "Three", "Four","Five"]
    sub_lst = ["A", "B", "C", "D"]


    def menu_command(hi=0,ddj=0):
        """Generic Menu command
        :hi: heading index (no index guard)
        :ddi: drop-down index (no index guard)
        """
        print(f"Self Test menu_command({menu_lst[hi]},{sub_lst[ddj]})")

    def testit(proc=menu_command, hi = 0, ddj = 0):
        print(f"\ntesting: hi={hi}, ddj={ddj}")
        menu_cmd = get_menu_cmd(proc=proc, hi=hi, ddj=ddj)
        menu_cmd()

    testit(hi=1, ddj=1)
    testit(hi=2, ddj=2)
    testit(hi=3, ddj=3)
    testit(hi=3, ddj=2)



