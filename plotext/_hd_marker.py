from plotext._link import *
from plotext._dict import *
from math import floor


class hd_marker:
   def __init__(self, dictionary):
      self.dictionary = dictionary

   def set_shape(self, cols, rows):
      self.cols = cols
      self.rows = rows
      self.shape = (cols, rows)

   def get_tuple(self, x, y):
      return get_tuple(x, y, self.cols, self.rows)

   def get_marker(self, tuple):
      return self.dictionary[tuple]

   
def get_tuple(x, y, cols, rows):
   x = floor(round((x - int(x)) * cols, 8))
   y = floor(round((y - int(y)) * rows, 8))
   m = [[0 for col in range(cols)] for row in range(rows)]
   m[y][x] = 1
   return tuple([el for sub in m for el in sub ])

def sum_tuples(*tuples):
   return tuple(int(any(el)) for el in zip(*tuples))


hd = hd_marker(hd_codes)
hd.set_shape(2, 2)

fhd = hd_marker(fhd_codes)
fhd.set_shape(2, 3)

braille = hd_marker(braille_codes)
braille.set_shape(2, 4)

hd_marker_codes = {'hd': hd, 'fhd': fhd, 'braille': braille}


      








