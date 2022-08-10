# motion.py 08Aug2021  crs, Author
"""
Simple motion commands
User inputs direction commands and the
picture changes
"""
cmds = {"up": 1, "down" : 1, "left" : 1,
        "right" : 1, "bye":1}
cmd_prev = "right"   # Last cmd
board_width = 5
board_height = board_width +1

"""
markers - for symetry make them the
same length
"""
empty = "."
full = "*"

"""
Initialize 2D array of empty cells
irow = Vertical down, starting at 0
icol = Horizontal to right, starting at 0
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

icol = 0   # Starting 0 based col,row values
irow = 0
while True:
    print_board()
    inp = input(f"Enter up,down,left, or right[{cmd_prev}]:")
    if inp == "":
        cmd = cmd_prev    # Repeat previous command
    else:
        cmd = inp.lower() # Make comparisons case insensitive
    if cmd not in cmds:
        print(f"I don't understand {cmd}")
        continue
    
    inewcol = icol        # Setup posible new location
    inewrow = irow
    if cmd == "up":
        inewrow  = irow - 1
    elif cmd == "down":
        inewrow = irow + 1
    elif cmd == "left":
        inewcol = icol - 1
    elif cmd == "right":
        inewcol = icol + 1
    elif cmd == "bye":
        print("Quitting")
        break

    # Check if new location is out of bounds
    if inewcol < 0 or inewcol >= board_width:
        print("col:",inewcol+1,
              "IS OUT OF BOUNDS") # Notify
        continue    # out of bounds
    
    if inewrow < 0 or  inewrow >= board_height:
        print("row:", inewrow+1,
              "IS OUT OF BOUNDS") # Notify
        continue    # out of bounds
    
    irow = inewrow  # Update location
    icol = inewcol
    board[irow][icol] = full    # Mark new location
    cmd_prev = cmd              # Record command
    
print("Good bye")
              

        
    
    
