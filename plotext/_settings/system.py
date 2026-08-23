# System settings: the system in use, the package version, and the optional packages, imported here and left as None when missing, since each is installed on its own, as in pip install plotext[image].

import sys

# Determine the platform type
platform = "windows" if sys.platform in {"win32", "cygwin"} else "unix"

# Package metadata
__name__ = "plotext"
__version__ = version = "6.0.0"

# Optional dependency: Pillow (image rendering), `pip install plotext[image]`.
try:
    from PIL import Image, ImageOps, ImageSequence
except ImportError:
    Image = ImageOps = ImageSequence = None

# Optional dependencies: ffpyplayer (video + audio playback) and yt-dlp (YouTube URL resolution), `pip install plotext[video]`.
try:
    from ffpyplayer.player import MediaPlayer
except ImportError:
    MediaPlayer = None

try:
    import yt_dlp
except ImportError:
    yt_dlp = None
