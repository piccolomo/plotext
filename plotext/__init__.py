"""The plotext package allows you to plot data directly on terminal."""
import platform

if platform.system() == "Windows":
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        print("Cannot set color support, use show(color=False)")

from plotext import plot
name="plotext"
__version__ = "0.1.16"