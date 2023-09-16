from plotext._marker import border, line

class matrix_class():
    def __init__(self, width = None, height = None):
        self.create_matrices(width, height)

    def create_matrices(self, width = None, height = None):
        self.set_size(width, height)
        marker = [[space for col in self.Width] for row in self.Height]
        self.marker = marker
            
    def set_size(self, width = None, height = None):
        self.width = int(width) if width is not None else 0
        self.height = int(height) if height is not None else 0
        self.size = [self.width, self.height]
        self.Width = range(self.width) 
        self.Height = range(self.height)
            
    def vertical_stack(self, matrix):
        new = matrix_class()
        new.marker = vertical_stack(self.marker, matrix.marker)
        new.update_size()
        return new
        
    def horizontal_stack(self, matrix):
        new = matrix_class()
        new.marker = horizontal_stack(self.marker, matrix.marker)
        new.update_size()
        return new
        
    def update_size(self):
        self.set_size(*matrix_size(self.marker))

    def get_string(self):
        strings = [''.join(row) for row in self.marker]
        self.string = '\n'.join(strings)
        return self.string

    def print(self):
        print(self.get_string())

    def set_marker(self, col, row, marker):
        self.marker[row][col] = marker

    def insert_element(self, col, row, marker):
        self.set_marker(col, row, marker)

    def insert_row(self, row, markers):
        cols = len(markers); Cols = range(cols)
        [self.insert_element(col, row, markers[col]) for col in Cols]

    def insert_col(self, col, markers):
        rows = len(markers); Rows = range(rows)
        [self.insert_element(col, row, markers[row]) for row in Rows]
    
space = ' '

def vertical_stack(matrix, extra): # vertical stack of two matrices
    return matrix + extra

def horizontal_stack(matrix, extra): # horizontal stack of two matrices
    lm, le = (len(matrix), len(extra))
    return matrix if le == 0 else extra if lm == 0 else [matrix[i] + extra[i] for i in range(lm)]

def join_matrices(matrices):
    cols, rows = matrix_size(matrices); Rows = range(rows); Cols = range(cols)
    matrix = matrix_class()
    for row in Rows:
        matrix_row = matrix_class()
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

