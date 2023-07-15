# wx_notes_graphics.py 24Jun2023  crs, from notes_graphics.py
#
# notes_graphics.py 19Oct2022  crs, from notes_e.py
#                   13Oct2022  crs, from notes_3d
#                   26-Jul-2018
"""
wxPython version
Demonstration of a simple text data base with
a simple tkinter graphics interface.
This program was initially developed with a series
of programs in the files:
    https://github.com/raysmith619
        /Introduction-To-Programming/
        /exercises/notes/notes_1,...g programs.
The program operation
provides the listing of lines in the data file
containing the designated pattern.  The pattern is
a regular expression.
"""
import re
import wx
import os

from wx_notes_data_win import NotesDataWin

# Default values
def_file_name = "test.notes"
def_pattern = "student"

finp = None     # Currently open if not None
ndw = None      # Set to NotesDataWin instance

def file_open_proc(file_name):
    """ open/reopen file
    :file_name: file name
    :returns: file pointer if successful, None if not
    """
    global finp     # We may close it
    if finp is not None:
        finp.close()
    print(f"file_open_proc({file_name})")
    try:
        finp = open(file_name)
    
    except IOError :
        msg = f"Can't open file {os.path.abspath(file_name)}"
        ndw.error_message(msg)
        finp = None
    return finp

def pattern_search_proc(file_name, pattern):
    """ search for pattern within file
    :file_name: file in which to search
    :pattern: pattern(regular expression) for which to search
                file line
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

app = wx.App()

ndw = NotesDataWin(file_name=def_file_name,
             pattern=def_pattern,
             file_open_proc=file_open_proc,
             pattern_search_proc=pattern_search_proc)

app.MainLoop()
