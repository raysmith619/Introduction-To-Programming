Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1+2
3
>>> 2*4
8
>>> 3/2
1.5
>>> 4-5
-1
>>> 5%2
1
>>> 10**3
1000
>>> 99999+1
100000
>>> 9999999999999999999999999999+1
10000000000000000000000000000
>>> 10000000000000000000000000000=1
SyntaxError: cannot assign to literal
>>> 10000000000000000000000000000-1
9999999999999999999999999999
>>> 2*3
6
>>> help("while")
The "while" statement
*********************

The "while" statement is used for repeated execution as long as an
expression is true:

   while_stmt ::= "while" assignment_expression ":" suite
                  ["else" ":" suite]

This repeatedly tests the expression and, if it is true, executes the
first suite; if the expression is false (which may be the first time
it is tested) the suite of the "else" clause, if present, is executed
and the loop terminates.

A "break" statement executed in the first suite terminates the loop
without executing the "else" clause’s suite.  A "continue" statement
executed in the first suite skips the rest of the suite and goes back
to testing the expression.

Related help topics: break, continue, if, TRUTHVALUE

>>> help("while")

>>> 
>>> 
>>> 10000000000000000000000000000-1
9999999999999999999999999999
>>> 1+2;3+4;5*6
3
7
30
>>> 10**9
1000000000
>>> 10**9/12
83333333.33333333
>>> 10**9/50
20000000.0
>>> 10**9/2000
500000.0
>>> a=1
>>> b=2
>>> c=3
>>> b*c
6
>>> yr_salary=10**9
>>> yr_salary
1000000000
>>> yr_salary/50
20000000.0
>>> mth_salary=yr_salary/50
>>> mth_salary
20000000.0
>>> "my_name"
'my_name'
>>> "Massachussets"
'Massachussets'
>>> print("yr:", yr_salary, " mth:",mth_salary)
yr: 1000000000  mth: 20000000.0
>>> print("yr:", yr_salary, " mth:",mth_salary.format())
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print("yr:", yr_salary, " mth:",mth_salary.format())
AttributeError: 'float' object has no attribute 'format'
>>> print("yr:", yr_salary, " mth:",mth_salary.format())
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print("yr:", yr_salary, " mth:",mth_salary.format())
AttributeError: 'float' object has no attribute 'format'
>>> print("yr:", yr_salary, " mth:",str(mth_salary).format())
yr: 1000000000  mth: 20000000.0
>>> print("yr:", yr_salary, " mth:",str(mth_salary).format())
yr: 1000000000  mth: 20000000.0
>>> print("yr:", yr_salary, " mth:",str(mth_salary).format())
KeyboardInterrupt
>>> help(format)
Help on built-in function format in module builtins:

format(value, format_spec='', /)
    Return value.__format__(format_spec)
    
    format_spec defaults to the empty string.
    See the Format Specification Mini-Language section of help('FORMATTING') for
    details.

>>> format(yr_salary,format_spec=",")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    format(yr_salary,format_spec=",")
TypeError: format() takes no keyword arguments
>>> format(yr_salary,",")
'1,000,000,000'
>>> help(format)
Help on built-in function format in module builtins:

format(value, format_spec='', /)
    Return value.__format__(format_spec)
    
    format_spec defaults to the empty string.
    See the Format Specification Mini-Language section of help('FORMATTING') for
    details.

>>> help('formatting')
No Python documentation found for 'formatting'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help('formatting')
No Python documentation found for 'formatting'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help('formatting'.upper())
Format String Syntax
********************

The "str.format()" method and the "Formatter" class share the same
syntax for format strings (although in the case of "Formatter",
subclasses can define their own format string syntax).  The syntax is
related to that of formatted string literals, but it is less
sophisticated and, in particular, does not support arbitrary
expressions.

Format strings contain “replacement fields” surrounded by curly braces
"{}". Anything that is not contained in braces is considered literal
text, which is copied unchanged to the output.  If you need to include
a brace character in the literal text, it can be escaped by doubling:
"{{" and "}}".

The grammar for a replacement field is as follows:

      replacement_field ::= "{" [field_name] ["!" conversion] [":" format_spec] "}"
      field_name        ::= arg_name ("." attribute_name | "[" element_index "]")*
      arg_name          ::= [identifier | digit+]
      attribute_name    ::= identifier
      element_index     ::= digit+ | index_string
      index_string      ::= <any source character except "]"> +
      conversion        ::= "r" | "s" | "a"
      format_spec       ::= <described in the next section>

In less formal terms, the replacement field can start with a
*field_name* that specifies the object whose value is to be formatted
and inserted into the output instead of the replacement field. The
*field_name* is optionally followed by a  *conversion* field, which is
preceded by an exclamation point "'!'", and a *format_spec*, which is
preceded by a colon "':'".  These specify a non-default format for the
replacement value.

See also the Format Specification Mini-Language section.

The *field_name* itself begins with an *arg_name* that is either a
number or a keyword.  If it’s a number, it refers to a positional
argument, and if it’s a keyword, it refers to a named keyword
argument.  If the numerical arg_names in a format string are 0, 1, 2,
… in sequence, they can all be omitted (not just some) and the numbers
0, 1, 2, … will be automatically inserted in that order. Because
*arg_name* is not quote-delimited, it is not possible to specify
arbitrary dictionary keys (e.g., the strings "'10'" or "':-]'") within
a format string. The *arg_name* can be followed by any number of index
or attribute expressions. An expression of the form "'.name'" selects
the named attribute using "getattr()", while an expression of the form
"'[index]'" does an index lookup using "__getitem__()".

Changed in version 3.1: The positional argument specifiers can be
omitted for "str.format()", so "'{} {}'.format(a, b)" is equivalent to
"'{0} {1}'.format(a, b)".

Changed in version 3.4: The positional argument specifiers can be
omitted for "Formatter".

Some simple format string examples:

   "First, thou shalt count to {0}"  # References first positional argument
   "Bring me a {}"                   # Implicitly references the first positional argument
   "From {} to {}"                   # Same as "From {0} to {1}"
   "My quest is {name}"              # References keyword argument 'name'
   "Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
   "Units destroyed: {players[0]}"   # First element of keyword argument 'players'.

