class Matrix {
private:
    CharacterHD * data = nullptr; // Single contiguous array of CharacterHD
    size_t width = 0;
    size_t height = 0;

    constexpr inline size_t index(const size_t col, const size_t row) const noexcept {
        return row * width + col;}

public:
    // Constructors
    constexpr Matrix() noexcept = default;

    Matrix(const size_t w, const size_t h) noexcept: data(new CharacterHD[w * h]()), width(w), height(h) {}

    Matrix(const size_t w, const size_t h, const Pixel & p) noexcept : Matrix(w, h) { fill_pixel(p); }

    Matrix(const size_t w, const size_t h, const CharacterHD & c) noexcept  : Matrix(w, h) { fill_character(c); }

    // Copy constructor
    Matrix(const Matrix & other) noexcept : width(other.width), height(other.height), data(new CharacterHD[other.width * other.height]) 
    {copy_from(other);}

    // Destructor
    ~Matrix() noexcept {destroy(); }

      // Assignment operator: Releases memory and copies data from another matrix
    Matrix & operator=(const Matrix & other) noexcept { 
      destroy(); 
      create(other.get_width(), other.get_height()); 
      copy_from(other); 
      return *this;}

      // Releases allocated memory
    void destroy() noexcept {delete[] data; data = nullptr;}
    void create(const size_t w, const size_t h) noexcept {data = new CharacterHD[w * h]();}
    void copy_from(const Matrix & other) noexcept {std::copy(other.data, other.data + width * height, data);}
    void clear() noexcept {for (size_t i = 0; i < width * height; i++) data[i].clear();}

    // Accessors
    constexpr size_t get_width() const noexcept { return width; }
    constexpr size_t get_height() const noexcept { return height; }

    inline CharacterHD & get_character(const size_t col, const size_t row) noexcept {return data[index(col, row)];}
    inline const CharacterHD & get_character(const size_t col, const size_t row) const noexcept {return data[index(col, row)];}

    // Checks
    bool is_empty(const size_t col_start, const size_t col_stop, const size_t row_start, const size_t row_stop) const noexcept {
        for (size_t r = row_start; r < row_stop; r++)
            for (size_t c = col_start; c < col_stop; c++)
                if (!get_character(c, r).is_empty()) return false;
        return true;}

    // Modifiers
    inline void set_character(const size_t col, const size_t row, const CharacterHD & c) noexcept {get_character(col, row) = c;}
    inline void set_wcharacter(const size_t col, const size_t row, const wchar_t & cs) noexcept { get_character(col, row).set_wcharacter(cs);}
    inline void set_pixel(const size_t col, const size_t row, const Pixel & p) noexcept {get_character(col, row).set_pixel(p);}

    void fill_pixel(const Pixel & p = Pixel()) noexcept {for (size_t i = 0; i < width * height; i++) data[i].set_pixel(p);}
    void fill_character(const CharacterHD & c) noexcept {for (size_t i = 0; i < width * height; i++) data[i] = c;}

    // Resizes the matrix
    void resize(const size_t & w, const size_t & h) noexcept { 
        Matrix temp(*this);
        destroy(); 
        create(w, h); 
        copy_from(temp);} //???


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

    inline Matrix part(const size_t & col_start, const size_t & col_stop, const size_t & row_start, const size_t & row_stop) const noexcept {
        const size_t new_height = std::min(row_stop - row_start, height);
        const size_t new_width  = std::min(col_stop - col_start, get_width());

        Matrix m(new_width, new_height);

        for (size_t r = 0; r < new_height; r++) {
            const size_t row_index = row_start + r;
            for (size_t c = 0; c < new_width; c++) {
                m.get_character(c, r) = get_character(col_start + c, row_index);}}

        return m;}


    inline void insert_matrix(const size_t & col, const size_t & row, const Matrix & m) noexcept {
      const size_t h = m.get_height();
      const size_t w = m.get_width();

      // Clamp to avoid overflow (optional but safe)
      //if (row >= get_height() || col >= get_width()) return;

      const size_t max_r = std::min(h, get_height() - row);
      const size_t max_c = std::min(w, get_width() - col);

      for (size_t r = 0; r < max_r; ++r) {
          const size_t dest_index = (row + r) * get_width() + col;
          const size_t src_index  = r * w;
          for (size_t c = 0; c < max_c; ++c) {
              data[dest_index + c] = m.data[src_index + c];}}}


    inline void insert_matrix_aligned(const size_t & col, size_t row, const Matrix & m, const Alignment & ha = -1, const Alignment & va = -1) noexcept {
      const size_t H = get_height();
      const size_t W = get_width();
      const size_t mH = m.get_height();
      const size_t mW = m.get_width();

      // Apply vertical alignment offset
      const int v_disp = va.get_displacement(mH);
      row += v_disp;

      // Apply horizontal alignment offset
      const int h_disp = ha.get_displacement(mW);
      const size_t aligned_col = col + h_disp;

      // Compute effective copy region
      const size_t max_r = std::min(mH, H - row);
      const size_t max_c = std::min(mW, W - aligned_col);

      // Copy row by row with alignment applied
      for (size_t r = 0; r < max_r; ++r) {
          const size_t dest_index = (row + r) * W + aligned_col;
          const size_t src_index  = r * mW;
          for (size_t c = 0; c < max_c; ++c) {
              data[dest_index + c] = m.data[src_index + c];}}}

