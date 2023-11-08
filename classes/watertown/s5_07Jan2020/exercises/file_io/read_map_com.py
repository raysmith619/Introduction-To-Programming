# read_map_com.py   12Nov2020  crs, from read_map.py
"""
Read text map file into array of lines
One might also consider map_data[][] as an array x,y chars
Supporting "//" C++ "to end of line" comments
because "#" already is found in map files
Blank lines as well as lines effectively blank
because of commenting are not stored.

"""
file_name = "map_file_com.txt"
map_data = []
com_str = "//"                      # Comment marker
# with == cleanup at end
with open(file_name) as finp:
    print("Input file")
    for line in finp:
        print(line, end="")         # Input
        if com_str in line:
            ind = line.index("//")
            if ind >= 0:
                line = line[:ind]   # Remove comment to end
        
        line = line.lstrip()        # Remove leading ws
        line = line.rstrip()        # Remove all trailing ws
        if len(line) == 0:
            continue                # Blank line
        map_data.append(line)
print("Data - with | making white space visible")
for data_line in map_data:
    print(f"|{data_line}|")         # | chars make visible