The *conversion* field causes a type coercion before formatting.
Normally, the job of formatting a value is done by the "__format__()"
method of the value itself.  However, in some cases it is desirable to
force a type to be formatted as a string, overriding its own
definition of formatting.  By converting the value to a string before
calling "__format__()", the normal formatting logic is bypassed.

Three conversion flags are currently supported: "'!s'" which calls
"str()" on the value, "'!r'" which calls "repr()" and "'!a'" which
calls "ascii()".

Some examples:

   "Harold's a clever {0!s}"        # Calls str() on the argument first
   "Bring out the holy {name!r}"    # Calls repr() on the argument first
   "More {!a}"                      # Calls ascii() on the argument first

The *format_spec* field contains a specification of how the value
should be presented, including such details as field width, alignment,
padding, decimal precision and so on.  Each value type can define its
own “formatting mini-language” or interpretation of the *format_spec*.

Most built-in types support a common formatting mini-language, which
is described in the next section.

A *format_spec* field can also include nested replacement fields
within it. These nested replacement fields may contain a field name,
conversion flag and format specification, but deeper nesting is not
allowed.  The replacement fields within the format_spec are
substituted before the *format_spec* string is interpreted. This
allows the formatting of a value to be dynamically specified.

See the Format examples section for some examples.


Format Specification Mini-Language
==================================

“Format specifications” are used within replacement fields contained
within a format string to define how individual values are presented
(see Format String Syntax and Formatted string literals). They can
also be passed directly to the built-in "format()" function.  Each
formattable type may define how the format specification is to be
interpreted.

Most built-in types implement the following options for format
specifications, although some of the formatting options are only
supported by the numeric types.

A general convention is that an empty format specification produces
the same result as if you had called "str()" on the value. A non-empty
format specification typically modifies the result.

