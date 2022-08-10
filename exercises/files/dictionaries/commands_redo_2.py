# commands_redo_2.py   27Feb2022  crs, Author
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
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\raysm\workspace\python\IntroductionToProgramming\exercises\dictionaries\commands_redo_2.py
commands: {'up': 1, 'down': 1, 'left': 1, 'right': 1}
Do: up
Do: down
in  is not in commands: up,down,left,right
out  is not in commands: up,down,left,right
'''