    // Insert operations
    void insert_wstring(const size_t col, const size_t row, const wstring & s) noexcept {for (size_t i = 0; i < s.size(); i++) get_character(col + i, row).set_wcharacter(s[i]);}

    // Insert a Colorize object into the matrix with alignment and optional checks.
    inline bool insert_colorized_aligned(const size_t & col, const size_t & row, const Colorize & s, const Alignment & ha = -1, const bool & check_space = false, const bool & change_color = true) noexcept 
      {if (row >= get_height() || col >= get_width()) return false;

      const size_t width  = get_width();
      const size_t height = get_height();
      const size_t slength = s.get_length();
      const int c = static_cast<int>(col) + ha.get_displacement(slength);

      // Compute insertion boundaries
      const size_t start = std::max<int>(0, c - 1);
      const size_t stop  = std::min(width, c + slength + 1);

      // Check boundaries and space availability
      if (check_space && (c < 0 || c + slength > width || !is_empty(start, stop, row, row + 1))) return false;

      // Insert characters directly into the matrix
        for (size_t i = 0; i < slength; ++i) {
            const size_t x = c + i;
            auto & ch = get_character(x, row);
            ch.set_wcharacter(s.get_wcharacter(i));
            if (change_color)  ch.set_pixel(s);}

        return true;}

    inline int insert_colorized_dynamically(const size_t & col, const size_t & row, const Colorize & s) noexcept {
        if (row >= height) return -1;

        const size_t w = s.get_length();
        const Vector<int> displacements = get_dynamic_displacements(w);

        for (int delta : displacements) {
            if (insert_colorized_aligned(col + delta, row, s, 0, true, true)) {
                return static_cast<int>(col) + delta;}}
        return -1;}

    inline void insert_point(const Point & p) noexcept {get_character(p.get_col(), p.get_row()).update(p);}

    inline void insert_points(const Points & points) noexcept {for (const Point & p : points) {insert_point(p);}}

    inline void to_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        const size_t total = width * height;
        for (size_t i = 0; i < total; ++i) {
            data[i].to_buffer(buffer, length_buffer);
            if ((i + 1) % width == 0 && (i + 1) != total) buffer[length_buffer++] = L'\n'; // Add newline after each row (except the last one)
        }}


    inline void to_colorless_buffer(wchar_t * buffer, size_t & length_buffer) const noexcept {
        const size_t total = width * height;
        for (size_t i = 0; i < total; ++i) {
            wchar_to_buffer(data[i].get_wcharacter(), buffer, length_buffer);
            if ((i + 1) % width == 0 && (i + 1) != total) buffer[length_buffer++] = L'\n'; // Add newline after each row (except the last one)
        }}


    wstring get_wstring(const bool colorless = false) const noexcept {
        wchar_t buffer[character_size_max * width * height + height + 1] = {0};
        size_t length = 0;
        if (colorless) to_colorless_buffer(buffer, length);
        else to_buffer(buffer, length);
        return wstring(buffer);}

    inline const wchar_t * get_cstring(const bool colorless = false) const noexcept {
        size_t required_size = character_size_max * get_width() * height + height + 1; // +1 for '\0'
        wchar_t * buffer = new wchar_t[required_size]; size_t length = 0;
        if (colorless) to_colorless_buffer(buffer, length);
        else to_buffer(buffer, length);
        buffer[length] = L'\0'; // Null terminator
        return buffer;}

      // inline void print(const bool colorless = false) const noexcept {
      //   const wchar_t * str = get_cstring(colorless);
      //   wcout.write(str, wcslen(str));
      //   wcout.flush();}


    inline void print(const bool colorless = false) const noexcept {
        const size_t total = width * height;
        for (size_t i = 0; i < total; ++i) {
            data[i].stream();
            if (not data[i].same_pixel(data[i + 1])) {wcout.write(ansi_end, 4);}
            if ((i + 1) % width == 0) {wcout.write(ansi_end, 4); if ((i + 1) != total) wcout.put(L'\n');}} // Add newline after each row (except the last one)
        wcout.flush();}
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
  //void matrix_insert_dots(Matrix * m, Dots * dots) noexcept {m->insert_dots(*dots);}
  void matrix_insert_points(Matrix * m, Points * dots) noexcept {m->insert_points(*dots);}

  void matrix_print(Matrix * matrix, bool colorless) noexcept {matrix->print(colorless);}

  Matrix * colorize_get_matrix(Colorize * c) noexcept {return new Matrix(colorize_to_matrix(*c));}


  void fast_print() {
    std::ios::sync_with_stdio(false);
    std::wcout.tie(nullptr);}

 
}
