# move_to_goal.py 26Aug2021  crs, Author
"""
Simple motion commands
User inputs direction commands and the
picture changes
"""
from random import randint

cmds = {"up": 1, "down" : 1, "left" : 1,
        "right" : 1, "bye":1}
cmd_prev = "right"   # Last cmd
board_width = 5
board_height = board_width +1

# Make the markers constant width,
# surrounding the symbols with
# white space so they stick out
# and don't visually interfere
# with any neighbors.
empty = " . "   # Indicates empty location
full =  " * "   # " traveled loc
start = " S "   # " starting point
goal =  " G "   # " goal point
goal_attained = "WON"   # Show found goal

# Tried to jazz it up
# with the following but
# couldn't get things to line up
### goal_attained = r"""😃"""

def print_board():
    """ Print board
    """
    for ir in range(board_height):
        for ic in range(board_width):
            print(board[ir][ic], sep="", end="")
        print()


# Starting/Goal settings
irow_start = randint(0, board_height-1)
icol_start = randint(0, board_width-1)
print(f"Start: row:{irow_start+1} col:{icol_start+1}") 
# Make the goal
# Insure the goal not the start
while True:
    irow_goal = randint(0, board_height-1)
    icol_goal = randint(0, board_width-1)
    if (irow_goal != irow_start
        or icol_goal != icol_start):
        break
print(f"Goal: row:{irow_goal+1} col:{icol_goal+1}") 
        
irow = 0    # Vertical down
icol = 0    # Horizontal to right

"""
Initialize 2D array of empty cells,
plus Start and Goal markers
"""
board = []  #list of rows, row is list of columns
#empty = (ir,ic)    #   TFD (Temporary for debugging)
for ir in range(board_height):
    row = []    # Build up next row
    for ic in range(board_width):
        if ir == irow_start and ic == icol_start:
            marker = start
        elif ir == irow_goal and ic == icol_goal:
            marker = goal
        else:
            marker = empty
        row.append(marker)
    board.append(row)   # Add row to board
        
irow, icol = irow_start, icol_start   # Starting location
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

    ir = irow       # Modify candidate location
    ic = icol
    if cmd == "up":
        ir  -= 1
    elif cmd == "down":
        ir += 1
    elif cmd == "left":
        ic -= 1
    elif cmd == "right":
        ic += 1
    elif cmd == "bye":
        print("Quitting")
        break
    
    if ic < 0 or ic >= board_width:
        print("col:",ic+1, "row:", ir+1,
              " Col OUT OF BOUNDS") # Notify
        continue    # out of bounds
    
    if ir < 0 or ir >= board_height:
        print("col:",ic+1, "row:", ir+1,
              " Row OUT OF BOUNDS") # Notify
        continue    # out of bounds

    irow = ir
    icol = ic
    
    if irow == irow_goal and icol == icol_goal:
        marker = goal_attained
        board[irow][icol] = marker
        print_board()
        print("Congratulation - you won!")
        break
    else:
        marker = full
    board[irow][icol] = full
    
print("Good bye")
              
r'''
Sample Output:
= RESTART: C:\Users\raysm\workspace\python\IntroductionToProgramming\presentation\Class_4_Classes_and_Dictionaries\homework\solutions\move_to_goal.py
Start: row:5 col:5
Goal: row:1 col:3
 .  .  G  .  . 
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  .  .  S 
 .  .  .  .  . 
Enter up,down,left, or right[right]:up
 .  .  G  .  . 
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  .  .  * 
 .  .  .  .  S 
 .  .  .  .  . 
Enter up,down,left, or right[up]:
 .  .  G  .  . 
 .  .  .  .  . 
 .  .  .  .  * 
 .  .  .  .  * 
 .  .  .  .  S 
 .  .  .  .  . 
Enter up,down,left, or right[up]:left
 .  .  G  .  . 
 .  .  .  .  . 
 .  .  .  *  * 
 .  .  .  .  * 
 .  .  .  .  S 
 .  .  .  .  . 
Enter up,down,left, or right[left]:
 .  .  G  .  . 
 .  .  .  .  . 
 .  .  *  *  * 
 .  .  .  .  * 
 .  .  .  .  S 
 .  .  .  .  . 
Enter up,down,left, or right[left]:up
 .  .  G  .  . 
 .  .  *  .  . 
 .  .  *  *  * 
 .  .  .  .  * 
 .  .  .  .  S 
 .  .  .  .  . 
Enter up,down,left, or right[up]:up
 .  . WON .  . 
 .  .  *  .  . 
 .  .  *  *  * 
 .  .  .  .  * 
 .  .  .  .  S 
 .  .  .  .  . 
Congratulation - you won!
Good bye
>>> 
'''
        
    
    
