# motion.py 08Aug2021  crs, Author
"""
Simple motion commands
User inputs direction commands and the
picture changes
"""
cmds = {"up": 1, "down" : 1, "left" : 1,
        "right" : 1, "bye":1}
cmd_prev = "right"   # Last cmd
irow = 0    # Vertical down
icol = 0    # Horizontal to right
board_width = 5
board_height = board_width +1
empty = "."
full = "*"

"""
Initialize 2D array of empty cells
"""
board = []  #list of rows, row is list of columns
for ir in range(board_height):
    row = []    # Build up next row
    for ic in range(board_width):
        #empty = (ir,ic)    #   TFD (Temporary for debugging)
        row.append(empty)
    board.append(row)   # Add row to board

def print_board():
    """ Print board
    """
    for irow in range(board_height):
        for icol in range(board_width):
            print(board[irow][icol], sep="", end="")
        print()
        
while True:
    print_board()
    inp = input(f"Enter up,down,left, or right[{cmd_prev}]:")
    if inp == "":
        cmd = cmd_prev    # Repeat previous command
    else:
        cmd = inp.lower() # Make comparisons case insensitive
        cmd_prev = cmd
    if cmd not in cmds:
        print(f"I don't understand {cmd}")
        continue

    if cmd == "up":
        irow  -= 1
    elif cmd == "down":
        irow += 1
    elif cmd == "left":
        icol -= 1
    elif cmd == "right":
        icol += 1
    elif cmd == "bye":
        print("Quitting")
        break
    
    if icol < 0 or icol >= board_width:
        print("col:",icol+1, "row:", irow+1,
              " OUT OF BOUNDS") # Notify
        continue    # out of bounds
    
    if irow < 0 or irow >= board_height:
        print("col:",icol+1, "row:", irow+1,
              " OUT OF BOUNDS") # Notify
        continue    # out of bounds
    
    board[irow][icol] = full
    
print("Good bye")
              

        
    
    
