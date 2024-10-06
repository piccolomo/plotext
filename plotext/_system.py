import sys, shutil
from ._default import default_terminal_size

platform = 'windows' if sys.platform in {'win32', 'cygwin'} else 'unix' 

def write(string, flush = True):
	sys.stdout.write(string)
	sys.stdout.flush() if flush else None

def get_terminal_size():
	try:
		size = shutil.get_terminal_size()
		return size.columns, size.lines
	except:
		return default_terminal_size
	
def clear_terminal(lines = None): # it clear the entire terminal, or the specified number of lines
    if lines is None:
        write('\033c')
    else:
        for r in range(lines):
            write("\033[A") # moves the curson up
            write("\033[2K") # clear the entire line