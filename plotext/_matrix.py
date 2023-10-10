from plotext._marker import border, line, space
from plotext._string import only_spaces, correct_position
from plotext._default import get_integer_horizontal_alignment, get_integer_vertical_alignment

class matrix_class():
    def __init__(self, width = None, height = None):
        self.set_matrices(width, height)

        
    def set_size(self, width = None, height = None):
        self.width = int(width) if width is not None else 0
        self.height = int(height) if height is not None else 0
        self.size = [self.width, self.height]
        self.Width = range(self.width) 
        self.Height = range(self.height)
        
    def update_size(self):
        self.set_size(*matrix_size(self.marker))

    def set_matrices(self, width = None, height = None):
        self.set_size(width, height)
        marker = [[space for col in self.Width] for row in self.Height]
        self.marker = marker
        
    def vertical_stack(self, matrix):
        new = matrix_class()
        new.marker = self.marker + matrix.marker
        new.update_size()
        return new
        
    def horizontal_stack(self, matrix):
        new = matrix_class()
        new.marker = horizontal_stack(self.marker, matrix.marker)
        new.update_size()
        return new

    def get_marker(self, row, col):
        return self.marker[row][col]
        
    def set_marker(self, row, col, marker):
        self.marker[row][col] = marker

    def insert_element(self, row, col, marker):
        self.set_marker(row, col, marker)


    def insert_horizontal_string(self, row, col, string, alignment = 'left', overwrite = True):
        length = len(string)
        index = get_integer_horizontal_alignment(alignment)
        col = correct_position(col, index, length, self.width)
        Cols = range(length)
        overwrite = overwrite or self.check_horizontal_string(row, col, length)
        [self.insert_element(row, col + c, string[c]) for c in Cols] if overwrite else None

    def insert_vertical_string(self, row, col, string, alignment = 'top', overwrite = True):
        length = len(string)
        index = get_integer_horizontal_alignment(alignment)
        row = correct_position(row, index, length, self.height)
        Rows = range(length)
        overwrite = overwrite or self.check_vertical_string(row, col, length)
        [self.insert_element(row + r, col, string[r]) for r in Rows] if overwrite else None

    def correct_horizontal_position(self, string, position, alignment = 'left'):
        ls = len(string)
        
        

    def get_horizontal_string(self, row, col, length):
        cols = range(max(0, col), min(col + length, self.width))
        string = [self.get_marker(row, c) for c in cols]
        return ''.join(string)

    # def correct_coord(string, label, coord): # In the attempt to insert a label in string at given coordinate, the coordinate is adjusted so not to hit the borders of the string
    # l = len(label)
    # b, e = max(coord - l + 1, 0), min(coord + l, len(string) - 1)
    # data = [i for i in range(b, e) if string[i] is space]
    # b, e = min(data, default = coord - l + 1), max(data, default = coord + l)
    # b, e = e - l + 1, b + l
    # return (b + e - l) // 2
        
    def get_vertical_string(self, row, col, length):
        rows = range(max(0, row), min(row + length, self.height))
        string = [self.get_marker(r, col) for r in rows]
        return ''.join(string)

    def check_horizontal_string(self, row, col, length):
        string = self.get_horizontal_string(row, col - 1, length + 2)
        return only_spaces(string)
                
    def check_vertical_string(self, row, col, length):
        string = self.get_vertical_string(row - 1, col, length + 2)
        return only_spaces(string)

        
    def get_string(self):
        strings = [''.join(row) for row in self.marker]
        self.string = '\n'.join(strings)
        return self.string

    def print(self):
        print(self.get_string())

    def clear(self):
        self.__init__(self.width, self.height)

        

    
def horizontal_stack(matrix, extra):
    return [matrix[i] + extra[i] for i in range(len(matrix))]

def join_matrices(matrices):
    cols, rows = matrix_size(matrices); Rows = range(rows); Cols = range(cols)
    height = [matrices[row][0].height for row in Rows]
    matrix = matrix_class(cols, 0)
    for row in Rows:
        matrix_row = matrix_class(0, height[row])
        for col in Cols:
            matrix_row = matrix_row.horizontal_stack(matrices[row][col])
        matrix = matrix.vertical_stack(matrix_row)
    return matrix

matrix_size = lambda matrix: [0, 0] if len(matrix) == 0 else [len(matrix[0]), len(matrix)] # width, height

# def get_frame(width, height):
#     Width = range(width); Height = range(height)
#     matrix = [[line.h] * width if row in [0, height - 1] else [line.vertical if col in [0, width - 1] else space for col in Width] for row in Height]
#     if width * height != 0:
#         matrix[0][0] = border.upper_left
#         matrix[0][-1] = border.upper_right
#         matrix[-1][0] = border.lower_left
#         matrix[-1][-1] = border.lower_right
#     return matrix

