# read_map.py   12Nov2020  crs, from read_file.py
"""
Read text map file into array of lines
One might also consider map_data[][] as an array x,y chars
One might consider supporting comments in the data file.

:) Would it be pedantic to start talking about design
decisions such as the character choices for walls allowing
support the Python "#" as comment character :)

"""
file_name = "map_file.txt"
map_data = []
# with == cleanup at end
with open(file_name) as finp:
    print("Input file")
    for line in finp:
        print(line, end="")         # Input
        line = line.lstrip()        # Remove leading ws
        line = line.rstrip('\n')    # Remove EOL, iff one
                                    # Oh for the C chomp
        map_data.append(line)
print("Data")
for data_line in map_data:
    print(data_line)
