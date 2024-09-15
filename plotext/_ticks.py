class ticks:
      horizontal = '─' 
      vertical = '│'
      
      cross = '┼'
      right = '├'
      left  = '┤'
      upper = '┴'
      lower = '┬'
      
      upper_right = '┘'
      upper_left = '└'
      lower_right = '┐'
      lower_left = '┌'


class ticks_dotted(ticks):
      horizontal = '┈' 
      vertical = '┊'


class ticks_double:
      horizontal = '═' 
      vertical = '║'
      
      cross = '╬'
      right = '╠'
      left  = '╣'
      upper = '╩'
      lower = '╦'

      upper_right = '╝'
      upper_left = '╚'
      lower_right = '╗'
      lower_left = '╔'


class ticks_rounded(ticks):
      upper_left = '╯'
      upper_right = '╰'
      lower_left = '╮'
      lower_right = '╭'


styles = ["default", "dotted", "double", "rounded"]
ticks_manager = [ticks, ticks_dotted, ticks_double, ticks_rounded]

def correct_style(style = None):
   style = style if style in styles else "default" 
   return style

def get_ticks(style = None):
   style = correct_style(style)
   return ticks_manager[styles.index(style)]