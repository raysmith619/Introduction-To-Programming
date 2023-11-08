# install_module.py
""" Installing a python module
"""
from subprocess import call
import sys
import os

exe_dir = os.path.dirname(sys.executable)
print("Python exe dir", exe_dir)
pip_exe = os.path.join(exe_dir, "Scripts", "pip.exe")
print("Pip exe:", pip_exe)
module = "xlrd"         # Default module
md=input('Name module:[%s]' % module)
if md != "":
    module = md
print("Installing", module)
try:
    call([pip_exe, 'install', module])
except Exception:
    print('Error')
print("End of install")

