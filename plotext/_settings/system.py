# System settings: platform detection and package metadata

import sys

# Determine the platform type
platform = "windows" if sys.platform in {"win32", "cygwin"} else "unix"

# Package metadata
__name__ = "plotext"
__version__ = version = "6.0.0beta"
