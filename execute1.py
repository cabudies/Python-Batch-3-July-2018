'''
my_cx_freeze.py
To run code from cmd
python my_cx_freeze.py build
'''
import os   
import sys
from cx_Freeze import setup, Executable

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

exe = Executable(
    # location to your file.
    script = r"C:\Users\JATINDER\PycharmProjects\TkinterExample\Tkinter Example.py",
    base = "Win32GUI",
)

options = {
    'build_exe': {
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ],
    },
}

# filename = "gamble.py"
setup(
    name = 'gamble1',
    version = '0.1',
    description = 'Gui test',
    options = options,
    executables = [exe]
)
