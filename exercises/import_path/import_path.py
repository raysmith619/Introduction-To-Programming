# import_path.py    11Sep2023  crs

import sys
print("path:","\n","\n\t".join(sys.path), "\n")
# Import target: C:\Users\raysm\vscode\resource_lib\src\
from select_trace import SlTrace   # Home rolled tracing/logging

SlTrace.lg("Hello World")