The general form of a *standard format specifier* is:

   format_spec     ::= [[fill]align][sign][#][0][width][grouping_option][.precision][type]
   fill            ::= <any character>
   align           ::= "<" | ">" | "=" | "^"
   sign            ::= "+" | "-" | " "
   width           ::= digit+
   grouping_option ::= "_" | ","
   precision       ::= digit+
   type            ::= "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

If a valid *align* value is specified, it can be preceded by a *fill*
character that can be any character and defaults to a space if
omitted. It is not possible to use a literal curly brace (“"{"” or
“"}"”) as the *fill* character in a formatted string literal or when
using the "str.format()" method.  However, it is possible to insert a
curly brace with a nested replacement field.  This limitation doesn’t
affect the "format()" function.

The meaning of the various alignment options is as follows:

   +-----------+------------------------------------------------------------+
   | Option    | Meaning                                                    |
   |===========|============================================================|
   | "'<'"     | Forces the field to be left-aligned within the available   |
   |           | space (this is the default for most objects).              |
   +-----------+------------------------------------------------------------+
   | "'>'"     | Forces the field to be right-aligned within the available  |
   |           | space (this is the default for numbers).                   |
   +-----------+------------------------------------------------------------+
   | "'='"     | Forces the padding to be placed after the sign (if any)    |
   |           | but before the digits.  This is used for printing fields   |
   |           | in the form ‘+000000120’. This alignment option is only    |
   |           | valid for numeric types.  It becomes the default when ‘0’  |
   |           | immediately precedes the field width.                      |
   +-----------+------------------------------------------------------------+
   | "'^'"     | Forces the field to be centered within the available       |
   |           | space.                                                     |
   +-----------+------------------------------------------------------------+

Note that unless a minimum field width is defined, the field width
will always be the same size as the data to fill it, so that the
alignment option has no meaning in this case.

The *sign* option is only valid for number types, and can be one of
the following:

   +-----------+------------------------------------------------------------+
   | Option    | Meaning                                                    |
   |===========|============================================================|
   | "'+'"     | indicates that a sign should be used for both positive as  |
   |           | well as negative numbers.                                  |
   +-----------+------------------------------------------------------------+
   | "'-'"     | indicates that a sign should be used only for negative     |
   |           | numbers (this is the default behavior).                    |
   +-----------+------------------------------------------------------------+
   | space     | indicates that a leading space should be used on positive  |
   |           | numbers, and a minus sign on negative numbers.             |
   +-----------+------------------------------------------------------------+

The "'#'" option causes the “alternate form” to be used for the
conversion.  The alternate form is defined differently for different
types.  This option is only valid for integer, float and complex
types. For integers, when binary, octal, or hexadecimal output is
used, this option adds the prefix respective "'0b'", "'0o'", or "'0x'"
to the output value. For float and complex the alternate form causes
the result of the conversion to always contain a decimal-point
character, even if no digits follow it. Normally, a decimal-point
character appears in the result of these conversions only if a digit
follows it. In addition, for "'g'" and "'G'" conversions, trailing
zeros are not removed from the result.

The "','" option signals the use of a comma for a thousands separator.
For a locale aware separator, use the "'n'" integer presentation type
instead.

Changed in version 3.1: Added the "','" option (see also **PEP 378**).

The "'_'" option signals the use of an underscore for a thousands
separator for floating point presentation types and for integer
presentation type "'d'".  For integer presentation types "'b'", "'o'",
"'x'", and "'X'", underscores will be inserted every 4 digits.  For
other presentation types, specifying this option is an error.

Changed in version 3.6: Added the "'_'" option (see also **PEP 515**).

*width* is a decimal integer defining the minimum total field width,
including any prefixes, separators, and other formatting characters.
If not specified, then the field width will be determined by the
content.

When no explicit alignment is given, preceding the *width* field by a
zero ("'0'") character enables sign-aware zero-padding for numeric
types.  This is equivalent to a *fill* character of "'0'" with an
*alignment* type of "'='".

The *precision* is a decimal number indicating how many digits should
be displayed after the decimal point for a floating point value
formatted with "'f'" and "'F'", or before and after the decimal point
for a floating point value formatted with "'g'" or "'G'".  For non-
number types the field indicates the maximum field size - in other
words, how many characters will be used from the field content. The
*precision* is not allowed for integer values.

Finally, the *type* determines how the data should be presented.

The available string presentation types are:

   +-----------+------------------------------------------------------------+
   | Type      | Meaning                                                    |
   |===========|============================================================|
   | "'s'"     | String format. This is the default type for strings and    |
   |           | may be omitted.                                            |
   +-----------+------------------------------------------------------------+
   | None      | The same as "'s'".                                         |
   +-----------+------------------------------------------------------------+

The available integer presentation types are:

   +-----------+------------------------------------------------------------+
   | Type      | Meaning                                                    |
   |===========|============================================================|
   | "'b'"     | Binary format. Outputs the number in base 2.               |
   +-----------+------------------------------------------------------------+
   | "'c'"     | Character. Converts the integer to the corresponding       |
   |           | unicode character before printing.                         |
   +-----------+------------------------------------------------------------+
   | "'d'"     | Decimal Integer. Outputs the number in base 10.            |
   +-----------+------------------------------------------------------------+
   | "'o'"     | Octal format. Outputs the number in base 8.                |
   +-----------+------------------------------------------------------------+
   | "'x'"     | Hex format. Outputs the number in base 16, using lower-    |
   |           | case letters for the digits above 9.                       |
   +-----------+------------------------------------------------------------+
   | "'X'"     | Hex format. Outputs the number in base 16, using upper-    |
   |           | case letters for the digits above 9.                       |
   +-----------+------------------------------------------------------------+
   | "'n'"     | Number. This is the same as "'d'", except that it uses the |
   |           | current locale setting to insert the appropriate number    |
   |           | separator characters.                                      |
   +-----------+------------------------------------------------------------+
   | None      | The same as "'d'".                                         |
   +-----------+------------------------------------------------------------+

In addition to the above presentation types, integers can be formatted
with the floating point presentation types listed below (except "'n'"
and "None"). When doing so, "float()" is used to convert the integer
to a floating point number before formatting.

The available presentation types for "float" and "Decimal" values are:

   +-----------+------------------------------------------------------------+
   | Type      | Meaning                                                    |
   |===========|============================================================|
   | "'e'"     | Scientific notation. For a given precision "p", formats    |
   |           | the number in scientific notation with the letter ‘e’      |
   |           | separating the coefficient from the exponent. The          |
   |           | coefficient has one digit before and "p" digits after the  |
   |           | decimal point, for a total of "p + 1" significant digits.  |
   |           | With no precision given, uses a precision of "6" digits    |
   |           | after the decimal point for "float", and shows all         |
   |           | coefficient digits for "Decimal". If no digits follow the  |
   |           | decimal point, the decimal point is also removed unless    |
   |           | the "#" option is used.                                    |
   +-----------+------------------------------------------------------------+
   | "'E'"     | Scientific notation. Same as "'e'" except it uses an upper |
   |           | case ‘E’ as the separator character.                       |
   +-----------+------------------------------------------------------------+
   | "'f'"     | Fixed-point notation. For a given precision "p", formats   |
   |           | the number as a decimal number with exactly "p" digits     |
   |           | following the decimal point. With no precision given, uses |
   |           | a precision of "6" digits after the decimal point for      |
   |           | "float", and uses a precision large enough to show all     |
   |           | coefficient digits for "Decimal". If no digits follow the  |
   |           | decimal point, the decimal point is also removed unless    |
   |           | the "#" option is used.                                    |
   +-----------+------------------------------------------------------------+
   | "'F'"     | Fixed-point notation. Same as "'f'", but converts "nan" to |
   |           | "NAN" and "inf" to "INF".                                  |
   +-----------+------------------------------------------------------------+
   | "'g'"     | General format.  For a given precision "p >= 1", this      |
   |           | rounds the number to "p" significant digits and then       |
   |           | formats the result in either fixed-point format or in      |
   |           | scientific notation, depending on its magnitude. A         |
   |           | precision of "0" is treated as equivalent to a precision   |
   |           | of "1".  The precise rules are as follows: suppose that    |
   |           | the result formatted with presentation type "'e'" and      |
   |           | precision "p-1" would have exponent "exp".  Then, if "m <= |
   |           | exp < p", where "m" is -4 for floats and -6 for            |
   |           | "Decimals", the number is formatted with presentation type |
   |           | "'f'" and precision "p-1-exp".  Otherwise, the number is   |
   |           | formatted with presentation type "'e'" and precision       |
   |           | "p-1". In both cases insignificant trailing zeros are      |
   |           | removed from the significand, and the decimal point is     |
   |           | also removed if there are no remaining digits following    |
   |           | it, unless the "'#'" option is used.  With no precision    |
   |           | given, uses a precision of "6" significant digits for      |
   |           | "float". For "Decimal", the coefficient of the result is   |
   |           | formed from the coefficient digits of the value;           |
   |           | scientific notation is used for values smaller than "1e-6" |
   |           | in absolute value and values where the place value of the  |
   |           | least significant digit is larger than 1, and fixed-point  |
   |           | notation is used otherwise.  Positive and negative         |
   |           | infinity, positive and negative zero, and nans, are        |
   |           | formatted as "inf", "-inf", "0", "-0" and "nan"            |
   |           | respectively, regardless of the precision.                 |
   +-----------+------------------------------------------------------------+
   | "'G'"     | General format. Same as "'g'" except switches to "'E'" if  |
   |           | the number gets too large. The representations of infinity |
   |           | and NaN are uppercased, too.                               |
   +-----------+------------------------------------------------------------+
   | "'n'"     | Number. This is the same as "'g'", except that it uses the |
   |           | current locale setting to insert the appropriate number    |
   |           | separator characters.                                      |
   +-----------+------------------------------------------------------------+
   | "'%'"     | Percentage. Multiplies the number by 100 and displays in   |
   |           | fixed ("'f'") format, followed by a percent sign.          |
   +-----------+------------------------------------------------------------+
   | None      | For "float" this is the same as "'g'", except that when    |
   |           | fixed-point notation is used to format the result, it      |
   |           | always includes at least one digit past the decimal point. |
   |           | The precision used is as large as needed to represent the  |
   |           | given value faithfully.  For "Decimal", this is the same   |
   |           | as either "'g'" or "'G'" depending on the value of         |
   |           | "context.capitals" for the current decimal context.  The   |
   |           | overall effect is to match the output of "str()" as        |
   |           | altered by the other format modifiers.                     |
   +-----------+------------------------------------------------------------+


Format examples
===============

This section contains examples of the "str.format()" syntax and
comparison with the old "%"-formatting.

In most of the cases the syntax is similar to the old "%"-formatting,
with the addition of the "{}" and with ":" used instead of "%". For
example, "'%03.2f'" can be translated to "'{:03.2f}'".

The new format syntax also supports new and different options, shown
in the following examples.

Accessing arguments by position:

   >>> '{0}, {1}, {2}'.format('a', 'b', 'c')
   'a, b, c'
   >>> '{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only
   'a, b, c'
   >>> '{2}, {1}, {0}'.format('a', 'b', 'c')
   'c, b, a'
   >>> '{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
   'c, b, a'
   >>> '{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
   'abracadabra'

Accessing arguments by name:

   >>> 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
   'Coordinates: 37.24N, -115.81W'
   >>> coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
   >>> 'Coordinates: {latitude}, {longitude}'.format(**coord)
   'Coordinates: 37.24N, -115.81W'

Accessing arguments’ attributes:

   >>> c = 3-5j
   >>> ('The complex number {0} is formed from the real part {0.real} '
   ...  'and the imaginary part {0.imag}.').format(c)
   'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'
   >>> class Point:
   ...     def __init__(self, x, y):
   ...         self.x, self.y = x, y
   ...     def __str__(self):
   ...         return 'Point({self.x}, {self.y})'.format(self=self)
   ...
   >>> str(Point(4, 2))
   'Point(4, 2)'

Accessing arguments’ items:

   >>> coord = (3, 5)
   >>> 'X: {0[0]};  Y: {0[1]}'.format(coord)
   'X: 3;  Y: 5'

Replacing "%s" and "%r":

   >>> "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
   "repr() shows quotes: 'test1'; str() doesn't: test2"

Aligning the text and specifying a width:

   >>> '{:<30}'.format('left aligned')
   'left aligned                  '
   >>> '{:>30}'.format('right aligned')
   '                 right aligned'
   >>> '{:^30}'.format('centered')
   '           centered           '
   >>> '{:*^30}'.format('centered')  # use '*' as a fill char
   '***********centered***********'

Replacing "%+f", "%-f", and "% f" and specifying a sign:

   >>> '{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
   '+3.140000; -3.140000'
   >>> '{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
   ' 3.140000; -3.140000'
   >>> '{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
   '3.140000; -3.140000'

Replacing "%x" and "%o" and converting the value to different bases:

   >>> # format also supports binary numbers
   >>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
   'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
   >>> # with 0x, 0o, or 0b as prefix:
   >>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
   'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

Using the comma as a thousands separator:

   >>> '{:,}'.format(1234567890)
   '1,234,567,890'

Expressing a percentage:

   >>> points = 19
   >>> total = 22
   >>> 'Correct answers: {:.2%}'.format(points/total)
   'Correct answers: 86.36%'

Using type-specific formatting:

   >>> import datetime
   >>> d = datetime.datetime(2010, 7, 4, 12, 15, 58)
   >>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
   '2010-07-04 12:15:58'

Nesting arguments and more complex examples:

   >>> for align, text in zip('<^>', ['left', 'center', 'right']):
   ...     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
   ...
   'left<<<<<<<<<<<<'
   '^^^^^center^^^^^'
   '>>>>>>>>>>>right'
   >>>
   >>> octets = [192, 168, 0, 1]
   >>> '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
   'C0A80001'
   >>> int(_, 16)
   3232235521
   >>>
   >>> width = 5
   >>> for num in range(5,12): 
   ...     for base in 'dXob':
   ...         print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
   ...     print()
   ...
       5     5     5   101
       6     6     6   110
       7     7     7   111
       8     8    10  1000
       9     9    11  1001
      10     A    12  1010
      11     B    13  1011

Related help topics: OPERATORS

>>> 
>>> Using type-specific formatting:
KeyboardInterrupt
>>> help(
	
KeyboardInterrupt
>>> help("keyword")
Help on module keyword:

NAME
    keyword - Keywords (from "Grammar/python.gram")

MODULE REFERENCE
    https://docs.python.org/3.9/library/keyword
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This file is automatically generated; please don't muck it up!
    
    To update the symbols in this file, 'cd' to the top directory of
    the python source tree and run:
    
        PYTHONPATH=Tools/peg_generator python3 -m pegen.keywordgen         Grammar/Grammar         Grammar/Tokens         Lib/keyword.py
    
    Alternatively, you can run 'make regen-keyword'.

FUNCTIONS
    iskeyword = __contains__(...) method of builtins.frozenset instance
        x.__contains__(y) <==> y in x.
    
    issoftkeyword = __contains__(...) method of builtins.frozenset instance
        x.__contains__(y) <==> y in x.

DATA
    __all__ = ['iskeyword', 'issoftkeyword', 'kwlist', 'softkwlist']
    kwlist = ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'ass...
    softkwlist = []

FILE
    c:\users\raysm\appdata\local\programs\python\python39\lib\keyword.py


>>> help("comment")_
SyntaxError: invalid syntax
>>> help("comment")
No Python documentation found for 'comment'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("comment")
No Python documentation found for 'comment'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("comments")
No Python documentation found for 'comments'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("#")
No Python documentation found for '#'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("=")
No Python documentation found for '='.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("arithmetic")
No Python documentation found for 'arithmetic'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("computation")
No Python documentation found for 'computation'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("==")
Operator precedence
*******************

The following table summarizes the operator precedence in Python, from
lowest precedence (least binding) to highest precedence (most
binding).  Operators in the same box have the same precedence.  Unless
the syntax is explicitly given, operators are binary.  Operators in
the same box group left to right (except for exponentiation, which
groups from right to left).

Note that comparisons, membership tests, and identity tests, all have
the same precedence and have a left-to-right chaining feature as
described in the Comparisons section.

+-------------------------------------------------+---------------------------------------+
| Operator                                        | Description                           |
|=================================================|=======================================|
| ":="                                            | Assignment expression                 |
+-------------------------------------------------+---------------------------------------+
| "lambda"                                        | Lambda expression                     |
+-------------------------------------------------+---------------------------------------+
| "if" – "else"                                   | Conditional expression                |
+-------------------------------------------------+---------------------------------------+
| "or"                                            | Boolean OR                            |
+-------------------------------------------------+---------------------------------------+
| "and"                                           | Boolean AND                           |
+-------------------------------------------------+---------------------------------------+
| "not" "x"                                       | Boolean NOT                           |
+-------------------------------------------------+---------------------------------------+
| "in", "not in", "is", "is not", "<", "<=", ">", | Comparisons, including membership     |
| ">=", "!=", "=="                                | tests and identity tests              |
+-------------------------------------------------+---------------------------------------+
| "|"                                             | Bitwise OR                            |
+-------------------------------------------------+---------------------------------------+
| "^"                                             | Bitwise XOR                           |
+-------------------------------------------------+---------------------------------------+
| "&"                                             | Bitwise AND                           |
+-------------------------------------------------+---------------------------------------+
| "<<", ">>"                                      | Shifts                                |
+-------------------------------------------------+---------------------------------------+
| "+", "-"                                        | Addition and subtraction              |
+-------------------------------------------------+---------------------------------------+
| "*", "@", "/", "//", "%"                        | Multiplication, matrix                |
|                                                 | multiplication, division, floor       |
|                                                 | division, remainder [5]               |
+-------------------------------------------------+---------------------------------------+
| "+x", "-x", "~x"                                | Positive, negative, bitwise NOT       |
+-------------------------------------------------+---------------------------------------+
| "**"                                            | Exponentiation [6]                    |
+-------------------------------------------------+---------------------------------------+
| "await" "x"                                     | Await expression                      |
+-------------------------------------------------+---------------------------------------+
| "x[index]", "x[index:index]",                   | Subscription, slicing, call,          |
| "x(arguments...)", "x.attribute"                | attribute reference                   |
+-------------------------------------------------+---------------------------------------+
| "(expressions...)",  "[expressions...]", "{key: | Binding or parenthesized expression,  |
| value...}", "{expressions...}"                  | list display, dictionary display, set |
|                                                 | display                               |
+-------------------------------------------------+---------------------------------------+

-[ Footnotes ]-

[1] While "abs(x%y) < abs(y)" is true mathematically, for floats it
    may not be true numerically due to roundoff.  For example, and
    assuming a platform on which a Python float is an IEEE 754 double-
    precision number, in order that "-1e-100 % 1e100" have the same
    sign as "1e100", the computed result is "-1e-100 + 1e100", which
    is numerically exactly equal to "1e100".  The function
    "math.fmod()" returns a result whose sign matches the sign of the
    first argument instead, and so returns "-1e-100" in this case.
    Which approach is more appropriate depends on the application.

[2] If x is very close to an exact integer multiple of y, it’s
    possible for "x//y" to be one larger than "(x-x%y)//y" due to
    rounding.  In such cases, Python returns the latter result, in
    order to preserve that "divmod(x,y)[0] * y + x % y" be very close
    to "x".

[3] The Unicode standard distinguishes between *code points* (e.g.
    U+0041) and *abstract characters* (e.g. “LATIN CAPITAL LETTER A”).
    While most abstract characters in Unicode are only represented
    using one code point, there is a number of abstract characters
    that can in addition be represented using a sequence of more than
    one code point.  For example, the abstract character “LATIN
    CAPITAL LETTER C WITH CEDILLA” can be represented as a single
    *precomposed character* at code position U+00C7, or as a sequence
    of a *base character* at code position U+0043 (LATIN CAPITAL
    LETTER C), followed by a *combining character* at code position
    U+0327 (COMBINING CEDILLA).

    The comparison operators on strings compare at the level of
    Unicode code points. This may be counter-intuitive to humans.  For
    example, ""\u00C7" == "\u0043\u0327"" is "False", even though both
    strings represent the same abstract character “LATIN CAPITAL
    LETTER C WITH CEDILLA”.

    To compare strings at the level of abstract characters (that is,
    in a way intuitive to humans), use "unicodedata.normalize()".

[4] Due to automatic garbage-collection, free lists, and the dynamic
    nature of descriptors, you may notice seemingly unusual behaviour
    in certain uses of the "is" operator, like those involving
    comparisons between instance methods, or constants.  Check their
    documentation for more info.

[5] The "%" operator is also used for string formatting; the same
    precedence applies.

[6] The power operator "**" binds less tightly than an arithmetic or
    bitwise unary operator on its right, that is, "2**-1" is "0.5".

Related help topics: lambda, or, and, not, in, is, BOOLEAN, COMPARISON,
BITWISE, SHIFTING, BINARY, FORMATTING, POWER, UNARY, ATTRIBUTES,
SUBSCRIPTS, SLICINGS, CALLS, TUPLES, LISTS, DICTIONARIES, COMPARISON

>>> help("comparisons")
No Python documentation found for 'comparisons'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("comparison")
No Python documentation found for 'comparison'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("comparison")
No Python documentation found for 'comparison'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("comparison")
No Python documentation found for 'comparison'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("compute")
No Python documentation found for 'compute'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("+")
Operator precedence
*******************

The following table summarizes the operator precedence in Python, from
lowest precedence (least binding) to highest precedence (most
binding).  Operators in the same box have the same precedence.  Unless
the syntax is explicitly given, operators are binary.  Operators in
the same box group left to right (except for exponentiation, which
groups from right to left).

Note that comparisons, membership tests, and identity tests, all have
the same precedence and have a left-to-right chaining feature as
described in the Comparisons section.

+-------------------------------------------------+---------------------------------------+
| Operator                                        | Description                           |
|=================================================|=======================================|
| ":="                                            | Assignment expression                 |
+-------------------------------------------------+---------------------------------------+
| "lambda"                                        | Lambda expression                     |
+-------------------------------------------------+---------------------------------------+
| "if" – "else"                                   | Conditional expression                |
+-------------------------------------------------+---------------------------------------+
| "or"                                            | Boolean OR                            |
+-------------------------------------------------+---------------------------------------+
| "and"                                           | Boolean AND                           |
+-------------------------------------------------+---------------------------------------+
| "not" "x"                                       | Boolean NOT                           |
+-------------------------------------------------+---------------------------------------+
| "in", "not in", "is", "is not", "<", "<=", ">", | Comparisons, including membership     |
| ">=", "!=", "=="                                | tests and identity tests              |
+-------------------------------------------------+---------------------------------------+
| "|"                                             | Bitwise OR                            |
+-------------------------------------------------+---------------------------------------+
| "^"                                             | Bitwise XOR                           |
+-------------------------------------------------+---------------------------------------+
| "&"                                             | Bitwise AND                           |
+-------------------------------------------------+---------------------------------------+
| "<<", ">>"                                      | Shifts                                |
+-------------------------------------------------+---------------------------------------+
| "+", "-"                                        | Addition and subtraction              |
+-------------------------------------------------+---------------------------------------+
| "*", "@", "/", "//", "%"                        | Multiplication, matrix                |
|                                                 | multiplication, division, floor       |
|                                                 | division, remainder [5]               |
+-------------------------------------------------+---------------------------------------+
| "+x", "-x", "~x"                                | Positive, negative, bitwise NOT       |
+-------------------------------------------------+---------------------------------------+
| "**"                                            | Exponentiation [6]                    |
+-------------------------------------------------+---------------------------------------+
| "await" "x"                                     | Await expression                      |
+-------------------------------------------------+---------------------------------------+
| "x[index]", "x[index:index]",                   | Subscription, slicing, call,          |
| "x(arguments...)", "x.attribute"                | attribute reference                   |
+-------------------------------------------------+---------------------------------------+
| "(expressions...)",  "[expressions...]", "{key: | Binding or parenthesized expression,  |
| value...}", "{expressions...}"                  | list display, dictionary display, set |
|                                                 | display                               |
+-------------------------------------------------+---------------------------------------+

