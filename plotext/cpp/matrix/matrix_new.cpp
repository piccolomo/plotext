
class Matrix {
private:
  CharacterHD * data;   // contiguous buffer of size width * height
  size_t width;
  size_t height;

  // helper: index into data
  inline size_t idx(const size_t & col, const size_t & row) const noexcept {
    return row * width + col;
  }

public:
  // Default
  Matrix() noexcept : data(nullptr), width(0), height(0) {}

  // Constructor width x height
  Matrix(const size_t & w, const size_t & h) noexcept
    : data(nullptr), width(w), height(h)
  {
    if (w == 0 || h == 0) { data = nullptr; }
    else { data = new CharacterHD[w * h]; }
  }

  // Constructor filled with Pixel
  Matrix(const size_t & w, const size_t & h, const Pixel & p) noexcept
    : Matrix(w, h) { fill_pixel(p); }

  // Constructor filled with CharacterHD
  Matrix(const size_t & w, const size_t & h, const CharacterHD & c) noexcept
    : Matrix(w, h) { fill_character(c); }

  // Copy constructor (deep)
  Matrix(const Matrix & other) noexcept
    : data(nullptr), width(other.width), height(other.height)
  {
    if (width == 0 || height == 0) { data = nullptr; }
    else {
      data = new CharacterHD[width * height];
      for (size_t i = 0; i < width * height; ++i) data[i] = other.data[i];
    }
  }

  // Move constructor
  Matrix(Matrix && other) noexcept
    : data(other.data), width(other.width), height(other.height)
  {
    other.data = nullptr;
    other.width = other.height = 0;
  }

  // Destructor
  ~Matrix() noexcept { delete[] data; data = nullptr; }

  // Copy assignment (copy-and-swap)
  Matrix & operator=(Matrix other) noexcept {
    swap(*this, other);
    return *this;
  }

  friend void swap(Matrix & a, Matrix & b) noexcept {
    std::swap(a.data, b.data);
    std::swap(a.width, b.width);
    std::swap(a.height, b.height);
  }

  // destroy (release memory)
  void destroy() noexcept {
    delete[] data;
    data = nullptr;
    width = height = 0;
  }

  // create (like original)
  void create(const size_t & h) noexcept {
    // resize rows only isn't meaningful without width: set height and allocate only if width>0
    height = h;
    if (width == 0 || height == 0) {
      delete[] data;
      data = nullptr;
    } else {
      delete[] data;
      data = new CharacterHD[width * height];
    }
  }

  // create_lines(w) previously constructed each Line; now resize width and allocate contiguous buffer
  void create_lines(const size_t & w, const CharacterHD & c = CharacterHD()) noexcept {
    // allocate new buffer of new width but keep height
    size_t new_w = w;
    size_t new_h = height;
    delete[] data;
    width = new_w;
    if (width == 0 || new_h == 0) { data = nullptr; return; }
    data = new CharacterHD[width * new_h];
    // initialize with c
    for (size_t i = 0; i < width * new_h; ++i) data[i] = c;
  }

  // copy_from from other matrix (copy overlapping region)
  void copy_from(const Matrix & other) noexcept {
    size_t minw = std::min(width, other.width);
    size_t minh = std::min(height, other.height);
    for (size_t r = 0; r < minh; ++r) {
      // copy row block
      const CharacterHD * src = other.data + r * other.width;
      CharacterHD * dst = data + r * width;
      for (size_t c = 0; c < minw; ++c) dst[c] = src[c];
    }
  }

  // resize (like original: preserve current contents as best as possible)
  void resize(const size_t & w, const size_t & h) noexcept {
    if (w == width && h == height) return;
    // create temp copy
    Matrix temp(*this);
    delete[] data;
    width = w;
    height = h;
    if (width == 0 || height == 0) { data = nullptr; return; }
    data = new CharacterHD[width * height];
    // fill with default constructed CharacterHD
    for (size_t i = 0; i < width * height; ++i) data[i] = CharacterHD();
    // copy back overlap
    copy_from(temp);
  }

  // clear (calls clear on each CharacterHD)
  void clear() noexcept {
    if (!data) return;
    for (size_t i = 0; i < width * height; ++i) data[i].clear();
  }

