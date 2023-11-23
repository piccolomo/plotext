from plotext._markers import tick
import sys

space = ' '
nl = '\n'

def write(string):
    sys.stdout.write(string)

def get_frame(width, height):
    Width = range(width); Height = range(height)
    matrix = [[tick.h] * width if row in [0, height - 1] else [tick.v if col in [0, width - 1] else space for col in Width] for row in Height]
    if width * height != 0:
        matrix[0][0] = tick.lower_left
        matrix[0][-1] = tick.lower_right
        matrix[-1][0] = tick.upper_left
        matrix[-1][-1] = tick.upper_right
    return '\n'.join([''.join(row) for row in matrix])   
