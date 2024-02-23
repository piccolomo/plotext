from plotext._system import platform
from plotext._hd_marker import hd_marker_codes
#from plotext._colorize import colorize
from copy import copy


space = ' '
nl = '\n'
   
default_marker = "hd" if platform == 'unix' else 'dot'

marker_codes = {'sd': '█', 'dot': '•', 'dollar': '$', 'euro': '€', 'bitcoin': '฿', 'at': '@', 'heart': '♥', 'smile': '☺', 'gclef': '𝄞', 'note': '𝅘𝅥', 'shamrock': '☘', 'atom': '⚛', 'snowflake': '❄', 'star': '❋', 'flower': '❁', 'lightning': '🌩', 'queen': '♕', 'king': '♔', 'cross': '♰', 'yinyang': '☯', 'om': 'ॐ', 'osiris': '𓂀', 'zero': '🯰', 'one': '🯱', 'two': '🯲', 'three': '🯳', 'four': '🯴', 'five': '🯵', 'six': '🯶', 'seven': '🯷', 'eight': '🯸', 'nine': '🯹'}


def harmonize_markers(markers):
   hd_markers = sorted([m for m in markers if m.get_string(1) in hd_marker_codes], key = lambda marker: marker.resolution(True), reverse = True)
   hd_marker = hd_markers[0].get_string(True) if len(hd_markers) > 0 else None
   markers = [m._reset_string(hd_marker) for m in markers] if hd_marker is not None else markers
   return markers


#def marker_class():