  // getters
  size_t get_height() const noexcept { return height; }
  size_t get_width() const noexcept { return width; }

  // get_line: returns a Line by value constructed from row data
  // (original returned Line&, but we no longer own Line instances)
  Line get_line(const size_t & row) const noexcept {
    size_t w = get_width();
    Line out(w);
    if (row >= height || w == 0) return out;
    const CharacterHD * src = data + row * width;
    for (size_t c = 0; c < w; ++c) out.set_character(c, src[c]); // Line::set_character used
    return out;
  }

  // get_character (returns reference into the buffer)
  CharacterHD & get_character(const size_t & col, const size_t & row) noexcept {
    return data[idx(col, row)];
  }

  const CharacterHD & get_character(const size_t & col, const size_t & row) const noexcept {
    return data[idx(col, row)];
  }

  // is_empty: checks if region is empty
  bool is_empty(const size_t col_start, const size_t col_stop, const size_t row_start, const size_t row_stop) const noexcept {
    if (col_start >= col_stop || row_start >= row_stop) return true;
    size_t cs = col_start, ce = std::min(col_stop, width);
    size_t rs = row_start, re = std::min(row_stop, height);
    for (size_t r = rs; r < re; ++r) {
      for (size_t c = cs; c < ce; ++c) {
        if (!get_character(c, r).is_empty()) return false;
      }
    }
    return true;
  }

  // fill_pixel: set pixel on each CharacterHD
  void fill_pixel(const Pixel & p = Pixel()) noexcept {
    if (!data) return;
    for (size_t i = 0; i < width * height; ++i) data[i].set_pixel(p);
  }

  // fill_character
  void fill_character(const CharacterHD & c) noexcept {
    if (!data) return;
    for (size_t i = 0; i < width * height; ++i) data[i] = c;
  }

  // set_character / set_wcharacter / set_pixel
  void set_character(const size_t & col, const size_t & row, const CharacterHD & c) noexcept {
    if (col >= width || row >= height) return;
    get_character(col, row) = c;
  }

  void set_wcharacter(const size_t & col, const size_t & row, const wchar_t & cs) noexcept {
    if (col >= width || row >= height) return;
    get_character(col, row).set_wcharacter(cs);
  }

  void set_pixel(const size_t & col, const size_t & row, const Pixel & p) noexcept {
    if (col >= width || row >= height) return;
    get_character(col, row).set_pixel(p);
  }

  // insert_wstring (row-level)
  void insert_wstring(const size_t & col, const size_t & row, const wstring & s) noexcept {
    if (row >= height) return;
    size_t len = s.size();
    for (size_t i = 0; i < len; ++i) {
      size_t c = col + i;
      if (c >= width) break;
      get_character(c, row).set_wcharacter(s[i]);
    }
  }

  // insert_line: insert a Line into a row at column
  void insert_line(const size_t & col, const size_t & row, const Line & s) noexcept {
    if (row >= height) return;
    size_t slen = s.get_width();
    for (size_t i = 0; i < slen; ++i) {
      size_t c = col + i;
      if (c >= width) break;
      get_character(c, row) = s.get_character(i);
    }
  }

  // insert_matrix: copy src matrix into *this at (col,row)
  void insert_matrix(const size_t & col, const size_t & row, const Matrix & m) noexcept {
    size_t mh = m.get_height();
    size_t mw = m.get_width();
    for (size_t r = 0; r < mh && (row + r) < height; ++r) {
      for (size_t c = 0; c < mw && (col + c) < width; ++c) {
        get_character(col + c, row + r) = m.get_character(c, r);
      }
    }
  }

  // insert_matrix_aligned: use Alignment for vertical placement and line-level insert_line_aligned for horizontal alignment
  void insert_matrix_aligned(const size_t & col, size_t row, const Matrix & m, const Alignment & ha = -1, const Alignment & va = -1) noexcept {
    size_t m_height = m.get_height();
    row += va.get_displacement(m_height);
    if ((int)row < 0 || row >= height || row + m_height > height) { return; }
    for (size_t r = 0; r < m_height; ++r) {
      // compute horizontal center/disp for this row
      size_t target_row = row + r;
      // We can use insert_line with horizontal displacement computed by ha.get_displacement
      int disp = ha.get_displacement(m.get_width());
      size_t c = col + disp;
      // bounds handling inside insert_line
      insert_line(c, target_row, m.get_line(r));
    }
  }

