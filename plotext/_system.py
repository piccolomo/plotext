import sys

platform = 'windows' if sys.platform in {'win32', 'cygwin'} else 'unix' 

write = lambda string: sys.stdout.write(string)
