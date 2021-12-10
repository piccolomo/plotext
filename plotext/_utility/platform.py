from plotext._utility.file import script_folder, parent_folder, join_paths
import sys
import os

def platform(): # the platform (eg: linux) you are using plotext with
    platform = sys.platform
    # According to the docs, this returns one of: 'aix', 'linux', 'win32', 'cygwin', 
    # 'darwin', or the modified result of `uname -s` on other Unix systems.
    if platform in {'win32', 'cygwin'}:
        # These are the only two possible outputs on Windows systems
        return 'windows'
    else:
        # Anything that is not Windows and that runs Python is a flavor of Unix
        return 'unix'

_platform = platform()

if _platform == "windows":
    # to enable ascii escape color sequences
    import subprocess 
    subprocess.call('', shell = True)

    # to enable higher definition markers in windows: it didn't work....
    #import ctypes
    #kernel32 = ctypes.windll.kernel32
    #kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7) 

    #import win32console 
    #win32console.SetConsoleCP(65001)
    #win32console.SetConsoleOutputCP(65001)

    #import sys, codecs
    #sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    #sys.stderr = codecs.getwriter('utf8')(sys.stderr)

    #import win_unicode_console

    
def version():
    init_file = join_paths(parent_folder(script_folder()), "__init__.py")
    with open(init_file, 'r') as fp:
        lines = fp.read()
    for line in lines.splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            version = line.split(delim)[1]
            print("plotext version:", version)
            return version
    else:
        print("Unable to find version string.")
