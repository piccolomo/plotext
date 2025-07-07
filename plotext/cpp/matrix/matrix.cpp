class Matrix {
private:
  Line * lines;  // Pointer to an array of Line
  size_t height;           // Height (number of rows) of the matrix

public:
  // Constructor that initializes the Matrix with given width and height
  Matrix(const size_t & w, const size_t & h) noexcept : lines(new Line[h]), height(h) {create(h); create_lines(w);}

  // Constructor that initializes Matrix and fills it with the given Pixel
  Matrix(const size_t & w, const size_t & h, const Pixel & p) noexcept : Matrix(w, h) {fill_pixel(p);}

  // Constructor that initializes Matrix and fills it with the given CharacterHD
  Matrix(const size_t & w, const size_t & h, const CharacterHD &c) noexcept : Matrix(w, h) {fill_character(c);}

  // Copy constructor: Deep copy from another matrix
  Matrix(const Matrix & other) noexcept { 
    create(other.height); 
    create_lines(other.get_width());
    copy_from(other);}

  // Destructor that cleans up the allocated memory for lines
  ~Matrix() noexcept {delete[] lines; lines = nullptr;}

  // Assignment operator: Releases memory and copies data from another matrix
  Matrix & operator=(const Matrix & other) noexcept { 
    destroy(); 
    create(other.height); 
    copy_from(other); 
    return *this;}

    // Releases allocated memory
  void destroy() noexcept {delete[] lines; lines = nullptr;}

    // Allocates memory for lines
  void create(const size_t & h) noexcept {height = h; lines = new Line[height];}

    // Initializes lines with given width and character
  void create_lines(const size_t & w, const CharacterHD & c = CharacterHD()) noexcept { 
    for (int row = 0; row < height; row++) {Line *address = & lines[row]; new(address) Line(w, c);}}

    // Copies data from another matrix
  void copy_from(const Matrix & other) noexcept {for (size_t i = 0; i < min(height, other.height); ++i) {lines[i].copy_from(other.lines[i]);}}

  // Resizes the matrix
  void resize(const size_t & w, const size_t & h) noexcept { 
    Matrix temp(*this);
    destroy(); 
    create(h); 
    create_lines(w);
    copy_from(temp);}

  // Clears all lines in the matrix
  void clear() noexcept {for (size_t row = 0; row < height; row++) {lines[row].clear();}}


  // Returns the height (number of rows) of the matrix
  size_t get_height() const noexcept {return height;}

  // Returns the width (number of columns) of the matrix
  size_t get_width() const noexcept { 
    if (height == 0) {return 0; } 
    else {return lines[0].get_width();}}

  // Returns the Line at the specified row
  Line & get_line(const size_t & row) const noexcept {return lines[row];}

  // Returns the CharacterHD at the specified column and row
  CharacterHD & get_character(const size_t &col, const size_t &row) const noexcept {return lines[row].get_character(col);}

  // Checks if a specified region is empty
  bool is_empty(const size_t col_start, const size_t col_stop, const size_t row_start, const size_t row_stop) const noexcept { 
    for (size_t row = row_start; row < row_stop; row++) { 
      if (!lines[row].is_empty(col_start, col_stop)) {return false;}} 
    return true;}


  // Fills the entire matrix with the given Pixel
  void fill_pixel(const Pixel &p = Pixel()) noexcept {for (size_t row = 0; row < height; row++) {lines[row].fill_pixel(p);}}

  // Fills the entire matrix with the given CharacterHD
  void fill_character(const CharacterHD & c) noexcept {for (size_t row = 0; row < height; row++) {lines[row].fill_character(c);}}


  // Inserts a CharacterHD at the specified row and column
  void set_character(const size_t & col, const size_t & row, const CharacterHD & c) noexcept {lines[row].set_character(col, c);}

    // Sets a wide character at the specified column and row.
  void set_wcharacter(const size_t & col, const size_t & row, const wchar_t & cs) noexcept {get_character(col, row).set_wcharacter(cs);}

  // Sets a pixel at the specified column and row.
  void set_pixel(const size_t & col, const size_t & row, const Pixel & p) noexcept {get_character(col, row).set_pixel(p);}


  // Inserts a wide string at the specified column and row in the matrix.
  void insert_wstring(const size_t & col, const size_t & row, const wstring & s) noexcept {lines[row].insert_wstring(col, s);}

  // Inserts a line at a specified position
  void insert_line(const size_t & col, const size_t & row, const Line & s) noexcept {lines[row].insert_line(col, s);}

  // Inserts a matrix into the current matrix at a specific position
  void insert_matrix(const size_t & col, const size_t & row, const Matrix & m) noexcept {for (size_t r = 0; r < m.get_height(); r++) {lines[row + r].insert_line(col, m.lines[r]);}} 

  void insert_matrix_aligned(const size_t & col, size_t row, const Matrix & m, const Alignment & ha = -1, const Alignment & va = -1) noexcept {
    size_t m_height = m.get_height();
    row += va.get_displacement(m_height);
    if (row < 0 or row + m_height > height or row >= height) {return;}
    for (size_t r = 0; r < m_height; r++) {lines[row + r].insert_line_aligned(col, m.lines[r], ha);}}

  // Inserts with alignment and additional options
  bool insert_colorized_aligned(const size_t & col, const size_t & row, const Colorize & s, const Alignment & ha = -1, const bool & check_space = false, const bool & change_color = true) 
    noexcept {return lines[row].insert_colorized_aligned(col, s, ha, check_space, change_color);}

  // Inserts dynamically based on alignment
  int insert_colorized_dynamically(const size_t & col, const size_t & row, const Colorize & s) noexcept {return lines[row].insert_colorized_dynamically(col, s);}

  // Inserts dots into the matrix (using Dots object)
  void insert_dots(Dots dots) noexcept {
    size_t length = dots.get_length();
    for (size_t i = 0; i < length; i++) {
      Dot & dot = dots.get(i);
      set_character(dot.get_col(), dot.get_row(), dot.get_character_hd());}}


  // Stacks two matrices vertically
  Matrix vstack(const Matrix & m, const bool & adapt = false) noexcept { 
    size_t width; 
    if (adapt) {width = max(get_width(), m.get_width());} 
    else {width = get_width();} 
    Matrix out(width, get_height() + m.get_height()); 
    out.insert_matrix(0, 0, *this); 
    out.insert_matrix(0, get_height(), m); 
    return out;}

  // Stacks two matrices horizontally
  Matrix hstack(const Matrix & m, const bool & adapt = false) noexcept { 
    size_t height; 
    if (adapt) { 
      height = max(get_height(), m.get_height());} 
    else {height = get_height();} 
    Matrix out(get_width() + m.get_width(), height); 
    out.insert_matrix(0, 0, *this); 
    out.insert_matrix(get_width(), 0, m); 
    return out;}

  // Creates a deep copy of the matrix
  Matrix copy() const noexcept {return Matrix(*this);}

  // Extracts a part of the matrix based on the specified column and row range
  Matrix part(const size_t & col_start, const size_t & col_stop, const size_t & row_start, const size_t & row_stop) const noexcept { 
    size_t new_height = min(row_stop - row_start, height); 
    size_t new_width = min(col_stop - col_start, get_width()); 
    Matrix m(new_width, new_height); 
    for (size_t row = 0; row < new_height; row++) { 
      m.lines[row] = lines[row_start + row].part(col_start, col_stop);} 
    return m;}

  // Extracts a part of the matrix based on the specified column and row stop
  Matrix part(const size_t & col_stop, const size_t & row_stop) const noexcept {return part(0, col_stop, 0, row_stop);}

  // Transposes the matrix (flips rows and columns)
  Matrix transpose() const noexcept { 
    size_t width = get_width(); 
    Matrix novel(height, width); 
    for (size_t col = 0; col < height; col++) { 
      for (size_t row = 0; row < width; row++) { 
        novel.get_character(col, row) = get_character(row, col);}} 
    return novel;}


  // Converts the matrix to a buffer (for display or storage)
  void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept { 
    for (size_t row = 0; row < height; row++) {lines[row].to_buffer(buffer, length_buffer); 
      if (row != height - 1) {cstring_to_buffer(new_line, buffer, length_buffer);}}}


    // Converts the matrix to a buffer (for display or storage)
  void to_colorless_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept { 
        for (size_t row = 0; row < height; row++) {lines[row].to_colorless_buffer(buffer, length_buffer); 
      if (row != height - 1) {cstring_to_buffer(new_line, buffer, length_buffer);}}}

  // Converts the matrix to a wide string (with optional color removal)
  wstring get_wstring(const bool & colorless = false) const noexcept { 
    size_t buffer_size = character_size_max * get_width() * height + height; 
    wchar_t buffer[buffer_size + 1]; 
    buffer[0] = '\0'; 
    size_t length = 0; 
    if (colorless) {to_colorless_buffer(buffer, length);} else {to_buffer(buffer, length);}
    wstring out(buffer); 
    return out;}

  // Displays the matrix (with optional color removal)
  void print(const bool & colorless = false) const noexcept {wcout << get_wstring(colorless) << flush;};
      
};


