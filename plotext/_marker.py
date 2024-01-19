space = ' '
nl = '\n'

class tick_class:
   horizontal = '─'
   vertical =  '│'
   
   cross = '┼'
   right = '├'
   left  = '┤'
   upper = '┴'
   lower = '┬'
   
   upper_left = '┘'
   upper_right = '└'
   lower_left = '┐'
   lower_right = '┌'

   
class tick_rounded_class(tick_class):
   upper_left = '╯'
   upper_right = '╰'
   lower_left = '╮'
   lower_right = '╭'

   
class tick_doubled_class:
   horizontal = '═'
   vertical =  '║'
   
   cross = '╬'
   right = '╠'
   left  = '╣'
   upper = '╩'
   lower = '╦'

   upper_left = '╝'
   upper_right = '╚'
   lower_left = '╗'
   lower_right = '╔'

class tick_dotted_class(tick_class):
   horizontal = '┈'
   vertical =  '┊'
   
tick = tick_class()
tick_rounded = tick_rounded_class()
tick_doubled = tick_doubled_class()
tick_dotted = tick_dotted_class()


marker_codes = {'sd': '█', 'dot': '•', 'dollar': '$', 'euro': '€', 'bitcoin': '฿', 'at': '@', 'heart': '♥', 'smile': '☺', 'gclef': '𝄞', 'note': '𝅘𝅥', 'shamrock': '☘', 'atom': '⚛', 'snowflake': '❄', 'star': '❋', 'flower': '❁', 'lightning': '🌩', 'queen': '♕', 'king': '♔', 'cross': '♰', 'yinyang': '☯', 'om': 'ॐ', 'osiris': '𓂀', 'zero': '🯰', 'one': '🯱', 'two': '🯲', 'three': '🯳', 'four': '🯴', 'five': '🯵', 'six': '🯶', 'seven': '🯷', 'eight': '🯸', 'nine': '🯹'}

#default_marker = "hd" if platform == 'unix' else 'dot'