  // insert_colorized_aligned (row-level): bring over Line implementation but operate on buffer directly
  bool insert_colorized_aligned(const size_t & col, const size_t & row, const Colorize & s, const Alignment & ha = -1, const bool & check_space = false, const bool & change_color = true) noexcept {
    if (row >= height) return false;
    size_t length = width;
    size_t slength = s.get_length();
    int c_int = (int)col + ha.get_displacement(slength);
    if (c_int < 0) return false;
    size_t c = (size_t)c_int;
    size_t start = (c == 0) ? 0 : (c - 1);
    size_t stop = std::min(length, c + slength + 1);
    if (check_space && (c_int < 0 || c + slength > length || !is_empty(start, stop, row, row + 1))) { return false; }
    for (size_t i = 0; i < slength; ++i) {
      size_t colpos = c + i;
      if (colpos >= width) break;
      get_character(colpos, row).set_wcharacter(s.get_wcharacter(i));
      if (change_color) { get_character(colpos, row).set_pixel(s); }
    }
    return true;
  }

  // helper: absolute insertion at a column without Alignment object (used by dynamic)
  bool insert_colorized_aligned_at(const size_t & col, const size_t & row, const Colorize & s, const bool & check_space = false, const bool & change_color = true) noexcept {
    if (row >= height) return false;
    size_t length = width;
    size_t slength = s.get_length();
    if (col + slength > length) return false;
    size_t start = (col == 0) ? 0 : (col - 1);
    size_t stop = std::min(length, col + slength + 1);
    if (check_space && !is_empty(start, stop, row, row + 1)) return false;
    for (size_t i = 0; i < slength; ++i) {
      size_t colpos = col + i;
      get_character(colpos, row).set_wcharacter(s.get_wcharacter(i));
      if (change_color) get_character(colpos, row).set_pixel(s);
    }
    return true;
  }

  // insert_colorized_dynamically: try offsets 0, -1, +1, -2, +2, ...
  int insert_colorized_dynamically(const size_t & col, const size_t & row, const Colorize & s) noexcept {
    if (row >= height) return -1;
    size_t w = s.get_length();
    // generate deltas: 0, -1, +1, -2, +2, ...
    for (size_t delta = 0; delta <= width; ++delta) {
      if (delta == 0) {
        if (insert_colorized_aligned_at(col, row, s, true, true)) return (int)col;
      } else {
        // try left
        if (col >= delta) {
          size_t cleft = col - delta;
          if (insert_colorized_aligned_at(cleft, row, s, true, true)) return (int)cleft;
        }
        // try right
        size_t cright = col + delta;
        if (cright + w <= width) {
          if (insert_colorized_aligned_at(cright, row, s, true, true)) return (int)cright;
        }
      }
    }
    return -1;
  }

      // Add a Point to the collection, creating or updating a Dot
  void add_point(const Point & p) noexcept {get_character(p.get_col(), p.get_row()).update(p);}

  void insert_signal(const Signal & signal) noexcept {
      for (auto & pf: signal) {
        for (Point & p: pf.get_filled_line()){add_point(p);}}}

  // vstack/hstack (create new matrices and insert)
  Matrix vstack(const Matrix & m, const bool & adapt = false) const noexcept {
    size_t out_w = adapt ? std::max(get_width(), m.get_width()) : get_width();
    Matrix out(out_w, get_height() + m.get_height());
    out.insert_matrix(0, 0, *this);
    out.insert_matrix(0, get_height(), m);
    return out;
  }

  Matrix hstack(const Matrix & m, const bool & adapt = false) const noexcept {
    size_t out_h = adapt ? std::max(get_height(), m.get_height()) : get_height();
    Matrix out(get_width() + m.get_width(), out_h);
    out.insert_matrix(0, 0, *this);
    out.insert_matrix(get_width(), 0, m);
    return out;
  }

  // copy
  Matrix copy() const noexcept { return Matrix(*this); }

