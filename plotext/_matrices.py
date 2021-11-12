from plotext._utility.color import color_type, color_code, sum_colors, begin_escape, end_escape, no_color_name, to_rgb
from plotext._utility.marker import refine_marker, space_marker, sum_markers
from plotext._utility.data import pad_matrix, insert
from math import floor

class figure_matrices(): # storing the figure canvas in matrix form
    def __init__(self):
        self.marker = []
        self.color = []
        self.background = []
        self.update_size()

    def update_size(self):
        self.rows = len(self.marker)
        self.cols = 0 if self.marker == [] else len(self.marker[0])

    def to_canvas(self): # turns the matrices to the plot canvas in string form
        self.update_size()
        if self.rows == 0:
            self.canvas = ''
            return self.canvas
        
        m = [el.copy() for el in self.marker.copy()]
        c = [el.copy() for el in self.color]
        b = [el.copy() for el in self.background]
        
        both = lambda row, col: [c[row][col], b[row][col]]
        for row in range(self.rows):
            for col in range(self.cols):
                if col == 0 or both(row, col) != both(row, col - 1):
                    m[row][col] = begin_escape(c[row][col]) + begin_escape(b[row][col]) + m[row][col]
                if (col == self.cols - 1) or both(row, col) != both(row, col + 1):
                    m[row][col] = m[row][col] + end_escape(b[row][col]) + end_escape(c[row][col])
# This is a longer escape version of previous lines
                # m[r][c] = begin_escape(b[r][c]) + m[r][c] + end_escape(b[r][c])
                # m[r][c] = begin_escape(color[r][c]) + m[r][c] + end_escape(color[r][c])
        self.canvas = '\n'.join([''.join(el) for el in m]) 
        end = end_escape((1,1,1))
        self.canvas = self.canvas + end if end in self.canvas else self.canvas
        self.canvas += '\n'
        return self.canvas
        
    def to_html(self):
        self.update_size()
        code = lambda color: "rgb" + str(color).replace(" ", "")
        #html = "<body>\n<p style=\"font-family:courier; font-size:11pt;\">\n\n"
        html = "<body> \n <code style = style=\"font-family:courier; \"font-size : 10pt;\"> \n\n"
        for r in range(self.rows):
            for c in range(self.cols):
                marker = self.marker[r][c]
                marker = "&nbsp;" if marker == space_marker else marker
                color = self.color[r][c]
                background = self.background[r][c]
                color = to_rgb(color)
                background = to_rgb(background)
                html += "<span style = \"color:" + code(color) + "; background-color: " + code(background) + "\">" + marker + "</span>"
            html += " <br>\n\n"
        html += "<code> \n </body>"
        return html

class subplot_matrices(figure_matrices): # storing the subplot canvas in matrix form
    def create(self, cols, rows, m, c, b): # create matrices with given dimensions
        self.marker = [[m for col in range(cols)] for row in range(rows)]
        self.color = [[color_code(c, 1) for col in range(cols)] for row in range(rows)]
        self.background = [[color_code(b, 0) for col in range(cols)] for row in range(rows)]
        self.update_size()

    def update_same_elements(self, x, y, m, c):
        # set marker, color and background elements at coordinates x, y, if provided
        m = [m] * len(x)
        c = [color_code(c, 1)] * len(x)
        self.update(x, y, m, c)

    def update_different_elements(self, x, y, m, c):
        # set marker, color and background elements at coordinates x, y, if provided
        x = [x[i] for i in range(len(x)) if m[i] != space_marker]
        y = [y[i] for i in range(len(x)) if m[i] != space_marker]
        c = [color_code(c[i], 1) for i in range(len(x)) if m[i] != space_marker]
        m = [refine_marker(m[i], x[i], y[i]) for i in range(len(x)) if m[i] != space_marker]
        self.update(x, y, m, c)

    def insert(self, row, col, m, c):
        c = [color_code(c[i], 1) for i in range(len(c))]
        self.marker = insert(self.marker, m, row, col)
        self.color = insert(self.color, c, row, col)

    def pad(self, side, m, c, b): # it adds data to the matrix on the specified side
        # m is now a matrixminimum
        c = [[color_code(c, 1) for i in el] for el in m]
        b = [[color_code(b, 0) for i in el] for el in m]
        self.marker = pad_matrix(self.marker, m, side)
        self.color = pad_matrix(self.color, c, side)
        self.background = pad_matrix(self.background, b, side)
        self.update_size()
    
    def update(self, x, y, m, c): # it updates the matrix of markers and colors 
        if self.marker == []:
            return 
        for i in range(len(x)):
            cx, rx = floor(x[i]), floor(y[i])
            if 0 <= cx < self.cols and 0 <= rx < self.rows:
                if c[i][0] == 3:
                    print(m[i])
                self.marker[self.rows - 1 - rx][cx] = sum_markers(self.marker[self.rows - 1 - rx][cx], m[i])
                self.color[self.rows - 1 - rx][cx] = sum_colors(self.color[self.rows - 1 - rx][cx], c[i])




