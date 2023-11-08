# where_are_we.py
# Find currently executing python
# usually IDLE
#
import os
import sys
from pathlib import Path
import subprocess

our_python = sys.executable
print(f"Our python: {our_python}")
python_path = Path(our_python)
scripts = python_path.parent.joinpath("scripts")
print(f"scripts dir: {scripts}")
if 'HOME' in os.environ:
    home = os.environ['HOME']
else:
    home = r"C:\Users\raysm"
print(f"HOME:{home}")
idle_cfg_dir= Path(home).joinpath(".idlerc")
print(f"IDLE cfg dir: {idle_cfg_dir}")
for root, dirs, files in os.walk(idle_cfg_dir):
    for name in files:
        fname = os.path.join(root, name)
        print(fname)
        with open(fname) as f:
            read_data = f.read()
            print(read_data)