-[ Footnotes ]-

[1] While "abs(x%y) < abs(y)" is true mathematically, for floats it
    may not be true numerically due to roundoff.  For example, and
    assuming a platform on which a Python float is an IEEE 754 double-
    precision number, in order that "-1e-100 % 1e100" have the same
    sign as "1e100", the computed result is "-1e-100 + 1e100", which
    is numerically exactly equal to "1e100".  The function
    "math.fmod()" returns a result whose sign matches the sign of the
    first argument instead, and so returns "-1e-100" in this case.
    Which approach is more appropriate depends on the application.

[2] If x is very close to an exact integer multiple of y, it’s
    possible for "x//y" to be one larger than "(x-x%y)//y" due to
    rounding.  In such cases, Python returns the latter result, in
    order to preserve that "divmod(x,y)[0] * y + x % y" be very close
    to "x".

[3] The Unicode standard distinguishes between *code points* (e.g.
    U+0041) and *abstract characters* (e.g. “LATIN CAPITAL LETTER A”).
    While most abstract characters in Unicode are only represented
    using one code point, there is a number of abstract characters
    that can in addition be represented using a sequence of more than
    one code point.  For example, the abstract character “LATIN
    CAPITAL LETTER C WITH CEDILLA” can be represented as a single
    *precomposed character* at code position U+00C7, or as a sequence
    of a *base character* at code position U+0043 (LATIN CAPITAL
    LETTER C), followed by a *combining character* at code position
    U+0327 (COMBINING CEDILLA).

    The comparison operators on strings compare at the level of
    Unicode code points. This may be counter-intuitive to humans.  For
    example, ""\u00C7" == "\u0043\u0327"" is "False", even though both
    strings represent the same abstract character “LATIN CAPITAL
    LETTER C WITH CEDILLA”.

    To compare strings at the level of abstract characters (that is,
    in a way intuitive to humans), use "unicodedata.normalize()".

