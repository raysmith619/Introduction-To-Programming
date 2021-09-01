#everything_python_1.py == one line comment
"""
This solution was made a bit more wordy complex?
in hopes of making the output more instructive
"""
sep="\n" + "="*50 + "\n"  # To separate examples

print(sep, "Arithmetic operators: 1+2-3*4/5: ",
      1+2-3*4/5)

print(sep, "Variables:") 
a="a"
total = 10
customer_name = "Ray Smith"
print("a:","a",
      "total:", total,
      " customer_name:", customer_name)

print(sep, "Arithmetic: raise to power:",
      "2**4:", 2**4)

print(sep, "Comparison:",
      "2>2:", 2>1, "2<3", 2<3,
      "4==4:", 4==4, "5>4:", 5>4,
      "6<=7:", 6<=7, "8!=9")

print(sep, "Character strings:", "\"Ray:\":", "Ray",
      "'Smith':", 'Smith')

print(sep, "Multiline strings:")
print('''
"""
First line
Second line
Third line
""":''')
"""
First line
Second line
Third line
"""

print(sep)
print("String comparison:",
      ' "b">"a":', "b">"a",
      ' "cd"<"ce":', "cd"<"ce",
      ' "fg"=="fg":', "fg"=="fg",
      ' "hi">="h":', "hi">="h",
      ' "j"<="jk":', "j"<="jk",
      ' "lmn"!="lm":', "lmn"!="lm")

print(sep, "Variables:")
top = 10
client = "Ray"
salary_mth = 5000.0
print(" top:", top, " client:", client,
      " salary_mth:", salary_mth)

print(sep, "Variable name rules:")
first_name = "Ray"
print("Good:",
      "first_name:", first_name)
print("See everything_1_err_bad_name.py")

print(sep, "Assignment:")
a = 1
b = a + 1
print("a:", a, "b after b=a+1:", b)

print(sep, "String manipulation:",
      '"Ray" + " " + "Smith":',
      "Ray" + " " + "Smith")

print(sep, "print:",
      " Well we have seen enough examples of print")

print(sep, "Multiple statements on a line - use ';' :")
print("print(1); print(2):");print(1); print(2)
      
print(sep, "Syntax errors: see everything_1_err_syntax.py")

print(sep, "Decisions: if statement:")
print("""
if 2>2:
    print("2>1"):
""")
if 2>1:
    print("2>1")

print(sep, "Decisions: if with all outcomes: ",
"""
n = 2
if n > 3:
    print("n:", n, " matches if condition))
elif n > 2:
    print("n:", n, " matches this test"))
else:
    print("n:", n, " something other")
: """)
n = 2
if n > 3:
    print("n:", n, " matches if condition")
elif n > 2:
    print("n:", n, " matches this test")
else:
    print("n:", n, " something other")

print(sep, "Looping: while statement",
      """
n = 0
while n < 10:
    print(n)
    n = n +1
:""")
n = 0
while n < 10:
    print(n)
    n = n +1

print(sep, "Looping: for statement:",
      """
for n in range(10):
    print(n)
""")
for n in range(10):
    print(n)

print(sep, "Looping: alternative flow:",
      """
for n in range(10):
    if n < 2:
        continue    #  skip less than 2
    if n > 5:
        break  # quit loop if greater than 5
    print(n)
""")
for n in range(10):
    if n < 2:
        continue    #  skip less than 2
    if n > 5:
        break  # quit loop if greater than 5
    print(n)

print(sep, "List: group of things in order:")
print("""
list1 = [1, 2, 3, 4]
for n in list1:
    print(n)
""")
list1 = [1, 2, 3, 4]
for n in list1:
    print(n)

print(sep, """List: getting the nth item
        starting at 0 as first:""")
print("""
print("list1[2]:", list1[2])
""")
print("list1[2]:", list1[2])

print(sep, "List of strings:")
print("""
color_list = ["red", "orange", "yellow", "green"]
for color in color_list:
    print(color)
""")
color_list = ["red", "orange", "yellow", "green"]
for color in color_list:
    print(color)

print(sep, "List: adding item to end of list:")
print("""
color_list.append("indigo")
color_list.append("violet")
for color in color_list:
    print(color)
""")
color_list.append("indigo")
color_list.append("violet")
for color in color_list:
    print(color)

print(sep, "List: assignment:")
print("""
list2 = list1
print("list1:")
for c in list1: print(c, end=":")
print("\nlist2")
for c in list2: print(c, end=":")
""")
list2 = list1
print("list1:")
for c in list1: print(c, end=":")
print("\nlist2")
for c in list2: print(c, end=":")

print(sep, "List: removing last appended:")
print("""
end_elm = list1.pop()
print("list1.pop:", end_elm, "list1:", list1)
""")
end_elm = list1.pop()
print("list1.pop:", end_elm, "list1:", list1)

print(sep, "Convert character string to integer:")
print("""
val = "42"
print("val:", val, " val +1:",  int(val)+1)
""")
val = "42"
print("val:", val, " val +1:",  int(val)+1)
  
print(sep, "Get input from  user, via keyboard:")
print("""
inp = input("Enter Name:")
print("Entered:", inp)
""")
inp = input("Enter Name:")
print("Entered:", inp)

print(sep, "Turtle graphics")
print("""
from turtle import *
color("blue")
circle(100)
""")
print("Creating turtle window")
from turtle import *
color("blue")
circle(100)
print("See blue circle in new window.")    
      


      



