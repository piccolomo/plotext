import plotext._utility as ut

class matrix_class():
    def __init__(self):
        self.set_size(0, 0)
        self.set_axes_color()
        self.set_canvas_area(0, 0, 0, 0)
        self.set_canvas_color()
        self.set_matrices()
        self.set_canvas()
        
    def set_size(self, cols, rows):
        self.rows = rows; self.Rows = range(self.rows)
        self.cols = cols; self.Cols = range(self.cols)
        self.size = [self.rows, self.cols]

    def update_size(self):
        self.cols, self.rows = ut.matrix_size(self.marker)
        self.Rows = range(self.rows); self.Cols = range(self.cols)
        self.size = [self.rows, self.cols]

    def set_axes_color(self, color = ut.no_color):
        self.axes_color = color

    def set_canvas_area(self, col1, col2, row1, row2):
        self.Cols_canvas = range(col1, col2)
        self.Rows_canvas = range(row1, row2)

    def set_canvas_color(self, color = ut.no_color):
        self.canvas_color = color

    def in_canvas(self, col, row):
        return col in self.Cols_canvas and row in self.Rows_canvas

    def set_matrices(self):
        self.marker = [[ut.space] * self.cols for row in self.Rows]
        self.fullground = [[ut.no_color] * self.cols for row in self.Rows]
        get_background = lambda col, row: self.canvas_color if self.in_canvas(col, row) else self.axes_color
        self.background = [[get_background(col, row) for col in self.Cols] for row in self.Rows]
        self.style = [[ut.no_color] * self.cols for row in self.Rows]

    def legal(self, col, row):
        return col in self.Cols and row in self.Rows

    def get_marker(self, col, row):
        return self.marker[row][col] #if self.legal(col, row) else "OUT"

    def get_marker_row(self, row):
        return self.marker[row] #if self.legal(0, row) else "OUT"

    def get_marker_col(self, col):
        return [self.marker[r][col] for r in self.Rows]#if self.legal(0, row) else "OUT"

    def set_marker(self, col, row, marker):
        self.marker[row][col] = marker
        
    def set_fullground(self, col, row, fullground = None):
        self.fullground[row][col] = fullground
        
    def set_background(self, col, row, background = None):
        self.background[row][col] = background
            
    def set_style(self, col, row, style = None):
        self.style[row][col] = style

    def insert_element(self, col, row, marker, fullground = None, style = None, background = None, check_canvas = False):
        test_canvas = True if check_canvas is False else col in self.Cols_canvas and row in self.Rows_canvas
        if self.legal(col, row) and test_canvas:
            self.set_marker(col, row, marker)
            self.set_fullground(col, row, fullground) if fullground is not None else None
            self.set_background(col, row, background) if background is not None else None
            self.set_style(col, row, style) if style is not None else None

    def add_horizontal_string(self, col, row, string, fullground = None, style = None, background = None, alignment = "left", check_space = False, check_canvas = False):
        l = len(string); L = range(l)
        col = col if alignment == "left" else col - l // 2 if alignment == "center" else col - l + 1 if alignment == "right" else ut.correct_coord(self.get_marker_row(row), string, col) # if dynamic
        b, e = max(col - 1, 0), min(col + l + 1, self.cols)
        test_space = all([self.get_marker(c, row) == ut.space for c in range(b, e)]) and col >= 0 and col + l <= self.cols if check_space else True
        [self.insert_element(col + i, row, string[i], fullground, style, background, check_canvas) for i in L] if test_space else None
        return test_space

    def add_vertical_string(self, col, row, string, fullground = None, style = None, background = None,  alignment = "bottom", check_canvas = False):
        l = len(string); L = range(l)
        row = row if alignment == "bottom" else row - l // 2 if alignment == "center" else row - l + 1 #if alignment == "top"
        [self.insert_element(col, row + i, string[i], fullground, style, background, check_canvas) for i in L]

    def add_multiple_horizontal_strings(self, col, row, string, fullground = None, style = None, background = None, alignment = "left", check_space = False, check_canvas = False):
        strings = ''.join(string).split('\n'); S = len(strings)
        [self.add_horizontal_string(col, row - s, strings[s], fullground, style, background, alignment, check_space, check_canvas) for s in range(S)]

    def add_multiple_vertical_strings(self, col, row, string, fullground = None, style = None, background = None, alignment = "left", check_canvas = False):
        strings = ''.join(string).split('\n'); S = len(strings)
        [self.add_vertical_string(col + s, row, strings[s], fullground, style, background, alignment, check_canvas) for s in range(S)]

    def get_colors(self, col, row):
        return [self.fullground[row][col], self.style[row][col], self.background[row][col]] #if self.legal(col, row) else ["OUT"] * 3

    def set_canvas(self):
        canvas = ''
        for row in self.Rows[::-1]:
            for col in self.Cols:
                marker = self.marker[row][col]
                colors = self.get_colors(col, row)
                if col == 0 or colors != self.get_colors(col - 1, row):
                    ansi = ut.colors_to_ansi(*colors)
                    canvas += ansi
                canvas += marker
                if col == self.cols - 1 or colors != self.get_colors(col + 1, row):
                    #ansi_next = colors_to_ansi(*colors_next)
                    canvas += ut.ansi_end  #+ ansi_next
            canvas += '\n'

        self.canvas = canvas
        #print(repr(canvas))
        #self.canvas = '\n'.join([''.join(self.marker[row]) for row in self.Rows])
        return self.canvas

    def get_canvas(self):
        return self.canvas

    def hstack(self, extra):
        self.marker = ut.hstack(self.marker, extra.marker)
        self.fullground = ut.hstack(self.fullground, extra.fullground)
        self.background = ut.hstack(self.background, extra.background)
        self.style = ut.hstack(self.style, extra.style)
        self.update_size()
        self.canvas = '';
        
    def vstack(self, extra):
        self.marker = ut.vstack(self.marker, extra.marker)
        self.fullground = ut.vstack(self.fullground, extra.fullground)
        self.background = ut.vstack(self.background, extra.background)
        self.style = ut.vstack(self.style, extra.style)
        self.update_size()
        self.canvas = ''

    def to_html(self): # turns a matrix of character in html form
        code = lambda color: "rgb" + str(color).replace(" ", "")
        #html = "<body>\n<p style=\"font-family:courier; font-size:11pt;\">\n\n"
        html = "<body> \n <code style = style=\"font-family:courier; \"font-size : 10pt;\"> \n\n"
        for r in range(self.rows - 1, -1, -1):
            for c in range(self.cols):
                marker = self.get_marker(c, r)
                color, style, background = self.get_colors(c, r)
                marker = "&nbsp;" if marker == ut.space else marker
                marker = '<b>' + marker + '</b>' if style == 'bold' else marker
                marker = '<i>' + marker + '</i>' if style == 'italic' else marker
                color = 'black' if color == ut.no_color else color
                background = 'white' if background == ut.no_color else background
                color = ut.to_rgb(color)
                background = ut.to_rgb(background)
                color = code(color)
                background = code(background)
                html += "<span style = \"color:" + color + "; background-color: " + background + "\">" + marker + "</span>"
            html += " <br>\n\n"
        html += "<code> \n </body>"
        return html

def join_matrices(matrices): # from a matrix of matrix_class() objects to a single matrix
    cols, rows = ut.matrix_size(matrices)
    M = matrix_class()
    for r in range(rows):
        m_rows = matrices[r][0].rows
        m = matrix_class()
        m.set_size(0, m_rows)
        m.set_matrices()
        for c in range(cols):
            m.hstack(matrices[r][c])
        M.vstack(m)
    return M