[4] Due to automatic garbage-collection, free lists, and the dynamic
    nature of descriptors, you may notice seemingly unusual behaviour
    in certain uses of the "is" operator, like those involving
    comparisons between instance methods, or constants.  Check their
    documentation for more info.

[5] The "%" operator is also used for string formatting; the same
    precedence applies.

[6] The power operator "**" binds less tightly than an arithmetic or
    bitwise unary operator on its right, that is, "2**-1" is "0.5".

Related help topics: lambda, or, and, not, in, is, BOOLEAN, COMPARISON,
BITWISE, SHIFTING, BINARY, FORMATTING, POWER, UNARY, ATTRIBUTES,
SUBSCRIPTS, SLICINGS, CALLS, TUPLES, LISTS, DICTIONARIES

>>> help("COMPARISON")
Comparisons
***********

Unlike C, all comparison operations in Python have the same priority,
which is lower than that of any arithmetic, shifting or bitwise
operation.  Also unlike C, expressions like "a < b < c" have the
interpretation that is conventional in mathematics:

   comparison    ::= or_expr (comp_operator or_expr)*
   comp_operator ::= "<" | ">" | "==" | ">=" | "<=" | "!="
                     | "is" ["not"] | ["not"] "in"

Comparisons yield boolean values: "True" or "False".

