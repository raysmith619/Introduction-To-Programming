#comprehension.py   09Aug2021  crs, Author

irow = 0    # Horizontal to right
icol = 0    # Vertical down
board_width = 5
board_height = board_width+1
empty = "."
full = "*"

"""
Initialize 2D array of empty cells
This uses an advanced list feature for
constructing lists.  One could use a more
tratidional two level for / while loop but I
was lazy.
"""
board = [[(irow,icol) for icol in range(board_width)]
           for irow in range(board_height)]

def print_board():
    """ Print board
    """
    print("(irow,icol)")
    for irow in range(board_height):
        for icol in range(board_width):
            print(board[irow][icol], sep="", end="")
        print()

    print("\nboard:", board)    
    print("\nirow, row")
    for irow in range(board_height):
        print(irow,board[irow])

print_board()
