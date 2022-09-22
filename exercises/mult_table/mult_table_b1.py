#mult_table_b1.py  22Sep2022  crs
""" Developing multiplication table
+ Asking for horzontal (m), vertical(n) min,max
+ Simple table, no formatting
+ Using formatted string give max space to align
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
print(f"Vertical {n_min} to {n_max}")
print("Multiplication Table  "
      f"{m_min} to {m_max} by {n_min} to {n_max}")

max_width = max(len(str(n_min*m_min)),
                len(str(n_min*m_max)),
                len(str(n_max*m_min)),
                len(str(n_max*m_max)))  # Assume max len

for n in range(n_min, n_max+1): # Vert n_min to n_max
    for m in range(m_min, m_max+1): # Horz m_min to m_max
        prod = n*m
        print(f"{prod:{max_width}} ", end="")
    print()         # End of line
    