Comparisons can be chained arbitrarily, e.g., "x < y <= z" is
equivalent to "x < y and y <= z", except that "y" is evaluated only
once (but in both cases "z" is not evaluated at all when "x < y" is
found to be false).

Formally, if *a*, *b*, *c*, …, *y*, *z* are expressions and *op1*,
*op2*, …, *opN* are comparison operators, then "a op1 b op2 c ... y
opN z" is equivalent to "a op1 b and b op2 c and ... y opN z", except
that each expression is evaluated at most once.

Note that "a op1 b op2 c" doesn’t imply any kind of comparison between
*a* and *c*, so that, e.g., "x < y > z" is perfectly legal (though
perhaps not pretty).


Value comparisons
=================

The operators "<", ">", "==", ">=", "<=", and "!=" compare the values
of two objects.  The objects do not need to have the same type.

Chapter Objects, values and types states that objects have a value (in
addition to type and identity).  The value of an object is a rather
abstract notion in Python: For example, there is no canonical access
method for an object’s value.  Also, there is no requirement that the
value of an object should be constructed in a particular way, e.g.
comprised of all its data attributes. Comparison operators implement a
particular notion of what the value of an object is.  One can think of
them as defining the value of an object indirectly, by means of their
comparison implementation.

Because all types are (direct or indirect) subtypes of "object", they
inherit the default comparison behavior from "object".  Types can
customize their comparison behavior by implementing *rich comparison
methods* like "__lt__()", described in Basic customization.