  // part: returns submatrix col_start..col_stop-1, row_start..row_stop-1
  Matrix part(const size_t & col_start, const size_t & col_stop, const size_t & row_start, const size_t & row_stop) const noexcept {
    size_t new_height = std::min(row_stop - row_start, height);
    size_t new_width = std::min(col_stop - col_start, width);
    Matrix m(new_width, new_height);
    for (size_t r = 0; r < new_height; ++r) {
      for (size_t c = 0; c < new_width; ++c) {
        m.set_character(c, r, get_character(col_start + c, row_start + r));
      }
    }
    return m;
  }

  Matrix part(const size_t & col_stop, const size_t & row_stop) const noexcept {
    return part(0, col_stop, 0, row_stop);
  }

  // transpose
  Matrix transpose() const noexcept {
    size_t w = get_width();
    size_t h = get_height();
    Matrix novel(h, w);
    for (size_t col = 0; col < h; ++col) {
      for (size_t row = 0; row < w; ++row) {
        novel.set_character(col, row, get_character(row, col));
      }
    }
    return novel;
  }

void to_buffer(wchar_t* buffer, size_t& length_buffer) const noexcept {
    for (size_t y = 0; y < height; ++y) {
      size_t row_offset = y * width;
      for (size_t x = 0; x < width; ++x)
          data[row_offset + x].to_buffer(buffer, length_buffer);
      buffer[length_buffer++] = L'\n';  // inline newline, no function call
}}

//     for (size_t y = 0; y < height; ++y) {
//         for (size_t x = 0; x < width; ++x)
//             get_character(x, y).to_buffer(buffer, length_buffer);
//         wchar_to_buffer(L'\n', buffer, length_buffer);
//     }
// }

  // to_colorless_buffer
  void to_colorless_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
    for (size_t row = 0; row < height; ++row) {
      Line temp = get_line(row);
      temp.to_colorless_buffer(buffer, length_buffer);
      if (row != height - 1) cstring_to_buffer(new_line, buffer, length_buffer);
    }
  }

  // get_wstring (build wide string)
  wstring get_wstring(const bool & colorless = false) const noexcept {
    size_t buffer_size = character_size_max * get_width() * height + height;
    // allocate on stack only if small; original used stack array - replicate but safer to allocate vector
    vector<wchar_t> buffer(buffer_size + 1);
    buffer[0] = L'\0';
    size_t length = 0;
    if (colorless) to_colorless_buffer(buffer.data(), length);
    else to_buffer(buffer.data(), length);
    return wstring(buffer.data());
  }

  // print
  void print(const bool & colorless = false) const noexcept {
    wcout << get_wstring(colorless) << flush;
  }
};


// class Matrix {
// private:
//   Line * lines;  // Pointer to an array of Line
//   size_t height;           // Height (number of rows) of the matrix

// public:
//   // Constructor that initializes the Matrix with given width and height
//   Matrix(const size_t & w, const size_t & h) noexcept : lines(new Line[h]), height(h) {create(h); create_lines(w);}

//   // Constructor that initializes Matrix and fills it with the given Pixel
//   Matrix(const size_t & w, const size_t & h, const Pixel & p) noexcept : Matrix(w, h) {fill_pixel(p);}

//   // Constructor that initializes Matrix and fills it with the given CharacterHD
//   Matrix(const size_t & w, const size_t & h, const CharacterHD &c) noexcept : Matrix(w, h) {fill_character(c);}

//   // Copy constructor: Deep copy from another matrix
//   Matrix(const Matrix & other) noexcept { 
//     create(other.height); 
//     create_lines(other.get_width());
//     copy_from(other);}

//   // Destructor that cleans up the allocated memory for lines
//   ~Matrix() noexcept {delete[] lines; lines = nullptr;}

//   // Assignment operator: Releases memory and copies data from another matrix
//   Matrix & operator=(const Matrix & other) noexcept { 
//     destroy(); 
//     create(other.height); 
//     copy_from(other); 
//     return *this;}

//     // Releases allocated memory
//   void destroy() noexcept {delete[] lines; lines = nullptr;}

//     // Allocates memory for lines
//   void create(const size_t & h) noexcept {height = h; lines = new Line[height];}

//     // Initializes lines with given width and character
//   void create_lines(const size_t & w, const CharacterHD & c = CharacterHD()) noexcept { 
//     for (int row = 0; row < height; row++) {Line *address = & lines[row]; new(address) Line(w, c);}}

