# install_module.py
# Install python module for currently executing python
# usually IDLE
#
import sys
from pathlib import Path
import subprocess

our_python = sys.executable
print(f"Our python: {our_python}")
python_path = Path(our_python)
scripts = python_path.parent.joinpath("scripts")
print(f"scripts dir: {scripts}")
pip_path = scripts.joinpath("pip.exe")
if not pip_path.exists():
    raise Error(f"file {pip_path} is not a file")

inp = input("Enter module to install: ")
if inp != "":
    pgm = str(pip_path)
    pgm_list = [pgm, "install", inp]
    print(f"Running: {pgm_list}")
    pgm_run = subprocess.Popen(pgm_list,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                )
    pgm_out, pgm_error = pgm_run.communicate()
    pgm_run.wait()
    print(f"pgm_error: {pgm_error}")
    print(f"output:\n{pgm_out}")