The default behavior for equality comparison ("==" and "!=") is based
on the identity of the objects.  Hence, equality comparison of
instances with the same identity results in equality, and equality
comparison of instances with different identities results in
inequality.  A motivation for this default behavior is the desire that
all objects should be reflexive (i.e. "x is y" implies "x == y").

A default order comparison ("<", ">", "<=", and ">=") is not provided;
an attempt raises "TypeError".  A motivation for this default behavior
is the lack of a similar invariant as for equality.

The behavior of the default equality comparison, that instances with
different identities are always unequal, may be in contrast to what
types will need that have a sensible definition of object value and
value-based equality.  Such types will need to customize their
comparison behavior, and in fact, a number of built-in types have done
that.

The following list describes the comparison behavior of the most
important built-in types.

* Numbers of built-in numeric types (Numeric Types — int, float,
  complex) and of the standard library types "fractions.Fraction" and
  "decimal.Decimal" can be compared within and across their types,
  with the restriction that complex numbers do not support order
  comparison.  Within the limits of the types involved, they compare
  mathematically (algorithmically) correct without loss of precision.

  The not-a-number values "float('NaN')" and "decimal.Decimal('NaN')"
  are special.  Any ordered comparison of a number to a not-a-number
  value is false. A counter-intuitive implication is that not-a-number
  values are not equal to themselves.  For example, if "x =
  float('NaN')", "3 < x", "x < 3" and "x == x" are all false, while "x
  != x" is true.  This behavior is compliant with IEEE 754.

* "None" and "NotImplemented" are singletons.  **PEP 8** advises that
  comparisons for singletons should always be done with "is" or "is
  not", never the equality operators.

* Binary sequences (instances of "bytes" or "bytearray") can be
  compared within and across their types.  They compare
  lexicographically using the numeric values of their elements.

* Strings (instances of "str") compare lexicographically using the
  numerical Unicode code points (the result of the built-in function
  "ord()") of their characters. [3]

  Strings and binary sequences cannot be directly compared.

* Sequences (instances of "tuple", "list", or "range") can be compared
  only within each of their types, with the restriction that ranges do
  not support order comparison.  Equality comparison across these
  types results in inequality, and ordering comparison across these
  types raises "TypeError".

  Sequences compare lexicographically using comparison of
  corresponding elements.  The built-in containers typically assume
  identical objects are equal to themselves.  That lets them bypass
  equality tests for identical objects to improve performance and to
  maintain their internal invariants.

  Lexicographical comparison between built-in collections works as
  follows:

  * For two collections to compare equal, they must be of the same
    type, have the same length, and each pair of corresponding
    elements must compare equal (for example, "[1,2] == (1,2)" is
    false because the type is not the same).

  * Collections that support order comparison are ordered the same as
    their first unequal elements (for example, "[1,2,x] <= [1,2,y]"
    has the same value as "x <= y").  If a corresponding element does
    not exist, the shorter collection is ordered first (for example,
    "[1,2] < [1,2,3]" is true).

* Mappings (instances of "dict") compare equal if and only if they
  have equal *(key, value)* pairs. Equality comparison of the keys and
  values enforces reflexivity.

  Order comparisons ("<", ">", "<=", and ">=") raise "TypeError".

* Sets (instances of "set" or "frozenset") can be compared within and
  across their types.

  They define order comparison operators to mean subset and superset
  tests.  Those relations do not define total orderings (for example,
  the two sets "{1,2}" and "{2,3}" are not equal, nor subsets of one
  another, nor supersets of one another).  Accordingly, sets are not
  appropriate arguments for functions which depend on total ordering
  (for example, "min()", "max()", and "sorted()" produce undefined
  results given a list of sets as inputs).

  Comparison of sets enforces reflexivity of its elements.

* Most other built-in types have no comparison methods implemented, so
  they inherit the default comparison behavior.

User-defined classes that customize their comparison behavior should
follow some consistency rules, if possible:

* Equality comparison should be reflexive. In other words, identical
  objects should compare equal:

     "x is y" implies "x == y"

* Comparison should be symmetric. In other words, the following
  expressions should have the same result:

     "x == y" and "y == x"

     "x != y" and "y != x"

     "x < y" and "y > x"

     "x <= y" and "y >= x"

* Comparison should be transitive. The following (non-exhaustive)
  examples illustrate that:

     "x > y and y > z" implies "x > z"

     "x < y and y <= z" implies "x < z"

* Inverse comparison should result in the boolean negation. In other
  words, the following expressions should have the same result:

     "x == y" and "not x != y"

     "x < y" and "not x >= y" (for total ordering)

     "x > y" and "not x <= y" (for total ordering)

  The last two expressions apply to totally ordered collections (e.g.
  to sequences, but not to sets or mappings). See also the
  "total_ordering()" decorator.

* The "hash()" result should be consistent with equality. Objects that
  are equal should either have the same hash value, or be marked as
  unhashable.

Python does not enforce these consistency rules. In fact, the
not-a-number values are an example for not following these rules.


Membership test operations
==========================

The operators "in" and "not in" test for membership.  "x in s"
evaluates to "True" if *x* is a member of *s*, and "False" otherwise.
"x not in s" returns the negation of "x in s".  All built-in sequences
and set types support this as well as dictionary, for which "in" tests
whether the dictionary has a given key. For container types such as
list, tuple, set, frozenset, dict, or collections.deque, the
expression "x in y" is equivalent to "any(x is e or x == e for e in
y)".