//     // Copies data from another matrix
//   void copy_from(const Matrix & other) noexcept {for (size_t i = 0; i < min(height, other.height); ++i) {lines[i].copy_from(other.lines[i]);}}

//   // Resizes the matrix
//   void resize(const size_t & w, const size_t & h) noexcept { 
//     Matrix temp(*this);
//     destroy(); 
//     create(h); 
//     create_lines(w);
//     copy_from(temp);}

//   // Clears all lines in the matrix
//   void clear() noexcept {for (size_t row = 0; row < height; row++) {lines[row].clear();}}


//   // Returns the height (number of rows) of the matrix
//   size_t get_height() const noexcept {return height;}

//   // Returns the width (number of columns) of the matrix
//   size_t get_width() const noexcept { 
//     if (height == 0) {return 0; } 
//     else {return lines[0].get_width();}}

//   // Returns the Line at the specified row
//   Line & get_line(const size_t & row) const noexcept {return lines[row];}

//   // Returns the CharacterHD at the specified column and row
//   CharacterHD & get_character(const size_t &col, const size_t &row) const noexcept {return lines[row].get_character(col);}

//   // Checks if a specified region is empty
//   bool is_empty(const size_t col_start, const size_t col_stop, const size_t row_start, const size_t row_stop) const noexcept { 
//     for (size_t row = row_start; row < row_stop; row++) { 
//       if (!lines[row].is_empty(col_start, col_stop)) {return false;}} 
//     return true;}


//   // Fills the entire matrix with the given Pixel
//   void fill_pixel(const Pixel &p = Pixel()) noexcept {for (size_t row = 0; row < height; row++) {lines[row].fill_pixel(p);}}

//   // Fills the entire matrix with the given CharacterHD
//   void fill_character(const CharacterHD & c) noexcept {for (size_t row = 0; row < height; row++) {lines[row].fill_character(c);}}


//   // Inserts a CharacterHD at the specified row and column
//   void set_character(const size_t & col, const size_t & row, const CharacterHD & c) noexcept {lines[row].set_character(col, c);}

//     // Sets a wide character at the specified column and row.
//   void set_wcharacter(const size_t & col, const size_t & row, const wchar_t & cs) noexcept {get_character(col, row).set_wcharacter(cs);}

//   // Sets a pixel at the specified column and row.
//   void set_pixel(const size_t & col, const size_t & row, const Pixel & p) noexcept {get_character(col, row).set_pixel(p);}


//   // Inserts a wide string at the specified column and row in the matrix.
//   void insert_wstring(const size_t & col, const size_t & row, const wstring & s) noexcept {lines[row].insert_wstring(col, s);}

//   // Inserts a line at a specified position
//   void insert_line(const size_t & col, const size_t & row, const Line & s) noexcept {lines[row].insert_line(col, s);}

//   // Inserts a matrix into the current matrix at a specific position
//   void insert_matrix(const size_t & col, const size_t & row, const Matrix & m) noexcept {for (size_t r = 0; r < m.get_height(); r++) {lines[row + r].insert_line(col, m.lines[r]);}} 

//   void insert_matrix_aligned(const size_t & col, size_t row, const Matrix & m, const Alignment & ha = -1, const Alignment & va = -1) noexcept {
//     size_t m_height = m.get_height();
//     row += va.get_displacement(m_height);
//     if (row < 0 or row + m_height > height or row >= height) {return;}
//     for (size_t r = 0; r < m_height; r++) {lines[row + r].insert_line_aligned(col, m.lines[r], ha);}}

//   // Inserts with alignment and additional options
//   bool insert_colorized_aligned(const size_t & col, const size_t & row, const Colorize & s, const Alignment & ha = -1, const bool & check_space = false, const bool & change_color = true) 
//     noexcept {return lines[row].insert_colorized_aligned(col, s, ha, check_space, change_color);}

//   // Inserts dynamically based on alignment
//   int insert_colorized_dynamically(const size_t & col, const size_t & row, const Colorize & s) noexcept {return lines[row].insert_colorized_dynamically(col, s);}

//   // //Inserts dots into the matrix (using Dots object)
//   // void insert_dots(Dots dots) noexcept {
//   //   size_t length = dots.get_length();
//   //   for (size_t i = 0; i < length; i++) {
//   //     Dot & dot = dots.at(i);
//   //     set_character(dot.get_col(), dot.get_row(), dot.get_character_hd());}}

