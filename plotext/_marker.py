from plotext._link import *
from plotext._dict import *
import ctypes as c
from math import floor


class tick_class():
   def __init__(self, style = None):
      self.styles = ['default', 'rounded', 'doubled', 'dotted']
      style = self.correct_style(style)

      self.horizontal = '┈' if style == 'dotted' else '═' if style == 'doubled' else '─' 
      self.vertical = '┊' if style == 'dotted' else '║' if style == 'doubled' else '│'
      
      self.cross = '╬' if style == 'doubled' else '┼'
      self.right = '╠' if style == 'doubled' else '├'
      self.left  = '╣' if style == 'doubled' else '┤'
      self.upper = '╩' if style == 'doubled' else '┴'
      self.lower = '╦' if style == 'doubled' else '┬'
      
      self.upper_left = '╯' if style == 'rounded' else '╝' if style == 'doubled' else '┘'
      self.upper_right = '╰' if style == 'rounded' else '╚' if style == 'doubled' else '└'
      self.lower_left = '╮' if style == 'rounded' else '╗' if style == 'doubled' else '┐'
      self.lower_right = '╭' if style == 'rounded' else '╔' if style == 'doubled' else '┌'

   def correct_style(self, style = None):
      return 'default' if style is None or style not in self.styles else style

def sum_tuples(*tuples):
   return tuple(int(any(el)) for el in zip(*tuples))

def get_tuple(x, y, cols, rows):
   x = floor(round((x - int(x)) * cols, 8))
   y = floor(round((y - int(y)) * rows, 8))
   m = [[0 for col in range(cols)] for row in range(rows)]
   m[y][x] = 1
   return tuple([el for sub in m for el in sub ])


class hd_marker:
   def __init__(self, dictionary):
      self.dictionary = dictionary

   def set_shape(self, cols, rows):
      self.cols = cols
      self.rows = rows
      self.shape = [cols, rows]

   def get_tuple(self, x, y):
      return get_tuple(x, y, self.cols, self.rows)

   def get_marker(self, tuple):
      return self.dictionary[tuple]

space = ' '
nl = '\n'
   
default_marker = "hd" if platform == 'unix' else 'dot'

hd = hd_marker(hd_codes)
hd.set_shape(2, 2)

fhd = hd_marker(fhd_codes)
fhd.set_shape(2, 3)

braille = hd_marker(braille_codes)
braille.set_shape(2, 4)

hd_marker_codes = {'hd': hd, 'fhd': fhd, 'braille': braille}

def correct_markers(marker = None):
   marker = default_marker if marker is None else marker
   marker = [marker] if isinstance(marker, str) else marker
   marker = list(map(correct_marker, marker))
   hd_markers = sorted([el for el in marker if el in hd_marker_codes], key = lambda el: marker_resolution(el)[1])
   marker = [hd_markers[0]] if len(hd_markers) > 0 else [el[0] for el in marker]
   return marker

def correct_marker(marker):
   return marker if marker in hd_marker_codes else marker_codes[marker] if marker in marker_codes.keys() else marker[0]

def marker_resolution(marker):
   return (1, 1) if marker not in hd_marker_codes else hd_marker_codes[marker].shape









