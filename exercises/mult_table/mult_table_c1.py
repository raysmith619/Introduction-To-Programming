#mult_table_c1.py  22Sep2022  crs
""" Developing multiplication table
+ Asking for horzontal (m), vertical(n) min,max
+ Simple table, no formatting
+ Using formatted string give max space to align
+ Provide top legend
+ Add left legend

"""
m_min = 1       # horizontal multiplicand
m_max = 5
n_min = m_min   # vertical
n_max = m_max

def get_in(prompt=None, default=None):
    """ Get keyboard input, prompting with default
    :prompt: optional prompt default: no prompt
    :default: optional default value
    """
    if prompt is not None:
        if default is not None:
            prompt = f"{prompt} [{default}]:"
    inp = input(prompt)
    if inp == "":
        inp = str(default)
    ret = int(inp)
    return ret

print("Multiplication Table Ranges")
m_min = get_in("horz start", m_min)
m_max = get_in("horz max", m_min+5)
print(f"Horizontal {m_min} to {m_max}")

n_min = get_in("vert start", m_min)
n_max = get_in("vert max", m_max)
print(f"Vertical {m_min} to {m_max}")
print("Multiplication Table  "
      f"{m_min} to {m_max} by {m_min} to {m_max}\n")

max_width = max(len(str(n_min*m_min)),
                len(str(n_min*m_max)),
                len(str(n_max*m_min)),
                len(str(n_max*m_max)))  # Assume max len
max_n_width = max(len(str(n_min)),len(str(n_max)))
                      
opr = "*"
for n in range(n_min, n_max+1): # Vert n_min to n_max
                                
    if n == n_min:                      # Legend at top
        print(f"{opr:^{max_n_width}} ", end="") #  room for left legend
        for m in range(m_min, m_max+1): # Horz m_min to m_max
            prod = n*m
            print(f"{m:{max_width}} ", end="")
        print()
        print(f"{' ':^{max_n_width}}.", end="") #  room for left legend
        for m in range(m_min, m_max+1): # Horz m_min to m_max
            prod_und = max_width*"-"
            print(f"{prod_und} ", end="")
        print()                         # End of top legend
    for m in range(m_min, m_max+1): # Horz m_min to m_max
        if m == m_min:                  # Left legend
            print(f"{n:{max_n_width}}|", end="")
        prod = n*m
        print(f"{prod:{max_width}} ", end="")
    print()         # End of line
    