// Converts a Colorize object into a Matrix with appropriate alignment and dimensions.
Matrix colorize_to_matrix(const Colorize & c) noexcept {
    vector<wstring> wstrings = split_wstring(c.get_string()); // Split the input string by new line.
    size_t width = get_width_strings(wstrings); // Get the maximum width of strings.
    size_t height = wstrings.size(); // Determine the number of rows.
    Matrix out(width, height); // Initialize output matrix with width and height.
    for (size_t row = 0; row < height; row++) {
        wstring s = wstrings.at(row); // Get the current string for the row.
        Colorize cs(s, c); // Create a Colorize object for the string.
        out.insert_colorized_aligned(0, row, cs, -1, 0, 1);} // Insert aligned Colorize string into the matrix.
    return out;}


extern "C" {

  Matrix * matrix_new(size_t width, size_t height, Pixel * p) noexcept {return new Matrix(width, height, *p);}
  void matrix_clear(Matrix * m) noexcept {m->clear();}
  void matrix_delete(Matrix * p) noexcept {delete p;}

  size_t matrix_get_width(Matrix * matrix) noexcept {return matrix->get_width();}
  size_t matrix_get_height(Matrix * matrix) noexcept {return matrix->get_height();}
  bool matrix_is_empty(Matrix * m, size_t col_start, size_t col_stop, size_t row_start, size_t row_stop) noexcept {return m->is_empty(col_start, col_stop, row_start, row_stop);}

  void matrix_resize(Matrix * m, size_t width, size_t height) noexcept {m->resize(width, height);}
  void matrix_fill_pixel(Matrix * m, Pixel * p) noexcept {m->fill_pixel(*p);}

  const wchar_t * matrix_get_wstring(Matrix * m, bool colorless) noexcept {return wstring_to_cstring(m->get_wstring(colorless));}
  void wstring_delete(wchar_t * wstr) noexcept {delete_cstring(wstr);}

  Matrix * matrix_vstack(Matrix * m1, Matrix * m2, bool adapt = 0) noexcept {return new Matrix(m1->vstack(*m2, adapt));}
  Matrix * matrix_hstack(Matrix * m1, Matrix * m2, bool adapt = 0) noexcept {return new Matrix(m1->hstack(*m2, adapt));}

  Matrix * matrix_part(const Matrix * m, size_t col_start, size_t col_stop, size_t row_start, size_t row_stop) noexcept {return new Matrix(m->part(col_start, col_stop, row_start, row_stop));}
  Matrix * matrix_copy(const Matrix * m) noexcept {return new Matrix(*m);}

  void matrix_set_wcharacter(Matrix * m, size_t col, size_t row, wchar_t cs) noexcept {m->set_wcharacter(col, row, cs);}
  void matrix_set_pixel(Matrix * m, size_t col, size_t row, Pixel * p) noexcept {m->set_pixel(col, row, *p);}

  void matrix_insert_wstring(Matrix * m, size_t col, size_t row, wchar_t * s) noexcept {m->insert_wstring(col, row, s);}
  void matrix_insert_matrix(Matrix * m, size_t col, size_t row, Matrix * mi) noexcept {m->insert_matrix(col, row, *mi);}
  void matrix_insert_matrix_aligned(Matrix * m, size_t col, size_t row, Matrix * mi, int ha, int va) noexcept {m->insert_matrix_aligned(col, row, *mi, ha, va);}
  bool matrix_insert_colorized_aligned(Matrix * m, size_t col, size_t row, Colorize * c, int ha, bool check_space, bool change_color) noexcept {return m->insert_colorized_aligned(col, row, *c, ha, check_space, change_color);} 
  int matrix_insert_colorized_dynamically(Matrix * m, size_t col, size_t row, const Colorize * c) noexcept {return m->insert_colorized_dynamically(col, row, *c);}
  void matrix_insert_dots(Matrix * m, Dots * dots) noexcept {m->insert_dots(*dots);}

  void matrix_print(Matrix * matrix, bool colorless) noexcept {matrix->print(colorless);}

  Matrix * colorize_get_matrix(Colorize * c) noexcept {return new Matrix(colorize_to_matrix(*c));}

}