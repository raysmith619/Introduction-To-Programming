# install_module.py
# Install python module for currently executing python
# usually IDLE
#
import sys
from pathlib import Path

our_python = sys.executable
print(f"Our python: {our_python}")
python_path = Path(our_python)
scripts = python_path.parent.joinpath("scripts")
print(f"scripts dir: {scripts}")
pip_path = scripts.joinpath("pip.exe")
if not pip_path.exists():
    raise Error(f"file {pip_exe} is not a file")


