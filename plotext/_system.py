import sys

platform = 'windows' if sys.platform in {'win32', 'cygwin'} else 'unix' 

def write(string, flush = True):
	sys.stdout.write(string)
	sys.stdout.flush() if flush else None