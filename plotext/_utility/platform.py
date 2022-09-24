from plotext._utility import join_paths, script_folder, parent_folder
import sys, shutil

def is_ipython(): # true if running in ipython shenn
    try:
        __IPYTHON__
        return True
    except NameError:
        return False

def version(): # returns plotext version
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
       print("unable to find version string")
       
def platform(): # the platform (eg: linux) you are using plotext with
   platform = sys.platform
   if platform in {'win32', 'cygwin'}:
       return 'windows'
   else:
       return 'unix'

platform = platform()

# to enable ascii escape color sequences
if platform == "windows":
    import subprocess 
    subprocess.call('', shell = True)

def terminal_size(): # it returns the terminal size as [width, height]
    try:
        size = shutil.get_terminal_size()
        return list(size)
    except OSError:
        return [None, None]

def clear_terminal(lines = None): # it cleat the entire terminal, or the specified number of lines
    if lines is None:
        write('\033c')
    else:
        for r in range(lines):
            write("\033[A") # moves the curson up
            write("\033[2K") # clear the entire line

def write(string): # the print function used by plotext
    sys.stdout.write(string)


