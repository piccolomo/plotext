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

      








