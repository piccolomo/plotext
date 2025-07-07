import sys

# Determine platform type: 'windows' or 'unix'
platform = 'windows' if sys.platform in {'win32', 'cygwin'} else 'unix'


