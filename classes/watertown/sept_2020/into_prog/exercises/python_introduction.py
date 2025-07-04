Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> # The following is an interactive introduction to basic Python concepts.
>>> # The text is pretty much as I typed it in to the Python IDLE shell,
>>> # and got printed out by the shell python shell evaluation.

>>> # You might get some useful practice by trying these examples on your
>>> # computer in the IDLE shell.
>>> # Lines with # are ignored by python from the # character to line end.
>>> # This introduction takes place within the python IDLE interpreter

>>> # Lines starting with ">>> " can be directly typed, minus the ">>> ", into
>>> # IDLE
>>> # Text typed after the ">>> " are evaluated by python, and the value,
>>> #  if any, is displayed.
>>> 1
1
>>> 1 + 2
3
>>> # One of the most basic features of python are numbers such 1, 2, 10, 3.2.
>>> # Along with number are arithmetic operators such as + for add
>>> # - for subtraction, * for multiplication, / for division,
>>> # ** for exponentiation, % for modulous(remainder), plus others.
>>> 2 + 3
5
>>> 2*3
6
>>> 2-1
1
>>> 2/2
1.0
>>> 2**3    # 2 raised to the 3 power: 2*2*2
8
>>> 5%2     # remainder of 5 divided by 2
1
>>> # OPTIONAL EXERCISE / CONTEST:
>>> # "Four Fours" : Using exactly 4 number 4 plus any legal operators
>>> #                or non-numeric/alphabetic sympols .e.g +,-,*,.,
>>> #                create the numbers 1, 2, 3, ..., in order as high as you can go.
>>> # A start:
>>> 44/44
1.0
>>> 4*4/(4+4)
2.0
>>> (4+4+4)/4
3.0
>>> (4-4)*4+4
4


>>>
>>> # One can do multiple things on a line by separating them
>>> # with semicolons (;)
>>> 1;2;4
1
2
4
# One may combine expressions on a line with separating commas:
>>> 2+3,2*3,2-1,2**3,5%2
(5, 6, 1, 8, 1)
>>> 
>>> # Another feature of python is the string.  The string is a sequence of
>>> # characters such as a,b,c or -,=,#. To indicate that this
>>> # sequence of characters is a list of characters,  one must surround the
>>> # sequence with matching markers.
>>> # The string markers may be a single double quote ("), a single single
>>> # quote ('), a tripple double quote ("""), or a tripple single quote (''').

>>> # Without the markers (",', ''', or """), Python thinks the characters
>>> # make up something else, such as a language word, variable name
>>> # or operation.
>>> "abc"
'abc'
>>> "def ghi"
'def ghi'
>>> "!@#$%^&*()_+"
'!@#$%^&*()_+'

>>> # Strings can be joined or concatinated by using "+"
>>> "Ray" + " " + "Smith"
'Ray Smith'

>>> # Normally strings MUST be on a single line
>>> # Multi-line strings may be created by using """ or ''' markers.
>>> # The string starts from the first marker (""" or ''') and
>>> # continues to the next MATCHING marker (""" or ''').
>>> """Possible multiline
string"""
'Possible multiline\nstring'
>>> # The "\n" in the above printout is python's abreviation of a "newline"
>>> # (line separator)

>>> # print - print out text, by default, to the screen
>>> # Unlike the python IDLE shell, whose default action
>>> # is to print each expression evaluated, normal python programs require
>>> # using the function "print" to print to the screen.

>>> # To print one or more values to the screen one may use print.
>>> # The format is:
>>> # print(...a comma separated set of values...)
>>> print(1,2,3)
1 2 3
>>> print("abc", "def", "ghi", 1, 2, 3)
abc def ghi 1 2 3

