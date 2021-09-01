# commands_redo_2.py   08Aug2021  crs, Author
# Example of dictionay as command list

commands = {"up":1, "down":1, "left":1, "right":1}
print("commands:", commands)
for inp in ["up", "down", "in", "out"]:
    if inp in commands:
        print("Do:", inp)
    else:
        commands_str = ",".join(commands) # join with separator
        print(inp, " is not in commands:", commands_str)

r'''
>>> 
= RESTART: C:\Users\raysm\workspace\python\
IntroductionToProgramming\exercises\dictionaries
\commands_redo_2.py
commands: {'up': 1, 'down': 1, 'left': 1, 'right': 1}
Do: up
Do: down
in  is not in commands: up,down,left,right
out  is not in commands: up,down,left,right
>>>
'''