//     // Add a Point to the collection, creating or updating a Dot
//   void add_point(const Point & p) noexcept {get_character(p.get_col(), p.get_row()).update(p);}

//   void insert_signal(const Signal & signal) noexcept {
//       for (auto & pf: signal) {
//         for (Point & p: pf.get_filled_line()){add_point(p);}}}

//   // Stacks two matrices vertically
//   Matrix vstack(const Matrix & m, const bool & adapt = false) noexcept { 
//     size_t width; 
//     if (adapt) {width = max(get_width(), m.get_width());} 
//     else {width = get_width();} 
//     Matrix out(width, get_height() + m.get_height()); 
//     out.insert_matrix(0, 0, *this); 
//     out.insert_matrix(0, get_height(), m); 
//     return out;}

//   // Stacks two matrices horizontally
//   Matrix hstack(const Matrix & m, const bool & adapt = false) noexcept { 
//     size_t height; 
//     if (adapt) { 
//       height = max(get_height(), m.get_height());} 
//     else {height = get_height();} 
//     Matrix out(get_width() + m.get_width(), height); 
//     out.insert_matrix(0, 0, *this); 
//     out.insert_matrix(get_width(), 0, m); 
//     return out;}

//   // Creates a deep copy of the matrix
//   Matrix copy() const noexcept {return Matrix(*this);}

//   // Extracts a part of the matrix based on the specified column and row range
//   Matrix part(const size_t & col_start, const size_t & col_stop, const size_t & row_start, const size_t & row_stop) const noexcept { 
//     size_t new_height = min(row_stop - row_start, height); 
//     size_t new_width = min(col_stop - col_start, get_width()); 
//     Matrix m(new_width, new_height); 
//     for (size_t row = 0; row < new_height; row++) { 
//       m.lines[row] = lines[row_start + row].part(col_start, col_stop);} 
//     return m;}

//   // Extracts a part of the matrix based on the specified column and row stop
//   Matrix part(const size_t & col_stop, const size_t & row_stop) const noexcept {return part(0, col_stop, 0, row_stop);}

//   // Transposes the matrix (flips rows and columns)
//   Matrix transpose() const noexcept { 
//     size_t width = get_width(); 
//     Matrix novel(height, width); 
//     for (size_t col = 0; col < height; col++) { 
//       for (size_t row = 0; row < width; row++) { 
//         novel.get_character(col, row) = get_character(row, col);}} 
//     return novel;}


//   // Converts the matrix to a buffer (for display or storage)
//   void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept { 
//     for (size_t row = 0; row < height; row++) {lines[row].to_buffer(buffer, length_buffer); 
//       if (row != height - 1) {cstring_to_buffer(new_line, buffer, length_buffer);}}}


//     // Converts the matrix to a buffer (for display or storage)
//   void to_colorless_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept { 
//         for (size_t row = 0; row < height; row++) {lines[row].to_colorless_buffer(buffer, length_buffer); 
//       if (row != height - 1) {cstring_to_buffer(new_line, buffer, length_buffer);}}}

//   // Converts the matrix to a wide string (with optional color removal)
//   wstring get_wstring(const bool & colorless = false) const noexcept { 
//     size_t buffer_size = character_size_max * get_width() * height + height; 
//     wchar_t buffer[buffer_size + 1]; 
//     buffer[0] = '\0'; 
//     size_t length = 0; 
//     if (colorless) {to_colorless_buffer(buffer, length);} else {to_buffer(buffer, length);}
//     wstring out(buffer); 
//     return out;}

//   // Displays the matrix (with optional color removal)
//   void print(const bool & colorless = false) const noexcept {wcout << get_wstring(colorless) << flush;};
      
// };


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
  //void matrix_insert_dots(Matrix * m, Dots * dots) noexcept {m->insert_dots(*dots);}
  void matrix_insert_signal(Matrix * m, Signal * dots) noexcept {m->insert_signal(*dots);}

  void matrix_print(Matrix * matrix, bool colorless) noexcept {matrix->print(colorless);}

  Matrix * colorize_get_matrix(Colorize * c) noexcept {return new Matrix(colorize_to_matrix(*c));}

}