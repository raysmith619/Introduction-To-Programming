# get_input.py 3Feb2020
"""
get_int function to retry if not integer
"""
def get_int(prompt=None):
    """ Get input, prompting with prompt provided
    Retry if incorrect input (not integer)
    :prompt: prompt string default: No prompt
    """
    while True:
        try:
            inp = input(prompt)
            num = int(inp)
            break
        except:
            print(inp, "is not a recognized integer, please try again")
    return num

# Self test used if this is the main (only) file executed
##
if __name__ == "__main__":        
    while True:
        num = get_int("Enter integer:")
        print("Number entered:", num)
