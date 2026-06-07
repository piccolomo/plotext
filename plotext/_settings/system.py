# System settings: platform detection, package metadata, and optional dependency imports.
# Optional deps are imported lazily inside the try/except — installed via the matching pip extras (e.g. `pip install plotext[image]`); when absent the names stay None.

import sys

# Determine the platform type
platform = "windows" if sys.platform in {"win32", "cygwin"} else "unix"

# Package metadata
__name__ = "plotext"
__version__ = version = "6.0.0b0"

# Optional dependency: Pillow (image rendering) — `pip install plotext[image]`.
try:
    from PIL import Image, ImageOps, ImageSequence
except ImportError:
    Image = ImageOps = ImageSequence = None

# Optional dependencies: ffpyplayer (video + audio playback) and yt-dlp (YouTube URL resolution) — `pip install plotext[video]`.
try:
    from ffpyplayer.player import MediaPlayer
except ImportError:
    MediaPlayer = None

try:
    import yt_dlp
except ImportError:
    yt_dlp = None
