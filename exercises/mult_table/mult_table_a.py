#mult_table_a.py  22Sep2022  crs
""" Developing multiplication table
+ Asking for horzontal (m), vertical(n) min,max
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

m_min = get_in("horz start", m_min)
m_max = get_in("horz max", m_max)

print(f"Horizontal {m_min} to {m_max}")
    