>>> # The values to print may be constants e.g. 1, "a", "a string"
>>> print(1, "a", "a string")
1 a a string
>>> # The values to print can be expressions, e.g. 1+2+3
>>> print(1+2+3)
6
>>> # Variables
>>> # In programming, python in particular, it is often very useful to have
>>> # places to store values which can be used later.
>>> # Usually, it is helpful that these places have names.  In general,
>>> # the function of a variable, is to contain a value, for later use.
>>> # The value is obtained at a later time by using the variable's name.

>>> # Variable names MUST
>>> #   1. start with a letter "a" through "z" or "_" and continue
>>> #      with letters "a"-"z", "0"-"9", or "_".
>>> #   2. NO other characters, such as spaces, periods, dashes,...
>>> #      are allowed
>>> # Variables are defined and initialized (provided with values) with
>>> # a statement of the form:
>>> #	<variable name> = <value>
>>> a_name = 123
>>> a_name
123
>>> a_string_var = "this is a string."
>>> a_string_var
'this is a string.'
>>> a = 1
>>> b = 2
>>> a + b
3
>>> # Illegal variable names - Can you tell why?
>>> 1 = 2
SyntaxError: can't assign to literal
>>> 1a = 2
SyntaxError: invalid syntax
>>> a b = 2
SyntaxError: invalid syntax
>>> a-b = 2
SyntaxError: can't assign to operator
>>> 
>>> print(a+b)
3
>>> # If one uses a variable name which has NOT YET been initialized (set to
>>> # value), one will usually get an error:
>>> not_yet_initialized
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    not_yet_initialized
NameError: name 'not_yet_initialized' is not defined
>>> 
>>> # if - testing
>>> # After simple calculations, the most useful computer programming operation
>>> # is decision making - testing for a condidition and doing different
>>> # things depending on the test results.
>>> # The most basic programming test uses the "if", "else", or "elif" key
>>> # words.
>>> # The form is:
>>> # if <testing condition>
>>> #     <indented code lines which get executed IF the <testing condition>
>>> #     is True>
>>> # NOTE: IDLE "guesses" and often indents for you
>>> n = 1
>>> if n == 1:
	print("n is 1")

n is 1
>>> n = 2
>>> if n > 0:
	print(n, "is greater than", 0)
	print("Another line executed if test passed")


2 is greater than 0
Another line executed if test passed
>>> # The "else" clause (indented lines following the "else:" line
>>> # is executed ONLY IF <testing condition> is False
>>> if n > 0:
	print("n is greater than 0")
	print("n is", n)
else:
	print("n is NOT greater than 0")
	print("n is", n)

	
n is greater than 0
n is 2

>>> if n > 1:
	print("n is greater than 1")
else:
	print("n is NOT greater than 1")

	
n is NOT greater than 1

>>> n = 0       # Change n so same test gives different result
>>> if n > 0:
	print("n is greater than 0")
	print("n is", n)
else:
	print("n is NOT greater than 0")
	print("n is", n)


n is NOT greater than 0
n is 0

>>> # "elif" is a python language short hand to facilitate making a list
>>> # of exclusive tests:
>>> val = "who"
>>> if val == "what":
	print("val is", val)
	print("but I don't know")
elif val == "where":
	print("val is", val)
	print("maybe")
elif val == "who":
	print("val is", val)
	print("I was about to give up!")
else:
	print("val is", val)
	print("I just don't know")

	
val is who
I was about to give up!
>>> 
>>> # while - Life is repleate with loops - programming is part of life
>>> # The simplest looping construct of python uses the "while" key word.
>>> # The form is:
>>> #	while <condition>:
>>> #       <indented lines which are executed
>>> #        repeatedly, once after each test condition
>>> #        passes>
>>> #
>>> start = 0
>>> val = start
>>> end = 5
>>> while val < end:
	print("val is", val)
	val = val + 1
	
val is 0
val is 1
val is 2
val is 3
val is 4
>>> print("Got to end, val is ", val)
Got to end, val is  5

