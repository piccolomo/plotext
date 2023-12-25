space = ' '
nl = '\n'

class tick_class:
   def __init__(self):
      self.h = self.horizontal = '─'
      self.v = self.vertical =  '│'
      
      self.c = self.cross = '┼'
      self.r = self.right = '├'
      self.l = self.left  = '┤'
      self.upper = '┴'
      self.lower = '┬'
      self.ul = self.upper_left = '┘'
      self.ur = self.upper_right = '└'
      self.ll = self.lower_left = '┐'
      self.lr = self.lower_right = '┌' 
      
tick = tick_class()

marker_codes = {'sd': '█', 'dot': '•', 'dollar': '$', 'euro': '€', 'bitcoin': '฿', 'at': '@', 'heart': '♥', 'smile': '☺', 'gclef': '𝄞', 'note': '𝅘𝅥', 'shamrock': '☘', 'atom': '⚛', 'snowflake': '❄', 'star': '❋', 'flower': '❁', 'lightning': '🌩', 'queen': '♕', 'king': '♔', 'cross': '♰', 'yinyang': '☯', 'om': 'ॐ', 'osiris': '𓂀', 'zero': '🯰', 'one': '🯱', 'two': '🯲', 'three': '🯳', 'four': '🯴', 'five': '🯵', 'six': '🯶', 'seven': '🯷', 'eight': '🯸', 'nine': '🯹'}

#default_marker = "hd" if platform == 'unix' else 'dot'
