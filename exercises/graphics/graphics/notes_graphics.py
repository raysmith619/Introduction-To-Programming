# notes_graphics.py 19Oct2022  crs, from notes_e.py
#                   13Oct2022  crs, from notes_3d
#                   26-Jul-2018
"""
Demonstration of a simple text data base with
a simple tkinter graphics interface.
This program was initially developed with a series
of programs in the files:
    https://github.com/raysmith619
        /Introduction-To-Programming/
        /exercises/notes/notes_1,...notes_e programs.
The program operation
provides the listing of lines in the data file
containing the designated pattern.  The pattern is
a regular expression.
"""
import re
import tkinter as tk

from notes_data_win import NotesDataWin

# Default values
def_file_name = "test.notes"    # Notes data file
def_pattern = "student"         # Search pattern

finp = None     # Currently open if not None
ndw = None      # Set to NotesDataWin instance

def file_open_proc(file_name):
    """ open/reopen file
        Display Message if not able to open file
    :file_name: file name
    :returns: file pointer if successful, None if not
    """
    global finp     # Modified, close if already open
    if finp is not None:
        finp.close()
    print(f"file_open_proc({file_name})")
    try:
        finp = open(file_name)
    
    except IOError :
        msg = f"Can't open file {file_name}"
        ndw.info_message("IOError", msg)
        finp = None
    return finp

def pattern_search_proc(file_name, pattern):
    """ search for pattern within file
        Display Message if not able to open file

    :file_name: file in which to search
    :pattern: pattern(regular expression)
                for which to search in
                file lines
    """
    ndw.list_print(f"\nFile:{file_name} Pattern: {pattern}")
    finp = file_open_proc(file_name)
    print(f"pattern_search_proc({file_name},{pattern})")
    if finp is None:
       print(f"search file {file_name} can't be opened")
       return

    for line in finp:
        line = line.rstrip()        # All trailing white space
        match = re.search(pattern, line)
        if (match):
            ndw.list_print(line)

    
ndw = NotesDataWin(file_name=def_file_name,
             pattern=def_pattern,
             file_open_proc=file_open_proc,
             pattern_search_proc=pattern_search_proc)

tk.mainloop()       # Process window events