>>> # Test conditions, used in if, and while statements may be
>>> # any expression that produces a boolean (True or False) result
>>> # including:
>>> # Comparisons: a == b, a != b, a > b, a < b, a >= b, a or b, a and b
>>> a = 1
>>> b = 2
>>> a == b, a != b, a > b, a < b, a >= b
(False, True, False, True, False)
>>> a = True
>>> b = False
>>> c = True
>>> a == b, a != b, a > b, a < b, a >= b, a or b, a and b
(False, True, True, False, True, True, False)
>>> not True
False
>>> 0 == False     # Just for cureosity, not good practice
True
>>> 1 == True
True
>>> True + True
2

>>> # Other ways to change looping
>>> # "break" - stop loop right now
>>> # "continue" - continue loop at next iteration
>>> n = 0
>>> while True:
	n = n + 1
	print("n is", n)
	if n % 2 == 0:	# Use remainder operator
		print("n % 2 == 0:n is", n)
		print("continue")
		continue
	if n % 3 == 0:
		print("n % 3 == 0:n is", n)
		print("continue")
		continue
	if n % 7 == 0:
		print("n % 7 == 0:n is", n)
		print("break")
		break

	
n is 1
n is 2
n % 2 == 0:n is 2
continue
n is 3
n % 3 == 0:n is 3
continue
n is 4
n % 2 == 0:n is 4
continue
n is 5
n is 6
n % 2 == 0:n is 6
continue
n is 7
n % 7 == 0:n is 7
break
>>>
>>> # inp("Enter guess:") - Soliciting user input from keyboard
>>> inp = input("Please Enter your guess, followed by the ENTER key:")
Please Enter your guess, followed by the ENTER key:123
>>> print("inp is", inp)
inp is 123
>>> 
>>> # Converting string of characters to an integer using int()
>>> # NOTE: inp, returned from inp(), is NOT an integer:
>>> inp
'123'
>>> inp == 123
False
# String '123' is not equal to integer 123

>>> inp + 1
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    inp + 1
TypeError: can only concatenate str (not "int") to str
# Previous error caused because python does not do arithmetic (e.g. addition)
# between strings such as '123' and integers

>>> guess = int(inp)    # Converting string ('123') to integer(123)
>>> guess
123
>>> guess == 123        # guess is an integer (123)
True
>>> guess + 1
124
>>> # Lists - an ordered grouping of things
>>> # Many programming languages use the concept of
>>> # an array for this purpose.
>>> # Python lists are more powerful
>>> list1 = [1,2,3,4]
>>> list1
[1, 2, 3, 4]
>>> list1[2]
3
>>> list1[2]    # Numbered, starting with 0
3
>>> list2 = [6,7,8]
>>> list2
[6, 7, 8]
>>> list1 + list2
[1, 2, 3, 4, 6, 7, 8]
>>> # Note that the "+" is required to add lists together
>>> list1 list2
SyntaxError: invalid syntax
>>> # Lists can be assigned
>>> list3 = list1
>>> list3
[1, 2, 3, 4]
>>> # values can be added to the end of lists
>>> list3.append(10)
>>> list3
[1, 2, 3, 4, 10]
>>> list1
[1, 2, 3, 4, 10]
>>> # Note that a change to list3 changes list1
>>> list3.pop()
10
>>> list3
[1, 2, 3, 4]
>>> #list.pop(number) removes an element at that position/index
>>> list3.pop(2)
3
>>> # Lots more on lists to come
>>> 
>>> # A dictionary - a set of key, value pairs
>>> # Just like names and definitions
>>> # in the traditional dictionary

>>> # Dictionary defined with {...pairs of name, value...}
>>> d1 = {"name1" : "value_1", "name2" : 2, "name3" : "3"}
>>> d1
{'name1': 'value_1', 'name2': 2, 'name3': '3'}
>>> # Getting entry value:
>>> d1["name1"]
'value_1'
>>> # Replacing entry:
>>> d1["name1"] = "new_value_1"
>>> d1
{'name1': 'new_value_1', 'name2': 2, 'name3': '3', 'name4': 4}