For the string and bytes types, "x in y" is "True" if and only if *x*
is a substring of *y*.  An equivalent test is "y.find(x) != -1".
Empty strings are always considered to be a substring of any other
string, so """ in "abc"" will return "True".

For user-defined classes which define the "__contains__()" method, "x
in y" returns "True" if "y.__contains__(x)" returns a true value, and
"False" otherwise.

For user-defined classes which do not define "__contains__()" but do
define "__iter__()", "x in y" is "True" if some value "z", for which
the expression "x is z or x == z" is true, is produced while iterating
over "y". If an exception is raised during the iteration, it is as if
"in" raised that exception.

Lastly, the old-style iteration protocol is tried: if a class defines
"__getitem__()", "x in y" is "True" if and only if there is a non-
negative integer index *i* such that "x is y[i] or x == y[i]", and no
lower integer index raises the "IndexError" exception.  (If any other
exception is raised, it is as if "in" raised that exception).

The operator "not in" is defined to have the inverse truth value of
"in".


Identity comparisons
====================

The operators "is" and "is not" test for an object’s identity: "x is
y" is true if and only if *x* and *y* are the same object.  An
Object’s identity is determined using the "id()" function.  "x is not
y" yields the inverse truth value. [4]

Related help topics: EXPRESSIONS, BASICMETHODS

>>> help("expressions")
No Python documentation found for 'expressions'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("expressions".upper())
Operator precedence
*******************

The following table summarizes the operator precedence in Python, from
lowest precedence (least binding) to highest precedence (most
binding).  Operators in the same box have the same precedence.  Unless
the syntax is explicitly given, operators are binary.  Operators in
the same box group left to right (except for exponentiation, which
groups from right to left).

Note that comparisons, membership tests, and identity tests, all have
the same precedence and have a left-to-right chaining feature as
described in the Comparisons section.

+-------------------------------------------------+---------------------------------------+
| Operator                                        | Description                           |
|=================================================|=======================================|
| ":="                                            | Assignment expression                 |
+-------------------------------------------------+---------------------------------------+
| "lambda"                                        | Lambda expression                     |
+-------------------------------------------------+---------------------------------------+
| "if" – "else"                                   | Conditional expression                |
+-------------------------------------------------+---------------------------------------+
| "or"                                            | Boolean OR                            |
+-------------------------------------------------+---------------------------------------+
| "and"                                           | Boolean AND                           |
+-------------------------------------------------+---------------------------------------+
| "not" "x"                                       | Boolean NOT                           |
+-------------------------------------------------+---------------------------------------+
| "in", "not in", "is", "is not", "<", "<=", ">", | Comparisons, including membership     |
| ">=", "!=", "=="                                | tests and identity tests              |
+-------------------------------------------------+---------------------------------------+
| "|"                                             | Bitwise OR                            |
+-------------------------------------------------+---------------------------------------+
| "^"                                             | Bitwise XOR                           |
+-------------------------------------------------+---------------------------------------+
| "&"                                             | Bitwise AND                           |
+-------------------------------------------------+---------------------------------------+
| "<<", ">>"                                      | Shifts                                |
+-------------------------------------------------+---------------------------------------+
| "+", "-"                                        | Addition and subtraction              |
+-------------------------------------------------+---------------------------------------+
| "*", "@", "/", "//", "%"                        | Multiplication, matrix                |
|                                                 | multiplication, division, floor       |
|                                                 | division, remainder [5]               |
+-------------------------------------------------+---------------------------------------+
| "+x", "-x", "~x"                                | Positive, negative, bitwise NOT       |
+-------------------------------------------------+---------------------------------------+
| "**"                                            | Exponentiation [6]                    |
+-------------------------------------------------+---------------------------------------+
| "await" "x"                                     | Await expression                      |
+-------------------------------------------------+---------------------------------------+
| "x[index]", "x[index:index]",                   | Subscription, slicing, call,          |
| "x(arguments...)", "x.attribute"                | attribute reference                   |
+-------------------------------------------------+---------------------------------------+
| "(expressions...)",  "[expressions...]", "{key: | Binding or parenthesized expression,  |
| value...}", "{expressions...}"                  | list display, dictionary display, set |
|                                                 | display                               |
+-------------------------------------------------+---------------------------------------+

-[ Footnotes ]-

[1] While "abs(x%y) < abs(y)" is true mathematically, for floats it
    may not be true numerically due to roundoff.  For example, and
    assuming a platform on which a Python float is an IEEE 754 double-
    precision number, in order that "-1e-100 % 1e100" have the same
    sign as "1e100", the computed result is "-1e-100 + 1e100", which
    is numerically exactly equal to "1e100".  The function
    "math.fmod()" returns a result whose sign matches the sign of the
    first argument instead, and so returns "-1e-100" in this case.
    Which approach is more appropriate depends on the application.

[2] If x is very close to an exact integer multiple of y, it’s
    possible for "x//y" to be one larger than "(x-x%y)//y" due to
    rounding.  In such cases, Python returns the latter result, in
    order to preserve that "divmod(x,y)[0] * y + x % y" be very close
    to "x".

[3] The Unicode standard distinguishes between *code points* (e.g.
    U+0041) and *abstract characters* (e.g. “LATIN CAPITAL LETTER A”).
    While most abstract characters in Unicode are only represented
    using one code point, there is a number of abstract characters
    that can in addition be represented using a sequence of more than
    one code point.  For example, the abstract character “LATIN
    CAPITAL LETTER C WITH CEDILLA” can be represented as a single
    *precomposed character* at code position U+00C7, or as a sequence
    of a *base character* at code position U+0043 (LATIN CAPITAL
    LETTER C), followed by a *combining character* at code position
    U+0327 (COMBINING CEDILLA).

    The comparison operators on strings compare at the level of
    Unicode code points. This may be counter-intuitive to humans.  For
    example, ""\u00C7" == "\u0043\u0327"" is "False", even though both
    strings represent the same abstract character “LATIN CAPITAL
    LETTER C WITH CEDILLA”.

    To compare strings at the level of abstract characters (that is,
    in a way intuitive to humans), use "unicodedata.normalize()".

[4] Due to automatic garbage-collection, free lists, and the dynamic
    nature of descriptors, you may notice seemingly unusual behaviour
    in certain uses of the "is" operator, like those involving
    comparisons between instance methods, or constants.  Check their
    documentation for more info.

[5] The "%" operator is also used for string formatting; the same
    precedence applies.

[6] The power operator "**" binds less tightly than an arithmetic or
    bitwise unary operator on its right, that is, "2**-1" is "0.5".

Related help topics: lambda, or, and, not, in, is, BOOLEAN, COMPARISON,
BITWISE, SHIFTING, BINARY, FORMATTING, POWER, UNARY, ATTRIBUTES,
SUBSCRIPTS, SLICINGS, CALLS, TUPLES, LISTS, DICTIONARIES

>>> 1=2
SyntaxError: cannot assign to literal
>>> d
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> 